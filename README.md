# SmartSupport AI

**SmartSupport AI** is an AI-powered customer support management system that automatically analyzes customer support tickets using machine learning.

The system classifies incoming tickets, predicts their priority and sentiment, estimates the expected resolution time, and provides dedicated interfaces for customers and administrators.

### Live Demo

**[SmartSupport AI](https://smart-support-ai-ten.vercel.app/)**

---

## Overview

SmartSupport AI is designed to automate the initial analysis and organization of customer support tickets.

When a customer submits a ticket, the backend processes the ticket through multiple machine learning models to determine:

* Ticket category
* Priority level
* Customer sentiment
* Estimated resolution time

The analyzed ticket is then stored in the database and made available to the customer and administrators according to their roles.

The application provides two separate portals:

* **Customer Portal** for submitting and tracking support tickets
* **Admin Portal** for managing tickets and viewing support analytics

---

## Features

### Customer Portal

* Customer registration and login
* JWT-based authentication
* Secure password hashing
* Submit support tickets
* Automatic AI ticket analysis
* Ticket category prediction
* Priority prediction
* Sentiment analysis
* Estimated resolution time
* View previously submitted tickets
* View ticket category and status
* Customer/Admin portal switching
* Secure logout

### Admin Portal

* Secure administrator login
* Role-based access control
* Admin-only dashboard
* View all customer tickets
* Dashboard statistics
* Category-based ticket exploration
* Category analytics
* Sentiment analytics
* Priority analytics
* Status analytics
* Ticket filtering
* View detailed ticket information
* Update ticket status
* Secure logout

---

# AI & Machine Learning

SmartSupport AI uses four machine learning models to analyze customer support tickets.

## 1. Ticket Category Classification

Predicts the type of customer support issue.

### Supported Categories

* Technical Issue
* Refund
* Delivery Issue
* Account Issue
* Cancellation
* Order Issue
* Subscription
* Payment Issue

### Model

* TF-IDF Vectorizer
* Logistic Regression

The model converts the ticket text into TF-IDF features and predicts the most relevant support category.

---

## 2. Ticket Priority Prediction

Predicts the urgency of a support ticket.

### Possible Priorities

* Low
* Medium
* High

### Model

* TF-IDF Vectorizer
* Logistic Regression

The predicted priority helps administrators identify tickets that may require faster attention.

---

## 3. Sentiment Analysis

Analyzes the sentiment expressed in the customer's ticket.

### Possible Sentiments

* Negative
* Neutral
* Positive

### Model

* TF-IDF Vectorizer
* Logistic Regression

The sentiment prediction provides additional context about the customer's experience and tone.

---

## 4. Resolution Time Prediction

Estimates the approximate number of hours required to resolve a ticket.

### Model

* TF-IDF Vectorizer
* Random Forest Regressor

### Development Performance

| Metric |      Result |
| ------ | ----------: |
| MAE    | ~2.53 hours |
| RMSE   | ~3.49 hours |
| R²     |       ~0.92 |

These metrics were obtained from the development/test dataset. They represent model performance on that dataset and should not be interpreted as guaranteed real-world resolution times.

---

# Ticket Processing Pipeline

Every newly submitted ticket passes through the complete prediction pipeline.

```text
Customer
   │
   ▼
Customer Portal
   │
   ▼
Submit Ticket
   │
   ▼
FastAPI Backend
   │
   ▼
AI Prediction Pipeline
   │
   ├── Category Model
   ├── Priority Model
   ├── Sentiment Model
   └── Resolution Time Model
   │
   ▼
Prediction Results
   │
   ▼
Save Ticket
   │
   ▼
PostgreSQL Database
   │
   ▼
Customer / Admin Portal
```

The predictions are generated from the submitted ticket text and stored together with the ticket record.

---

# System Architecture

```text
                    SmartSupport AI
                          │
             ┌────────────┴────────────┐
             │                         │
             ▼                         ▼
      Customer Portal             Admin Portal
             │                         │
             └────────────┬────────────┘
                          │
                          ▼
                   FastAPI Backend
                          │
                          ▼
                AI Prediction Pipeline
                          │
             ┌────────────┼────────────┐
             │            │            │
             ▼            ▼            ▼
         Category      Priority    Sentiment
             │            │            │
             └────────────┼────────────┘
                          │
                          ▼
                  Resolution Time
                          │
                          ▼
                   PostgreSQL DB
```

---

# Technology Stack

## Frontend

* React
* Vite
* React Router
* CSS

## Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* Uvicorn

## Authentication & Security

* JWT
* `python-jose`
* Argon2 password hashing
* `pwdlib`
* Role-based authorization
* Environment-based configuration

## Machine Learning

* Scikit-learn
* NumPy
* Joblib
* TF-IDF
* Logistic Regression
* Random Forest Regressor

## Database

* SQLite for local development
* PostgreSQL for production
* Neon PostgreSQL for the deployed application

## Deployment

* Vercel for the React frontend
* Render for the FastAPI backend
* Neon PostgreSQL for the production database

---

# Project Structure

```text
SmartSupport-AI/
│
├── datasets/
│   ├── category_tickets_improved.csv
│   ├── sentiment_tickets_clean.csv
│   └── resolution_tickets.csv
│
├── models/
│   ├── category_model.pkl
│   ├── category_tfidf_vectorizer.pkl
│   ├── priority_model.pkl
│   ├── priority_tfidf_vectorizer.pkl
│   ├── sentiment_model.pkl
│   ├── sentiment_tfidf_vectorizer.pkl
│   ├── resolution_model.pkl
│   └── resolution_tfidf_vectorizer.pkl
│
├── src/
│   ├── __init__.py
│   ├── api.py
│   ├── auth.py
│   ├── database.py
│   ├── ticket_prediction.py
│   └── create_admin.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── admin/
│   │   │   └── customer/
│   │   ├── services/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── ...
│   ├── package.json
│   └── ...
│
├── .env.example
├── .gitignore
├── render.yaml
├── requirements.txt
└── README.md
```

The `.env` file is created locally and is intentionally excluded from Git.

---

# Local Development

## 1. Clone the Repository

```bash
git clone https://github.com/goldersayantan/SmartSupport-AI.git

cd SmartSupport-AI
```

## 2. Create a Python Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

## 3. Install Backend Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
DATABASE_URL=sqlite:///./smartsupport.db
FRONTEND_URL=http://localhost:5173
```

Use `.env.example` as the configuration template.

**Never commit the `.env` file or production credentials to Git.**

---

## 5. Start the FastAPI Backend

From the project root:

```bash
uvicorn src.api:app --reload
```

The API will normally be available at:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 6. Create an Admin Account

Run:

```bash
python -m src.create_admin
```

Follow the prompts to create the administrator account.

Admin registration is intentionally not exposed through the customer-facing application.

---

# Frontend Setup

Open another terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Create a frontend `.env` file:

```env
VITE_API_URL=http://127.0.0.1:8000
```

Start the development server:

```bash
npm run dev
```

The frontend will normally be available at:

```text
http://localhost:5173
```

---

# Authentication

SmartSupport AI uses JWT-based authentication with role-based authorization.

## Customer

Customers can:

* Create an account
* Sign in
* Submit support tickets
* View their own tickets
* View ticket status
* Log out securely

## Administrator

Administrators can:

* Sign in through the Admin Portal
* View all customer tickets
* Analyze ticket data
* Filter tickets
* View ticket details
* Update ticket status
* Log out securely

Admin accounts are created privately using the admin creation script.

---

# API Endpoints

## Authentication

```text
POST /auth/signup
POST /auth/login
POST /auth/token
```

## Customer

```text
POST /predict
GET /tickets/my-tickets
```

## Admin

```text
GET /tickets
PATCH /tickets/{ticket_id}/status
```

## General

```text
GET /
```

---

# Database

## Local Development

SQLite is used for local development:

```env
DATABASE_URL=sqlite:///./smartsupport.db
```

This allows the application to run locally without requiring a separate database server.

## Production

The deployed application uses PostgreSQL hosted on Neon.

The production database connection is provided through the `DATABASE_URL` environment variable.

```env
DATABASE_URL=your-neon-postgresql-connection-string
```

Database credentials must never be committed to Git.

---

# Deployment

SmartSupport AI is deployed using a multi-service architecture:

```text
                    SmartSupport AI
                          │
             ┌────────────┴────────────┐
             │                         │
             ▼                         ▼
       React Frontend             FastAPI Backend
             │                         │
             ▼                         ▼
          Vercel                    Render
                                       │
                                       ▼
                              Neon PostgreSQL
```

### Production Services

| Component | Platform        |
| --------- | --------------- |
| Frontend  | Vercel          |
| Backend   | Render          |
| Database  | Neon PostgreSQL |

### Live Application

**https://smart-support-ai-ten.vercel.app/**

---

# Production Environment Variables

## Backend

The backend requires:

```env
SECRET_KEY=your-production-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
DATABASE_URL=your-neon-postgresql-connection-string
FRONTEND_URL=https://your-frontend-domain.vercel.app
```

## Frontend

The frontend requires:

```env
VITE_API_URL=https://your-backend-domain.onrender.com
```

Production secrets should be configured through the deployment platforms and must not be stored in GitHub.

---

# Render Configuration

The repository includes a `render.yaml` file for the FastAPI backend deployment.

The production server runs:

```bash
uvicorn src.api:app --host 0.0.0.0 --port $PORT
```

Python dependencies are installed using:

```bash
pip install -r requirements.txt
```

The backend connects to the production Neon PostgreSQL database using the `DATABASE_URL` environment variable.

---

# Security

SmartSupport AI includes several security measures:

* JWT-based authentication
* Argon2 password hashing
* Role-based authorization
* Protected admin endpoints
* Protected customer ticket endpoints
* Environment-based secret configuration
* Environment-based database configuration
* Environment-based CORS configuration
* `.env` excluded from Git
* Separate customer and administrator access

A strong randomly generated `SECRET_KEY` should always be used in production.

Database credentials, API secrets, JWT secrets, and other sensitive configuration values should never be committed to the repository.

---

# Machine Learning Model Storage

The backend requires the trained machine learning artifacts to perform predictions.

The model files include:

```text
models/
├── category_model.pkl
├── category_tfidf_vectorizer.pkl
├── priority_model.pkl
├── priority_tfidf_vectorizer.pkl
├── sentiment_model.pkl
├── sentiment_tfidf_vectorizer.pkl
├── resolution_model.pkl
└── resolution_tfidf_vectorizer.pkl
```

Each model is loaded by the backend prediction pipeline when processing customer tickets.

---

# Current Project Status

SmartSupport AI V2 is a completed full-stack application with:

* Customer authentication
* Administrator authentication
* JWT authorization
* Role-based access control
* AI ticket classification
* Priority prediction
* Sentiment analysis
* Resolution-time prediction
* Customer ticket history
* Admin dashboard
* Ticket analytics
* Ticket filtering
* Ticket details
* Ticket status management
* SQLite local database support
* PostgreSQL production database
* Environment-based configuration
* Trained ML model artifacts
* React frontend
* FastAPI backend
* Production deployment

The complete customer and administrator workflow has been implemented and deployed.

---

# Future Improvements

Potential future improvements include:

* Email notifications
* Password reset functionality
* Ticket conversations
* Real-time ticket updates
* Advanced AI-generated responses
* Knowledge-base integration
* Automatic ticket assignment
* Dedicated support-agent accounts
* Advanced PostgreSQL analytics
* Production monitoring
* Docker deployment
* CI/CD pipeline
* Larger and more diverse ML training datasets
* Automated model retraining
* AI-assisted ticket responses

---

# License

This project is currently intended as a personal/academic project.
