import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("./datasets/category_tickets.csv")

X = df["ticket"]
y = df["category"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.20, random_state = 42, stratify = y
)

print("Total tickets: ", len(df))
print("Training tickets: ", len(X_train))
print("Testing tickets: ", len(X_test))

print("\nTraining category distribution: ")
print(y_train.value_counts())

print("\nTesting category distribution: ")
print(y_test.value_counts())