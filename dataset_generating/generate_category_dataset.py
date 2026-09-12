# import pandas as pd
# import random

# random.seed(42)

# # Ticket templates for each category

# ticket_templates = {

#     "Payment Issue": [
#         "My payment failed while placing the order",
#         "I was charged twice for the same transaction",
#         "My payment was deducted but the order was not placed",
#         "The payment keeps getting declined",
#         "I was charged but my order still shows as unpaid",
#         "Why did my card payment fail?",
#         "The money was deducted from my account but the payment failed",
#         "I cannot complete my payment",
#         "My transaction failed",
#         "The payment gateway is not working",
#         "I was charged twice for one order",
#         "My UPI payment failed",
#         "The payment was successful but the order was cancelled",
#         "I made a payment but it is still showing as pending",
#         "Why is my payment pending?"
#     ],

#     "Delivery Issue": [
#         "Where is my package?",
#         "My order has not arrived yet",
#         "My delivery is late",
#         "When will my package be delivered?",
#         "The delivery date has passed",
#         "My order is still in transit",
#         "The courier has not delivered my package",
#         "My package is delayed",
#         "I have been waiting for my order",
#         "The tracking information has not updated",
#         "Why is my delivery taking so long?",
#         "My package has not been delivered",
#         "The delivery is taking longer than expected",
#         "Can you tell me where my package is?",
#         "My shipment is stuck in transit"
#     ],

#     "Refund": [
#         "I want a refund",
#         "How can I request a refund?",
#         "Please refund my order",
#         "When will I receive my refund?",
#         "My refund has not arrived",
#         "I have been waiting for my refund",
#         "Why is my refund delayed?",
#         "I need my money back",
#         "Can I get a refund for this order?",
#         "The refund was approved but I have not received it",
#         "My money has not been refunded",
#         "How long does a refund take?",
#         "I want to return the payment and get a refund",
#         "Please process my refund",
#         "Where is my refund?"
#     ],

#     "Cancellation": [
#         "I want to cancel my order",
#         "Please cancel my purchase",
#         "How can I cancel my order?",
#         "I need to cancel an order",
#         "Can you cancel my order?",
#         "I no longer want this order",
#         "Please stop my order",
#         "I want to cancel the purchase",
#         "Can I cancel my order?",
#         "I placed the order by mistake",
#         "I want to cancel before it is shipped",
#         "Please cancel this transaction",
#         "How do I cancel a purchase?",
#         "Cancel my recent order",
#         "I changed my mind and want to cancel"
#     ],

#     "Account Issue": [
#         "I forgot my password",
#         "How can I reset my password?",
#         "I cannot log into my account",
#         "My account is locked",
#         "I cannot access my account",
#         "How do I change my email address?",
#         "I want to update my account information",
#         "My password is not working",
#         "I forgot my login details",
#         "I am unable to sign in",
#         "How can I change my password?",
#         "My account login is not working",
#         "I cannot remember my password",
#         "How do I update my phone number?",
#         "I am having trouble accessing my account"
#     ],

#     "Technical Issue": [
#         "The website is not working",
#         "The app keeps crashing",
#         "I cannot open the application",
#         "The website is showing an error",
#         "The app is very slow",
#         "I am getting an error message",
#         "The checkout page is not loading",
#         "The application stopped working",
#         "I cannot use the website",
#         "The page keeps freezing",
#         "The app crashes whenever I open it",
#         "There is a technical problem",
#         "The website keeps showing an error",
#         "The application is not responding",
#         "I am unable to use the checkout page"
#     ],

#     "Subscription": [
#         "I want to cancel my subscription",
#         "How can I upgrade my subscription?",
#         "I want to change my subscription plan",
#         "My subscription was renewed automatically",
#         "Why was I charged for my subscription?",
#         "How do I renew my subscription?",
#         "I want to upgrade my plan",
#         "Can I change my subscription?",
#         "My subscription payment failed",
#         "How can I stop automatic renewal?",
#         "I want to downgrade my plan",
#         "When does my subscription expire?",
#         "I was charged for a subscription I cancelled",
#         "How can I manage my subscription?",
#         "I need help with my subscription"
#     ],

#     "Order Issue": [
#         "My order is showing the wrong item",
#         "I received the wrong product",
#         "My order contains a damaged item",
#         "The product I received is different from what I ordered",
#         "One item is missing from my order",
#         "My order is incomplete",
#         "I received a damaged product",
#         "The wrong product was delivered",
#         "There is an item missing from my package",
#         "My order details are incorrect",
#         "I received the wrong size",
#         "The product I received is damaged",
#         "Something is missing from my order",
#         "My order contains the wrong product",
#         "The item I received is not what I purchased"
#     ]
# }

# # Additional phrases

# prefixes = [
#     "",
#     "Please help me, ",
#     "I need help because ",
#     "Can you help me? ",
#     "I am facing an issue where ",
#     "I am having a problem because ",
#     "Could you please help? ",
#     "I need assistance because "
# ]

# suffixes = [
#     "",
#     " Please help.",
#     " Can you check this?",
#     " What should I do?",
#     " Please look into this.",
#     " I need assistance.",
#     " Can you resolve this?",
#     " Please help me with this issue."
# ]


# # --------------------------------------------------
# # 3. Generate dataset
# # --------------------------------------------------

# data = []

# TARGET_PER_CATEGORY = 700

# for category, templates in ticket_templates.items():
#     for _ in range(TARGET_PER_CATEGORY):
#         base_ticket = random.choice(templates).strip()
#         prefix = random.choice(prefixes).strip()
#         suffix = random.choice(suffixes).strip()

#         # Combine parts safely with spaces
#         ticket_parts = [prefix, base_ticket, suffix]
#         ticket = " ".join(
#             part for part in ticket_parts if part
#         )

#         # Remove accidental multiple spaces
#         ticket = " ".join(ticket.split())
#         data.append({
#             "ticket": ticket,
#             "category": category
#         })
# df = pd.DataFrame(data)

# # --------------------------------------------------
# # 4. Shuffle and remove duplicates
# # --------------------------------------------------

# df = df.sample(
#     frac=1,
#     random_state=42
# ).reset_index(drop=True)

# df = df.drop_duplicates(subset=["ticket"])

# # --------------------------------------------------
# # 5. Save dataset
# # --------------------------------------------------

# df.to_csv("category_tickets.csv", index=False)

# print("Dataset created successfully!")
# print()

# print("Number of tickets:", len(df))
# print()

# print("Categories:")
# print(df["category"].value_counts())
# print()

# print("First 10 rows:")
# print(df.head(10))





import pandas as pd

df = pd.read_csv("./datasets/category_tickets.csv")

new_delivery = [
    "Where is my order?",
    "Where is my package?",
    "My order has not arrived yet",
    "My package has not arrived yet",
    "When will my order arrive?",
    "When will my package arrive?",
    "When can I expect my delivery?",
    "My delivery is late",
    "My order is late",
    "My package is delayed",
    "My delivery was supposed to arrive yesterday",
    "My order was supposed to arrive yesterday",
    "The delivery date has passed",
    "My package was supposed to arrive but it hasn't",
    "I have not received my package",
    "I have not received my order",
    "My order is still in transit",
    "My package is still in transit",
    "The tracking information has not updated",
    "My package tracking has not changed",
    "Can you tell me where my order is?",
    "Can you check the status of my package?",
    "I want to track my order",
    "I want to know when my package will arrive",
    "My package is taking too long to arrive",
    "Why has my order not arrived?",
    "Why is my package delayed?",
    "Why is my delivery taking so long?",
    "My expected delivery date has passed",
    "My order has been delayed"
]

new_df = pd.DataFrame({
    "ticket": new_delivery,
    "category": "Delivery Issue"
})

# Create clean_ticket column
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

new_df["clean_ticket"] = new_df["ticket"].apply(clean_text)

# Add new examples
df = pd.concat([df, new_df], ignore_index=True)

# Remove exact duplicates
df = df.drop_duplicates(subset=["ticket"]).reset_index(drop=True)

# Save improved dataset
df.to_csv("./datasets/category_tickets_improved.csv", index=False)

print("Original rows:", len(df) - len(new_delivery))
print("New rows:", len(df))
print("\nCategory distribution:")
print(df["category"].value_counts())