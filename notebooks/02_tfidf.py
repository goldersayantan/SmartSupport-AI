import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("./datasets/tickets.csv")

df["clean_ticket"] = df["ticket"].str.lower()

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["clean_ticket"])

print("Number of tickets: ", X.shape[0])
print("Number of features: ", X.shape[1])

print("\nTF-IDF matrix shape:")
print(X.shape)

print("\nFirst 20 features:")
print(vectorizer.get_feature_names_out()[:20])

print("\nFirst ticket:")
print(df["clean_ticket"].iloc[0])

print("\nTF-IDF values of first ticket:")
print(X[0].toarray())
