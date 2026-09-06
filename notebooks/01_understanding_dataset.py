import pandas as pd
import re

df = pd.read_csv("./tickets.csv")

# Convert text to lowercase
df["clean_ticket"] = df["ticket"].str.lower()

# Replace punctuation with spaces
df["clean_ticket"] = df["clean_ticket"].apply(
    lambda text: re.sub(r"[^\w\s]", " ", text)
)

# Remove extra spaces
df["clean_ticket"] = df["clean_ticket"].str.split().str.join(" ")

# Display original and cleaned text
print(
    df[["ticket", "clean_ticket"]]
    .head(10)
    .to_string(index=False)
)