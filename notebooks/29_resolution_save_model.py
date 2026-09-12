import pandas as pd
import re
import pickle

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


# Save model
with open("./models/resolution_model.pkl", "wb") as file:
    pickle.dump(model, file)


# Save TF-IDF vectorizer
with open("./models/resolution_tfidf_vectorizer.pkl", "wb") as file:
    pickle.dump(tfidf, file)


print("Resolution model saved successfully!")
print("Saved: models/resolution_model.pkl")
print("Saved: models/resolution_tfidf_vectorizer.pkl")