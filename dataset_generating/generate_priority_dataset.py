import pandas as pd
import random

random.seed(42)

# --------------------------------------------------
# 1. Ticket templates for each priority
# --------------------------------------------------

priority_templates = {

    "Low": [
        "How can I change my email address?",
        "I want to update my phone number",
        "How do I change my account name?",
        "I want to update my profile information",
        "How can I change my account details?",
        "Can I update my personal information?",
        "How do I change my delivery address?",
        "Can I change the address on my account?",
        "How can I update my profile?",
        "I want to change my account settings",
        "How do I update my preferences?",
        "Can I change my notification settings?",
        "How can I update my communication preferences?",
        "Where can I change my account information?",
        "I need help updating my profile",
        "How do I change my username?",
        "Can I update my account details?",
        "I want to modify my profile",
        "How can I edit my account information?",
        "Where can I update my phone number?"
    ],

    "Medium": [
        "Where can I see my order status?",
        "Where is my package?",
        "My delivery is late",
        "The delivery is two days late",
        "When will my order arrive?",
        "My package has not arrived yet",
        "My order is delayed",
        "The tracking information has not updated",
        "Why is my delivery taking so long?",
        "My package is still in transit",
        "When will my package be delivered?",
        "My shipment has been delayed",
        "The courier has not delivered my order",
        "My order has not arrived yet",
        "Can you tell me where my package is?",
        "My delivery date has passed",
        "The tracking status has not changed",
        "My package is stuck in transit",
        "I am still waiting for my delivery",
        "My order is taking longer than expected"
    ],

    "High": [
        "My payment was deducted but the order failed",
        "I was charged twice for the same order",
        "Someone used my account without permission",
        "My account is completely locked",
        "I see an unauthorized transaction",
        "Someone accessed my account",
        "I cannot access my account after suspicious activity",
        "My card was charged but I did not make this purchase",
        "There is an unauthorized payment on my account",
        "Someone has accessed my account without my permission",
        "I noticed a payment that I did not make",
        "My account has been compromised",
        "I think someone has hacked my account",
        "There is suspicious activity on my account",
        "My money was taken without authorization",
        "I found an unknown transaction on my account",
        "My card was charged for a purchase I did not make",
        "Someone made a purchase using my account",
        "I believe my account has been hacked",
        "There is a fraudulent transaction on my account"
    ]
}


# --------------------------------------------------
# 2. Additional phrases
# --------------------------------------------------

prefixes = [
    "",
    "Please help me, ",
    "I need help because ",
    "Can you help me? ",
    "I am facing an issue where ",
    "I am having a problem because ",
    "Could you please help? ",
    "I need assistance because ",
    "Can someone help me? ",
    "I would like to know, "
]


suffixes = [
    "",
    " Please help.",
    " Can you check this?",
    " What should I do?",
    " Please look into this.",
    " I need assistance.",
    " Can you resolve this?",
    " Please help me with this issue.",
    " Can you help me?",
    " Please check this for me."
]


# --------------------------------------------------
# 3. Generate dataset
# --------------------------------------------------

data = []

TARGET_PER_PRIORITY = 500

for priority, templates in priority_templates.items():

    for _ in range(TARGET_PER_PRIORITY):

        # Choose a random base ticket
        base_ticket = random.choice(templates)

        # Choose random prefix and suffix
        prefix = random.choice(prefixes)
        suffix = random.choice(suffixes)

        # Combine everything
        ticket = f"{prefix} {base_ticket} {suffix}"

        # Remove extra spaces
        ticket = " ".join(ticket.split())

        data.append({
            "ticket": ticket,
            "priority": priority
        })


# --------------------------------------------------
# 4. Create DataFrame
# --------------------------------------------------

df = pd.DataFrame(data)


# --------------------------------------------------
# 5. Shuffle dataset
# --------------------------------------------------

df = df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)


# --------------------------------------------------
# 6. Remove duplicate tickets
# --------------------------------------------------

df = df.drop_duplicates(
    subset=["ticket"]
).reset_index(drop=True)


# --------------------------------------------------
# 7. Save dataset
# --------------------------------------------------

df.to_csv(
    "priority_tickets.csv",
    index=False
)


# --------------------------------------------------
# 8. Display information
# --------------------------------------------------

print("Priority dataset created successfully!")
print()

print("Number of tickets:", len(df))
print()

print("Priority distribution:")
print(df["priority"].value_counts())
print()

print("First 10 rows:")
print(df.head(10))