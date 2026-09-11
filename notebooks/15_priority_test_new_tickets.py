import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("./priority_tickets.csv")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

df["cleaned_ticket"] = df["ticket"].apply(clean_text)

X = df["cleaned_ticket"]
y = df["priority"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

tfidf = TfidfVectorizer()

X_train_tfidf = tfidf.fit_transform(X_train)

model = LogisticRegression(max_iter=1000)

model.fit(X_train_tfidf, y_train)

new_tickets = [
    "I need to change the email linked to my account",
    "My parcel has been delayed for three days",
    "There is a transaction on my card that I don't recognize",
    "How do I update my profile information?",
    "My shipment is still in transit",
    "Someone made a payment using my account"
]

new_tickets_cleaned = [
    clean_text(ticket)
    for ticket in new_tickets
]

new_tickets_tfidf = tfidf.transform(new_tickets_cleaned)

predictions = model.predict(new_tickets_tfidf)
print("\nPredictions for new tickets:\n")

for ticket, prediction in zip(new_tickets, predictions):
    print("Ticket:", ticket)
    print("Predicted Priority:", prediction)
    print("-" * 60)