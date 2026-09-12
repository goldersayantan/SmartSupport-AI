import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("./datasets/sentiment_tickets.csv")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

df["cleaned_ticket"] = df["ticket"].apply(clean_text)

X = df["cleaned_ticket"]

tfidf = TfidfVectorizer()

X_tfidf = tfidf.fit_transform(X)

print("Original text:")
print(X.iloc[0])

print("\nTF-IDF shape:")
print(X_tfidf.shape)

print("\nNumber of features:")
print(len(tfidf.get_feature_names_out()))

print("\nFirst 20 features:")
print(tfidf.get_feature_names_out()[:20])