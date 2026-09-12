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

tfidf = TfidfVectorizer()

X_train_tfidf = tfidf.fit_transform(X_train)

model = LogisticRegression(max_iter=1000)

model.fit(X_train_tfidf, y_train)

new_tickets = [
    "I am extremely happy with the service",
    "My payment failed and I am very angry",
    "Can you tell me where my package is?",
    "Thank you for resolving my issue quickly",
    "This is a terrible experience and I am frustrated",
    "I need information about changing my account details"
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
    print("Predicted Sentiment:", prediction)
    print("-" * 60)