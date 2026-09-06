import joblib

# Load saved files
vectorizer = joblib.load(
    "tfidf_vectorizer.pkl"
)

model = joblib.load(
    "ticket_category_model.pkl"
)

# New customer tickets
new_tickets = [
    "Someone used my account and I cannot log in",
    "My payment was deducted but the order failed",
    "The delivery is two days late",
    "The website keeps freezing",
    "I need to cancel my purchase"
]

# Convert tickets to TF-IDF
tickets_tfidf = vectorizer.transform(
    new_tickets
)

# Predict categories
predictions = model.predict(
    tickets_tfidf
)

# Display results
print("Predictions using saved model:\n")

for ticket, prediction in zip(
    new_tickets,
    predictions
):
    print("Ticket:", ticket)
    print("Predicted Category:", prediction)
    print("-" * 60)