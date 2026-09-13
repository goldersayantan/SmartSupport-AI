from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.ticket_prediction import predict_ticket

app = FastAPI(title = "SmartSupport AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class TicketRequest(BaseModel):
    ticket: str

@app.get("/")
def home():
    return  {
        "message": "SmartSupport AI API is running."
    }

@app.post("/predict")
def predict(request: TicketRequest):
    result = predict_ticket(request.ticket)
    return result
