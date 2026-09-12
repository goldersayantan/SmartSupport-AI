import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("./datasets/sentiment_tickets.csv")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

df["cleaned_ticket"] = df["ticket"].apply(clean_text)

X = df["cleaned_ticket"]
y = df["sentiment"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

tfidf = TfidfVectorizer(
    ngram_range=(1, 2)
)

X_train_tfidf = tfidf.fit_transform(X_train)

model = LogisticRegression(max_iter=1000)

model.fit(X_train_tfidf, y_train)

test_tickets = [
    "My package has been delayed for five days",
    "I was charged twice for the same purchase",
    "My payment failed but money was deducted from my bank account",
    "I was charged for my subscription even though I cancelled it",
    "My refund has not arrived yet",
    "The website keeps crashing",
    "I cannot log into my account",
    
    "How can I change my email address?",
    "Where can I track my package?",
    "What is the refund policy?",
    "How do I cancel my order?",
    "Where can I see my payment history?",
    
    "My package arrived on time",
    "My payment was completed successfully",
    "The support team solved my problem",
    "I received my refund successfully",
    "Everything is working perfectly now"
]

cleaned_tests = [
    clean_text(ticket)
    for ticket in test_tickets
]

test_tfidf = tfidf.transform(cleaned_tests)

predictions = model.predict(test_tfidf)

print("Real-World Sentiment Tests")
print("=" * 50)

for ticket, prediction in zip(test_tickets, predictions):
    print(f"Ticket: {ticket}")
    print(f"Predicted Sentiment: {prediction}")
    print("-" * 50)