import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load Dataset
df = pd.read_csv("./tickets.csv")

# Input and Target
X = df["ticket"]
y = df["category"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state = 42, stratify=y
)

# TF-IDF
vectorizer = TfidfVectorizer()

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Create Logistic Regression
model = LogisticRegression(max_iter=1000)

# Model training
model.fit(X_train_tfidf, y_train)

# Prediction making
y_pred = model.predict(X_test_tfidf)

# Model Evaluation
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:")
print(accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("Model Training completed!")
print("\nFirst 10 Predictions: ")

for actual, predicted in zip(y_test.iloc[:10],y_pred[:10]):
    print(f"Actual: {actual} || Predicted: {predicted}")