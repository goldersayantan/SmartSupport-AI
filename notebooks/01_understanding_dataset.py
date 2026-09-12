import pandas as pd
import re

df = pd.read_csv("./datasets/tickets.csv")

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