import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# Load dataset
df = pd.read_csv("./datasets/category_tickets.csv")

X = df["ticket"]
y = df["category"]


# Split data
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


# Train model
model = LogisticRegression(max_iter=1000)

model.fit(X_train_tfidf, y_train)


# Save using pickle
with open("category_tfidf_vectorizer.pkl", "wb") as file:
    pickle.dump(vectorizer, file)

with open("category_model.pkl", "wb") as file:
    pickle.dump(model, file)


print("Category model and TF-IDF vectorizer saved successfully!")