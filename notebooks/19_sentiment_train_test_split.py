import pandas as pd
import re
from sklearn.model_selection import train_test_split

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

print("Total samples:", len(df))
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))
print("\nTraining sentiment distribution:")
print(y_train.value_counts())
print("\nTesting sentiment distribution:")
print(y_test.value_counts())