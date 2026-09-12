import pandas as pd
import re

# Load dataset
df = pd.read_csv("./datasets/sentiment_tickets.csv")

print(df.head())
print("\nNumber of rows:", df.shape[0])
print("Number of columns:", df.shape[1])
print("\nColumns:")
print(df.columns)

print("\nSentiment Distribution:")
print(df["sentiment"].value_counts())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

df["cleaned_ticket"] = df["ticket"].apply(clean_text)

print("\nOriginal vs Cleaned Tickets:")
print(df[["ticket", "cleaned_ticket"]].head(10))