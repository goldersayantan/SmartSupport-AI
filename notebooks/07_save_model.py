import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("./tickets.csv")

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

# Train Model
model = LogisticRegression(
    max_iter=1000
)

model.fit(X_train_tfidf, y_train)

# Save TF-IDF Vectorizer
joblib.dump(
    vectorizer,
    "tfidf_vectorizer.pkl"
)

# Save ML Model
joblib.dump(
    model,
    "ticket_category_model.pkl"
)

print("Model and TF-IDF vectorizer saved successfully!")