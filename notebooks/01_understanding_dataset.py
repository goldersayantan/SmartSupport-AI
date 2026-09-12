import pandas as pd
import re

df = pd.read_csv("./datasets/category_tickets.csv")

df["clean_ticket"] = df["ticket"].str.lower()
df["clean_ticket"] = df["clean_ticket"].apply(
    lambda text: re.sub(r"[^\w\s]", " ", text)
)

df["clean_ticket"] = df["clean_ticket"].str.split().str.join(" ")

print(
    df[["ticket", "clean_ticket"]]
    .head(10)
    .to_string(index=False)
)

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nCategory distribution:")
print(df["category"].value_counts())

print("\nSample data:")
print(df.sample(10, random_state=42))
