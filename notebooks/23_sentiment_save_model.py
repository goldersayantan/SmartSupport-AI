import pandas as pd
import re
import pickle
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

with open("sentiment_tfidf_vectorizer.pkl", "wb") as file:
    pickle.dump(tfidf, file)

with open("sentiment_model.pkl", "wb") as file:
    pickle.dump(model, file)


print("sentiment model saved successfully!")
print("Saved: sentiment_tfidf_vectorizer.pkl")
print("Saved: sentiment_model.pkl")