import pandas as pd
import re
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

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
X_test_tfidf = tfidf.transform(X_test)


# Log-transform target
y_train_log = np.log1p(y_train)


# Random Forest model
model = RandomForestRegressor(
    n_estimators=300,
    random_state=42,
    min_samples_leaf=2
)

model.fit(X_train_tfidf, y_train)


# Predictions
y_pred = model.predict(X_test_tfidf)


# Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)


print("Resolution Time Model")
print("-" * 40)
print(f"MAE  : {mae:.2f} hours")
print(f"MSE  : {mse:.2f}")
print(f"RMSE : {rmse:.2f} hours")
print(f"R²   : {r2:.2f}")