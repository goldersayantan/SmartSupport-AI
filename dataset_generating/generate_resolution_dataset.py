import pandas as pd
import random


random.seed(42)


# --------------------------------------------------
# Resolution ticket templates
# --------------------------------------------------

ticket_templates = [

    # Account Issues
    ("Account Issue", "How can I change my email address?", 1, 3),
    ("Account Issue", "I want to update my phone number", 1, 3),
    ("Account Issue", "I need to update my profile information", 1, 3),
    ("Account Issue", "I forgot my password and cannot log in", 2, 5),
    ("Account Issue", "My account is locked and I cannot access it", 3, 7),
    ("Account Issue", "Someone accessed my account and I cannot log in", 6, 12),

    # Delivery Issues
    ("Delivery Issue", "Where is my package?", 5, 10),
    ("Delivery Issue", "My delivery is slightly delayed", 6, 12),
    ("Delivery Issue", "My parcel has been delayed for several days", 10, 20),
    ("Delivery Issue", "The tracking information has not been updated", 8, 16),
    ("Delivery Issue", "My package has not arrived", 18, 30),
    ("Delivery Issue", "My package is missing and the delivery shows completed", 24, 40),

    # Payment Issues
    ("Payment Issue", "My payment failed", 3, 7),
    ("Payment Issue", "My card payment was declined", 3, 8),
    ("Payment Issue", "My payment failed but money was deducted", 7, 15),
    ("Payment Issue", "I was charged twice for the same transaction", 8, 16),
    ("Payment Issue", "There is an unknown transaction on my card", 10, 20),
    ("Payment Issue", "A large unauthorized payment was made from my account", 15, 30),

    # Refund Issues
    ("Refund", "I want a refund for my order", 18, 30),
    ("Refund", "I requested a refund for my purchase", 20, 32),
    ("Refund", "My refund has not arrived yet", 24, 40),
    ("Refund", "The refund was approved but I have not received the money", 30, 48),
    ("Refund", "I have been waiting several days for my refund", 36, 60),
    ("Refund", "My refund amount is incorrect", 30, 55),

    # Cancellation
    ("Cancellation", "I want to cancel my order", 2, 5),
    ("Cancellation", "Please cancel my recent purchase", 2, 6),
    ("Cancellation", "I need to cancel an order that has not shipped", 2, 6),
    ("Cancellation", "I want to cancel my order but it has already been processed", 5, 12),
    ("Cancellation", "I need help cancelling an order that has already shipped", 10, 20),

    # Technical Issues
    ("Technical Issue", "The website is not loading properly", 4, 10),
    ("Technical Issue", "The website keeps freezing", 5, 12),
    ("Technical Issue", "I cannot place an order because the website crashes", 8, 16),
    ("Technical Issue", "The payment page is not working", 8, 18),
    ("Technical Issue", "The app keeps crashing when I try to use it", 8, 18),
    ("Technical Issue", "The website is completely unavailable", 15, 30),

    # Subscription
    ("Subscription", "How can I change my subscription plan?", 2, 5),
    ("Subscription", "I want to cancel my subscription", 2, 6),
    ("Subscription", "I was charged for my subscription", 5, 10),
    ("Subscription", "I was charged after cancelling my subscription", 8, 18),
    ("Subscription", "My subscription benefits are not working", 8, 18),
    ("Subscription", "I cannot access my paid subscription", 10, 22),

    # Order Issues
    ("Order Issue", "Where can I see my order status?", 5, 10),
    ("Order Issue", "My order information is incorrect", 6, 12),
    ("Order Issue", "My order is incomplete", 10, 20),
    ("Order Issue", "An item is missing from my order", 12, 24),
    ("Order Issue", "I received the wrong item", 15, 28),
    ("Order Issue", "My entire order is missing", 20, 36),
]


# --------------------------------------------------
# Prefixes and suffixes
# --------------------------------------------------

prefixes = [
    "",
    "Please help me,",
    "I need help because",
    "I am having a problem because",
    "I need assistance because",
    "Can you help me with this?",
    "I am facing an issue where",
]

suffixes = [
    "",
    "Can you check this?",
    "Please help me.",
    "Can you look into this?",
    "I need this resolved.",
    "Please resolve this issue.",
]


# --------------------------------------------------
# Generate dataset
# --------------------------------------------------

data = []

samples_per_template = 35

for category, template, min_hours, max_hours in ticket_templates:

    for _ in range(samples_per_template):

        prefix = random.choice(prefixes)
        suffix = random.choice(suffixes)

        # Build ticket text
        if prefix == "":
            ticket = template
        elif prefix.endswith("?"):
            ticket = f"{prefix} {template}"
        else:
            ticket = f"{prefix} {template}"

        if suffix:
            ticket = f"{ticket} {suffix}"

        # Add small random variation to resolution time
        resolution_time = random.uniform(min_hours, max_hours)

        data.append([
            ticket,
            resolution_time
        ])


# --------------------------------------------------
# Create DataFrame
# --------------------------------------------------

df = pd.DataFrame(
    data,
    columns=[
        "ticket",
        "resolution_time_hours"
    ]
)


# Round resolution time
df["resolution_time_hours"] = df[
    "resolution_time_hours"
].round(1)


# Remove duplicate tickets
df = df.drop_duplicates(subset=["ticket"])


# Shuffle dataset
df = df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)


# --------------------------------------------------
# Save dataset
# --------------------------------------------------

df.to_csv(
    "./resolution_tickets.csv",
    index=False
)


# --------------------------------------------------
# Display information
# --------------------------------------------------

print("Dataset created successfully!")

print("\nTotal samples:", len(df))

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 10 rows:")
print(df.head(10))

print("\nResolution Time Statistics:")
print(df["resolution_time_hours"].describe())

print("\nResolution Time Range:")
print(
    "Minimum:",
    df["resolution_time_hours"].min(),
    "hours"
)

print(
    "Maximum:",
    df["resolution_time_hours"].max(),
    "hours"
)