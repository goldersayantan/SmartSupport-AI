import pandas as pd

df = pd.read_csv("./datasets/sentiment_tickets.csv")

negative = df[df["sentiment"] == "Negative"].sample(
    100,
    random_state=42
)

neutral = df[df["sentiment"] == "Neutral"].sample(
    100,
    random_state=42
)

positive = df[df["sentiment"] == "Positive"].sample(
    100,
    random_state=42
)

df_balanced = pd.concat(
    [negative, neutral, positive],
    ignore_index=True
)

df_balanced = df_balanced.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

df_balanced.to_csv(
    "./datasets/sentiment_tickets_clean.csv",
    index=False
)

print("Balanced dataset:")
print(df_balanced["sentiment"].value_counts())
print("\nTotal rows:", len(df_balanced))