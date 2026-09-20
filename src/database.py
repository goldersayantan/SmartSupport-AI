import os

from dotenv import load_dotenv
from sqlalchemy import (create_engine, Column, Integer, String, Float, DateTime, ForeignKey)
from sqlalchemy.orm import ( declarative_base, sessionmaker)
from datetime import datetime

# --------------------------------
# Environment Variables
# --------------------------------

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgresql://",
        "postgresql+psycopg://",
        1
    )

if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL is not configured."
    )

# --------------------------------
# Database Engine
# --------------------------------

connect_args = {}

if DATABASE_URL.startswith("sqlite"):
    connect_args = {
        "check_same_thread": False
    }

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args
)

# --------------------------------
# Session
# --------------------------------

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# --------------------------------
# User Model
# --------------------------------

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, default="customer", nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

# --------------------------------
# Ticket Model
# --------------------------------

class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True,index=True)
    customer_name = Column(String, default="Anonymous")
    customer_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    ticket = Column(String, nullable=False)
    category = Column(String)
    priority = Column(String)
    sentiment = Column(String)
    resolution_time_hours = Column(Float)
    status = Column(String, default="Open")
    created_at = Column(DateTime, default=datetime.utcnow)

# --------------------------------
# Create Tables
# --------------------------------

Base.metadata.create_all(
    bind=engine
)

