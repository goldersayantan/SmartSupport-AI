import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("./datasets/tickets.csv")

# Input and target
X = df["ticket"]
y = df["category"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# TF-IDF
vectorizer = TfidfVectorizer()

X_train_tfidf = vectorizer.fit_transform(X_train)

# Train Logistic Regression
model = LogisticRegression(max_iter=1000)

model.fit(X_train_tfidf, y_train)

# New unseen tickets
new_tickets = [
    "My card was charged but the order was not completed",
    "I cannot remember my account password",
    "My package is still not here",
    "I want to get my money back for this purchase",
    "The application crashes whenever I try to open it",
    "I want to stop my current order",
    "I received a damaged product",
    "I want to upgrade my current plan"
]

# Convert new tickets to TF-IDF
new_tickets_tfidf = vectorizer.transform(new_tickets)

# Predict categories
predictions = model.predict(new_tickets_tfidf)

# Display predictions
print("Predictions for new tickets:\n")

for ticket, prediction in zip(new_tickets, predictions):
    print("Ticket:", ticket)
    print("Predicted Category:", prediction)
    print("-" * 60)