import pandas as pd
import re
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestRegressor


# Load dataset
df = pd.read_csv("./datasets/resolution_tickets.csv")


# Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


df["cleaned_ticket"] = df["ticket"].apply(clean_text)


# Input and target
X = df["cleaned_ticket"]
y = df["resolution_time_hours"]


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# TF-IDF
tfidf = TfidfVectorizer()

X_train_tfidf = tfidf.fit_transform(X_train)


# Random Forest Regression
model = RandomForestRegressor(
    n_estimators=300,
    random_state=42,
    min_samples_leaf=2
)

model.fit(X_train_tfidf, y_train)


# Test tickets
test_tickets = [
    "I want to cancel my order",
    "Please cancel my purchase",
    "I need to cancel my order immediately",
    "I accidentally placed the wrong order and want to cancel it",
    "Can you cancel my order before it ships?"
]


# Transform test tickets
test_cleaned = [clean_text(ticket) for ticket in test_tickets]

test_tfidf = tfidf.transform(test_cleaned)


# Predict
predicted_hours = model.predict(test_tfidf)


# Display predictions
print("\nNew Ticket Predictions")
print("=" * 60)

for ticket, hours in zip(test_tickets, predicted_hours):
    print(f"Ticket: {ticket}")
    print(f"Predicted Resolution Time: {hours:.2f} hours")
    print("-" * 60)