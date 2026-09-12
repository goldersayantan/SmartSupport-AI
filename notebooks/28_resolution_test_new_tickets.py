import pandas as pd
import re

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression


# Load dataset
df = pd.read_csv("./datasets/resolution_tickets.csv")


# Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


df["cleaned_ticket"] = df["ticket"].apply(clean_text)


# Features and target
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


# Train regression model
model = LinearRegression()

model.fit(X_train_tfidf, y_train)


# New tickets
new_tickets = [
    "I need to change the email linked to my account",
    "My parcel has been delayed for three days",
    "There is a transaction on my card that I don't recognize",
    "My payment failed but money was deducted",
    "I want to cancel my order",
    "I have been waiting for my refund",
    "The website keeps freezing",
    "I was charged twice for the same order"
]


# Clean new tickets
cleaned_tickets = [
    clean_text(ticket) for ticket in new_tickets
]


# Convert to TF-IDF
new_tickets_tfidf = tfidf.transform(cleaned_tickets)


# Predict resolution time
predictions = model.predict(new_tickets_tfidf)


# Display predictions
print("\nPredictions for New Tickets:\n")

for ticket, prediction in zip(new_tickets, predictions):
    print("Ticket:", ticket)
    print(f"Predicted Resolution Time: {prediction:.2f} hours")
    print("-" * 60)