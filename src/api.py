from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from src.ticket_prediction import predict_ticket
from src.database import SessionLocal, Ticket
from src.auth import (hash_password, verify_password, create_access_token, get_current_user, get_current_admin)
from src.database import User
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException
import os
from dotenv import load_dotenv

app = FastAPI(title="SmartSupport AI")

load_dotenv()

FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TicketRequest(BaseModel):
    ticket: str
    customer_name: str = "Anonymous"

class SignupRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

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

@app.head("/")
def head():
    return

@app.post("/predict")
def predict(
    request: TicketRequest,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    # Run AI prediction
    result = predict_ticket(request.ticket)

    # Create database record

    new_ticket = Ticket(
        customer_name=request.customer_name,
        customer_id=current_user["user_id"],
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
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
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
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
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


@app.post("/auth/signup")
def signup(
    request: SignupRequest,
    db: Session = Depends(get_db)
):
    # Check whether the email already exists
    existing_user = (
        db.query(User)
        .filter(User.email == request.email)
        .first()
    )

    if existing_user:
        return {
            "error": "Email already registered"
        }

    # Hash the password before storing it
    hashed_password = hash_password(
        request.password
    )

    # Create the customer
    user = User(
        name=request.name,
        email=request.email,
        password_hash=hashed_password,
        role="customer"
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "message": "Account created successfully",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        }
    }


@app.post("/auth/login")
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    # Find user by email
    user = (
        db.query(User)
        .filter(User.email == request.email)
        .first()
    )

    # Don't reveal whether the email exists
    if not user:
        return {
            "error": "Invalid email or password"
        }

    # Verify password
    if not verify_password(
        request.password,
        user.password_hash
    ):
        return {
            "error": "Invalid email or password"
        }

    # Create JWT token
    access_token = create_access_token(
        user_id=user.id,
        role=user.role
    )

    return {
        "message": "Login successful",
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        }
    }


@app.post("/auth/token")
def login_for_swagger(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(User.email == form_data.username)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(
        form_data.password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        user_id=user.id,
        role=user.role
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@app.get("/tickets/my-tickets")
def get_my_tickets(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    tickets = (
        db.query(Ticket)
        .filter(
            Ticket.customer_id == current_user["user_id"]
        )
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


