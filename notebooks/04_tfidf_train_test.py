import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("./datasets/category_tickets.csv")

X = df["ticket"]
y = df["category"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

vectorizer = TfidfVectorizer()

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

print("Training tickets:", X_train.shape[0])
print("Testing tickets:", X_test.shape[0])

print("\nTraining TF-IDF shape:")
print(X_train_tfidf.shape)

print("\nTesting TF-IDF shape:")
print(X_test_tfidf.shape)

print("\nNumber of TF-IDF features:")
print(len(vectorizer.get_feature_names_out()))

print("\nFirst 20 features:")
print(vectorizer.get_feature_names_out()[:20])