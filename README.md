# SmartSupport AI

SmartSupport AI is an AI-powered customer support system that automatically analyzes customer support tickets and helps support teams manage them efficiently.

The system uses machine learning to classify support tickets, determine their priority and sentiment, and estimate the expected resolution time.

It provides separate portals for **Customers** and **Administrators**.

---

## Features

### Customer Portal

* Customer registration and login
* Secure JWT authentication
* Submit support tickets
* Automatic AI ticket analysis
* Ticket category prediction
* Priority prediction
* Sentiment analysis
* Estimated resolution time
* View previously submitted tickets
* View ticket category and current status
* Customer/Admin portal switching
* Secure logout

### Admin Portal

* Secure admin login
* Admin-only dashboard
* View all customer tickets
* Dashboard ticket statistics
* Category-based ticket exploration
* Category analytics
* Sentiment analytics
* Priority analytics
* Status analytics
* Ticket filtering
* View ticket details
* Update ticket status
* Secure admin logout

---

## AI / Machine Learning

SmartSupport AI currently uses four machine learning models.

### 1. Ticket Category Classification

Predicts the type of customer support issue.

Supported categories:

* Technical Issue
* Refund
* Delivery Issue
* Account Issue
* Cancellation
* Order Issue
* Subscription
* Payment Issue

Model:

* TF-IDF Vectorizer
* Logistic Regression

The model predicts the category of a newly submitted customer support ticket.

---

### 2. Ticket Priority Prediction

Predicts the priority level of a support ticket.

Possible priorities:

* Low
* Medium
* High

Model:

* TF-IDF Vectorizer
* Logistic Regression

---

### 3. Sentiment Analysis

Determines the customer's sentiment from the submitted ticket.

Possible sentiments:

* Negative
* Neutral
* Positive

Model:

* TF-IDF Vectorizer
* Logistic Regression

---

### 4. Resolution Time Prediction

Estimates how many hours may be required to resolve a support ticket.

Model:

* TF-IDF Vectorizer
* Random Forest Regressor

Model performance during development:

* MAE: approximately 2.53 hours
* RMSE: approximately 3.49 hours
* R²: approximately 0.92

These metrics are based on the development/test dataset and should not be interpreted as guaranteed real-world resolution times.

---

## System Architecture

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
    ├── Category
    ├── Priority
    ├── Sentiment
    └── Resolution Time
    │
    ▼
Database
    │
    ├── Customer Accounts
    ├── Customer Tickets
    └── Ticket Status
    │
    ▼
Admin Portal
    │
    ├── Dashboard
    ├── Categories
    ├── Analytics
    └── Ticket Management
```

---

## Technology Stack

### Frontend

* React
* Vite
* React Router
* CSS

### Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* Uvicorn

### Authentication

* JWT
* `python-jose`
* Argon2 password hashing
* `pwdlib`

### Machine Learning

* Scikit-learn
* NumPy
* Joblib
* TF-IDF
* Logistic Regression
* Random Forest Regressor

### Database

* SQLite for local development
* PostgreSQL for production
* Neon PostgreSQL for the production database

### Deployment

* Vercel for the React frontend
* Render for the FastAPI backend
* Neon PostgreSQL for the production database

---

## Project Structure

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

> The `.env` file is created locally and is intentionally excluded from Git.

---

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/goldersayantan/SmartSupport-AI.git

cd SmartSupport-AI
```

---

### 2. Create a Python virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file in the project root.

For local development:

```env
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
DATABASE_URL=sqlite:///./smartsupport.db
FRONTEND_URL=http://localhost:5173
```

Never commit the `.env` file to Git.

Use `.env.example` as the configuration template.

For production, environment variables are configured through the deployment platforms rather than committed to the repository.

---

### 5. Start the FastAPI backend

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

### 6. Create the first admin account

Run:

```bash
python -m src.create_admin
```

Follow the prompts to create the administrator account.

Admin registration is intentionally not exposed through the customer-facing application.

---

## Frontend Setup

Open another terminal and move into the frontend:

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

## Authentication

SmartSupport AI uses JWT-based authentication with role-based authorization.

### Customer

Customers can:

1. Create an account
2. Sign in
3. Submit support tickets
4. View their own tickets
5. View ticket status
6. Log out securely

### Admin

Administrators can:

1. Sign in through the Admin Portal
2. View all customer tickets
3. Analyze ticket data
4. Filter tickets
5. View ticket details
6. Update ticket status
7. Log out securely

Admin accounts are created privately using the admin creation script.

---

## API Endpoints

### Authentication

```text
POST /auth/signup
POST /auth/login
POST /auth/token
```

### Customer

```text
POST /predict
GET /tickets/my-tickets
```

### Admin

```text
GET /tickets
PATCH /tickets/{ticket_id}/status
```

### General

```text
GET /
```

---

## Ticket Prediction Pipeline

When a customer submits a ticket, the backend processes it through the complete AI prediction pipeline.

```text
Customer Ticket
      │
      ▼
FastAPI /predict
      │
      ▼
Ticket Prediction Pipeline
      │
      ├── Category Model
      │
      ├── Priority Model
      │
      ├── Sentiment Model
      │
      └── Resolution Time Model
      │
      ▼
Prediction Result
      │
      ▼
Save Ticket to Database
      │
      ▼
Return Result to Customer
```

Each prediction is generated from the ticket text and stored together with the ticket record.

---

## Database

### Local Development

The project uses SQLite for local development:

```env
DATABASE_URL=sqlite:///./smartsupport.db
```

This allows the application to run locally without requiring a separate database server.

### Production

The production environment uses PostgreSQL hosted on Neon.

The production database URL is provided through the deployment environment:

```env
DATABASE_URL=your-neon-postgresql-connection-string
```

The production database connection string must never be committed to Git.

---

## Deployment

SmartSupport AI is being prepared for cloud deployment using:

* **Vercel** — React frontend
* **Render** — FastAPI backend
* **Neon** — PostgreSQL database

Production architecture:

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

### Production Environment Variables

The backend requires:

```env
SECRET_KEY=your-production-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
DATABASE_URL=your-neon-postgresql-connection-string
FRONTEND_URL=https://your-frontend-domain.vercel.app
```

The frontend requires:

```env
VITE_API_URL=https://your-backend-domain.onrender.com
```

Production secrets should be configured through the hosting platforms and should not be stored in GitHub.

---

## Render Configuration

The repository contains a `render.yaml` file that defines the FastAPI web service configuration.

The backend is started using:

```bash
uvicorn src.api:app --host 0.0.0.0 --port $PORT
```

Render installs the required Python packages using:

```bash
pip install -r requirements.txt
```

The production backend uses the Neon PostgreSQL connection through the `DATABASE_URL` environment variable.

---

## Security

The application includes:

* Password hashing with Argon2
* JWT authentication
* Role-based authorization
* Protected admin endpoints
* Protected customer ticket endpoints
* Environment-based secret configuration
* Environment-based database configuration
* Environment-based CORS configuration
* `.env` excluded from Git

The production deployment should use a strong randomly generated `SECRET_KEY`.

Database credentials and other sensitive environment variables should never be committed to the repository.

---

## Machine Learning Model Storage

The trained machine learning models are required by the backend prediction pipeline.

The model files include:

```text
category_model.pkl
category_tfidf_vectorizer.pkl

priority_model.pkl
priority_tfidf_vectorizer.pkl

sentiment_model.pkl
sentiment_tfidf_vectorizer.pkl

resolution_model.pkl
resolution_tfidf_vectorizer.pkl
```

For deployment, these model artifacts must be available to the backend environment.

The models should be stored using an appropriate deployment strategy rather than exposing sensitive or unnecessary development artifacts.

---

## Future Improvements

Possible future improvements include:

* Email notifications
* Password reset
* Ticket conversations
* Real-time ticket updates
* Advanced AI response generation
* Knowledge-base integration
* Automatic ticket assignment
* Agent accounts
* Advanced PostgreSQL analytics
* Production monitoring
* Docker deployment
* CI/CD pipeline
* Improved ML models using larger real-world datasets
* Model retraining pipeline
* AI-assisted ticket responses

---

## Project Status

SmartSupport AI V2 currently includes:

* Customer authentication
* Admin authentication
* JWT authorization
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
* SQLite local database
* PostgreSQL production database configuration
* Environment-based configuration
* Render deployment configuration

The application has been tested locally with the complete customer and administrator workflow.

The project is currently being prepared for production deployment using:

**Vercel + Render + Neon PostgreSQL**

---

## License

This project is currently intended as a personal/academic project.
