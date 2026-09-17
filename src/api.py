from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session

from src.ticket_prediction import predict_ticket
from src.database import SessionLocal, Ticket


app = FastAPI(title="SmartSupport AI")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TicketRequest(BaseModel):
    ticket: str
    customer_name: str = "Anonymous"


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {
        "message": "SmartSupport AI API is running"
    }


@app.post("/predict")
def predict(
    request: TicketRequest,
    db: Session = Depends(get_db)
):

    # Run AI prediction
    result = predict_ticket(request.ticket)

    # Create database record
    new_ticket = Ticket(
        customer_name=request.customer_name,
        ticket=request.ticket,
        category=result["category"],
        priority=result["priority"],
        sentiment=result["sentiment"],
        resolution_time_hours=result["resolution_time_hours"],
        status="Open"
    )

    # Save ticket
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    return {
        "id": new_ticket.id,
        "customer_name": new_ticket.customer_name,
        "ticket": request.ticket,
        "category": result["category"],
        "priority": result["priority"],
        "sentiment": result["sentiment"],
        "resolution_time_hours": result["resolution_time_hours"],
        "status": new_ticket.status
    }


@app.get("/tickets")
def get_tickets(
    db: Session = Depends(get_db)
):

    tickets = (
        db.query(Ticket)
        .order_by(Ticket.created_at.desc())
        .all()
    )

    return [
        {
            "id": ticket.id,
            "customer_name": ticket.customer_name,
            "ticket": ticket.ticket,
            "category": ticket.category,
            "priority": ticket.priority,
            "sentiment": ticket.sentiment,
            "resolution_time_hours": ticket.resolution_time_hours,
            "status": ticket.status,
            "created_at": ticket.created_at
        }
        for ticket in tickets
    ]

class StatusUpdate(BaseModel):
    status: str


@app.patch("/tickets/{ticket_id}/status")
def update_ticket_status(
    ticket_id: int,
    request: StatusUpdate,
    db: Session = Depends(get_db)
):

    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if not ticket:
        return {
            "error": "Ticket not found"
        }

    ticket.status = request.status

    db.commit()
    db.refresh(ticket)

    return {
        "message": "Ticket status updated successfully",
        "id": ticket.id,
        "status": ticket.status
    }