import pandas as pd
import re

df = pd.read_csv("priority_tickets.csv")

print(df.head())
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

print(df.columns)

print("\nPriority distribution:")
print(df["priority"].value_counts())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

df["cleaned_ticket"] = df["ticket"].apply(clean_text)

print("\nOriginal vs Cleaned Tickets:")
print(df[["ticket", "cleaned_ticket"]].head(10))