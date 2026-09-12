import pandas as pd
import random

random.seed(42)

negative = [
    # Account
    ("I cannot log into my account", "Negative"),
    ("My account has been locked and I cannot access it", "Negative"),
    ("Someone accessed my account without my permission", "Negative"),
    ("I cannot reset my password", "Negative"),
    ("My account keeps rejecting my correct password", "Negative"),
    ("I lost access to my account", "Negative"),
    ("Someone changed my account details without permission", "Negative"),
    ("My account login is not working", "Negative"),
    ("I am unable to access my profile", "Negative"),
    ("My account was blocked unexpectedly", "Negative"),

    # Payment
    ("My payment failed and my money was deducted", "Negative"),
    ("I was charged twice for the same purchase", "Negative"),
    ("Money was deducted but my order was not placed", "Negative"),
    ("My payment keeps getting declined", "Negative"),
    ("The payment failed even though I have enough money", "Negative"),
    ("I was charged the wrong amount", "Negative"),
    ("My card was charged but the payment failed", "Negative"),
    ("I cannot complete my payment", "Negative"),
    ("The payment page keeps failing", "Negative"),
    ("My transaction failed but I was still charged", "Negative"),

    # Delivery
    ("My package has been delayed for five days", "Negative"),
    ("My order still has not arrived", "Negative"),
    ("My delivery is much later than expected", "Negative"),
    ("My parcel has not arrived yet", "Negative"),
    ("The delivery is several days late", "Negative"),
    ("My package was supposed to arrive yesterday", "Negative"),
    ("My order has been stuck in transit", "Negative"),
    ("The delivery date keeps getting postponed", "Negative"),
    ("My package has been delayed again", "Negative"),
    ("I have been waiting too long for my delivery", "Negative"),

    # Refund
    ("My refund has not arrived yet", "Negative"),
    ("I have been waiting for my refund for several days", "Negative"),
    ("My refund is taking too long", "Negative"),
    ("I requested a refund but have not received it", "Negative"),
    ("My refund was promised but I still have not received it", "Negative"),
    ("The refund has not been credited to my account", "Negative"),
    ("I am still waiting for the money to be refunded", "Negative"),
    ("My refund request has been delayed", "Negative"),
    ("I have not received the refund for my cancelled order", "Negative"),
    ("The refund process is taking too long", "Negative"),

    # Order
    ("I received the wrong product", "Negative"),
    ("My product arrived damaged", "Negative"),
    ("The item I received is defective", "Negative"),
    ("My order is missing from my account", "Negative"),
    ("The product I received is not what I ordered", "Negative"),
    ("Part of my order was missing", "Negative"),
    ("The item arrived broken", "Negative"),
    ("My order was incorrect", "Negative"),
    ("I received a damaged product", "Negative"),
    ("The product quality was disappointing", "Negative"),

    # Cancellation
    ("I cancelled my order but I was still charged", "Negative"),
    ("My cancellation request was ignored", "Negative"),
    ("The order was not cancelled after I requested cancellation", "Negative"),
    ("I cancelled my subscription but was charged again", "Negative"),
    ("My order cancellation did not work", "Negative"),
    ("I was charged even though I cancelled the order", "Negative"),
    ("My cancellation request is still pending", "Negative"),
    ("The system would not let me cancel my order", "Negative"),
    ("My subscription cancellation failed", "Negative"),
    ("I cannot cancel my order", "Negative"),

    # Technical
    ("The website keeps crashing", "Negative"),
    ("The app keeps freezing", "Negative"),
    ("The checkout page is not working", "Negative"),
    ("The website stops responding during checkout", "Negative"),
    ("The payment page is not loading", "Negative"),
    ("The app crashes whenever I open it", "Negative"),
    ("I cannot complete checkout because the website is broken", "Negative"),
    ("The website keeps showing an error", "Negative"),
    ("The app is extremely slow and keeps freezing", "Negative"),
    ("The checkout process keeps failing", "Negative"),

    # Subscription
    ("I cannot access my premium subscription", "Negative"),
    ("My subscription stopped working", "Negative"),
    ("I was charged for a subscription I cancelled", "Negative"),
    ("My premium features are not available", "Negative"),
    ("My subscription payment failed unexpectedly", "Negative"),
    ("I paid for premium but cannot use it", "Negative"),
    ("My subscription benefits disappeared", "Negative"),
    ("The subscription is active but I cannot access it", "Negative"),
    ("I was charged twice for my subscription", "Negative"),
    ("My subscription was renewed without my permission", "Negative"),

    # General complaints
    ("I am very disappointed with the service", "Negative"),
    ("This service has been extremely frustrating", "Negative"),
    ("I am unhappy with how this was handled", "Negative"),
    ("This experience has been terrible", "Negative"),
    ("I am very dissatisfied with the service", "Negative"),
    ("My problem has still not been resolved", "Negative"),
    ("I have been waiting too long for support", "Negative"),
    ("This issue has caused me a lot of trouble", "Negative"),
    ("I am extremely frustrated with this problem", "Negative"),
    ("This is unacceptable", "Negative"),
    ("I am disappointed with my experience", "Negative"),
    ("The service has been very poor", "Negative"),
    ("I am unhappy with my purchase", "Negative"),
    ("The support response was not helpful", "Negative"),
    ("My issue keeps happening again", "Negative"),
    ("I expected much better service", "Negative"),
    ("This problem is still unresolved", "Negative"),
    ("I am frustrated with the repeated failures", "Negative"),
    ("The experience was very disappointing", "Negative"),
    ("I am not satisfied with the service", "Negative"),

    # More natural mixed cases
    ("My order arrived late and the product was damaged", "Negative"),
    ("My payment failed and I cannot place my order", "Negative"),
    ("My refund is late and support has not helped", "Negative"),
    ("I was charged twice and cannot get a refund", "Negative"),
    ("My package is missing and tracking has not updated", "Negative"),
    ("I cannot log in after changing my password", "Negative"),
    ("The app crashes whenever I try to make a payment", "Negative"),
    ("I was charged after cancelling my subscription", "Negative"),
    ("My order was cancelled but my money was not returned", "Negative"),
    ("The website keeps freezing when I try to order", "Negative"),
    ("My delivery is late and nobody can tell me why", "Negative"),
    ("I received the wrong item and need a replacement", "Negative"),
    ("My card was charged but my order failed", "Negative"),
    ("I cannot access the premium features I paid for", "Negative"),
    ("My account was accessed by someone else", "Negative"),
    ("I have waited several days for customer support", "Negative"),
    ("The refund for my cancelled order is still missing", "Negative"),
    ("The payment system keeps rejecting my card", "Negative"),
    ("My package arrived damaged and I am unhappy", "Negative"),
    ("The checkout system is completely unusable", "Negative"),
]


neutral = [
    # Account
    ("How can I change my email address?", "Neutral"),
    ("How do I update my phone number?", "Neutral"),
    ("How can I update my profile?", "Neutral"),
    ("How do I reset my password?", "Neutral"),
    ("How can I change my account details?", "Neutral"),
    ("How do I update my account information?", "Neutral"),
    ("Where can I edit my profile?", "Neutral"),
    ("How can I change my account name?", "Neutral"),
    ("Can I update my personal information?", "Neutral"),
    ("Where can I manage my account settings?", "Neutral"),

    # Payment
    ("How can I update my payment method?", "Neutral"),
    ("Where can I see my payment history?", "Neutral"),
    ("How can I view my transactions?", "Neutral"),
    ("What payment methods are available?", "Neutral"),
    ("How do payments work?", "Neutral"),
    ("Where can I find my billing information?", "Neutral"),
    ("How can I change my billing details?", "Neutral"),
    ("Can I use another payment method?", "Neutral"),
    ("Where can I check my previous payments?", "Neutral"),
    ("How can I view my transaction details?", "Neutral"),

    # Delivery
    ("Where can I track my package?", "Neutral"),
    ("How can I track my order?", "Neutral"),
    ("When should my package arrive?", "Neutral"),
    ("Can you tell me the delivery status?", "Neutral"),
    ("How long does delivery normally take?", "Neutral"),
    ("Where can I find my tracking information?", "Neutral"),
    ("How do I check whether my order was shipped?", "Neutral"),
    ("What are the available delivery options?", "Neutral"),
    ("Can I change the delivery address?", "Neutral"),
    ("Where can I see my delivery details?", "Neutral"),

    # Refund
    ("What is the refund policy?", "Neutral"),
    ("How long does a refund normally take?", "Neutral"),
    ("Where can I check my refund status?", "Neutral"),
    ("How do I request a refund?", "Neutral"),
    ("What are the conditions for a refund?", "Neutral"),
    ("How does the refund process work?", "Neutral"),
    ("Where can I find refund information?", "Neutral"),
    ("Can you explain the refund procedure?", "Neutral"),
    ("How can I check a refund request?", "Neutral"),
    ("What happens after I request a refund?", "Neutral"),

    # Order
    ("Where can I find my order details?", "Neutral"),
    ("How can I check my order status?", "Neutral"),
    ("Where can I see my previous orders?", "Neutral"),
    ("How do I place an order?", "Neutral"),
    ("Can I change my order details?", "Neutral"),
    ("How can I view my order history?", "Neutral"),
    ("Where can I find my order number?", "Neutral"),
    ("How do I return an item?", "Neutral"),
    ("What is the return process?", "Neutral"),
    ("Can I modify my order?", "Neutral"),

    # Cancellation
    ("How do I cancel my order?", "Neutral"),
    ("What is the cancellation process?", "Neutral"),
    ("Can I cancel an order before shipping?", "Neutral"),
    ("How can I cancel my subscription?", "Neutral"),
    ("Where can I find the cancellation option?", "Neutral"),
    ("What happens when I cancel an order?", "Neutral"),
    ("Can I cancel my purchase?", "Neutral"),
    ("How long does order cancellation take?", "Neutral"),
    ("What are the cancellation conditions?", "Neutral"),
    ("How can I stop an order before it ships?", "Neutral"),

    # Technical
    ("What should I do if the website is not loading?", "Neutral"),
    ("How can I troubleshoot the app?", "Neutral"),
    ("Where can I find technical support?", "Neutral"),
    ("How do I update the application?", "Neutral"),
    ("What are the system requirements?", "Neutral"),
    ("How can I clear the app cache?", "Neutral"),
    ("How do I report a technical problem?", "Neutral"),
    ("Where can I find troubleshooting instructions?", "Neutral"),
    ("How can I resolve a login problem?", "Neutral"),
    ("Can you provide technical support information?", "Neutral"),

    # Subscription
    ("How do I manage my subscription?", "Neutral"),
    ("Where can I check my subscription status?", "Neutral"),
    ("How can I upgrade my subscription?", "Neutral"),
    ("How do I change my subscription plan?", "Neutral"),
    ("What subscription plans are available?", "Neutral"),
    ("How can I renew my subscription?", "Neutral"),
    ("Where can I find my subscription details?", "Neutral"),
    ("How do I view my subscription history?", "Neutral"),
    ("What are the subscription options?", "Neutral"),
    ("How can I manage premium features?", "Neutral"),

    # General
    ("How can I contact customer support?", "Neutral"),
    ("Where can I find help?", "Neutral"),
    ("Can you provide information about my account?", "Neutral"),
    ("Where can I find the help center?", "Neutral"),
    ("How can I get assistance with an order?", "Neutral"),
    ("What support options are available?", "Neutral"),
    ("Where can I find customer service information?", "Neutral"),
    ("How can I contact the support team?", "Neutral"),
    ("Can you explain how the service works?", "Neutral"),
    ("Where can I find more information?", "Neutral"),

    # More natural examples
    ("I would like to know my order status", "Neutral"),
    ("I want to know when my package will arrive", "Neutral"),
    ("I need information about my refund", "Neutral"),
    ("I would like to know about the return policy", "Neutral"),
    ("I need help updating my profile", "Neutral"),
    ("I want to know how to change my email", "Neutral"),
    ("I need information about available payment methods", "Neutral"),
    ("I would like to check my subscription details", "Neutral"),
    ("I want to know how cancellation works", "Neutral"),
    ("I need information about delivery times", "Neutral"),
    ("I would like to check my transaction history", "Neutral"),
    ("I want to know how to track my package", "Neutral"),
    ("I need instructions for resetting my password", "Neutral"),
    ("I would like information about account settings", "Neutral"),
    ("I want to know how to return a product", "Neutral"),
    ("I need information about order changes", "Neutral"),
    ("I would like to know how refunds are processed", "Neutral"),
    ("I want to know what payment options are supported", "Neutral"),
    ("I need help understanding my subscription", "Neutral"),
    ("I would like information about customer support", "Neutral"),
]


positive = [
    # Account
    ("My account is working again", "Positive"),
    ("I can access my account now", "Positive"),
    ("The password reset worked perfectly", "Positive"),
    ("My account issue was resolved quickly", "Positive"),
    ("Thank you, I can log in again", "Positive"),
    ("My account is working perfectly now", "Positive"),
    ("The login problem was fixed", "Positive"),
    ("I successfully regained access to my account", "Positive"),
    ("My profile update worked successfully", "Positive"),
    ("Everything is fine with my account now", "Positive"),

    # Payment
    ("My payment was completed successfully", "Positive"),
    ("The payment went through successfully", "Positive"),
    ("My payment was processed without any problem", "Positive"),
    ("The payment issue was resolved quickly", "Positive"),
    ("My transaction was completed successfully", "Positive"),
    ("The payment worked perfectly", "Positive"),
    ("My card payment was successful", "Positive"),
    ("The payment was processed correctly", "Positive"),
    ("Everything went smoothly with my payment", "Positive"),
    ("I successfully completed my payment", "Positive"),

    # Delivery
    ("My package arrived on time", "Positive"),
    ("My order was delivered successfully", "Positive"),
    ("My package arrived earlier than expected", "Positive"),
    ("The delivery was fast and smooth", "Positive"),
    ("I received my order safely", "Positive"),
    ("My package arrived in perfect condition", "Positive"),
    ("The delivery went perfectly", "Positive"),
    ("My order arrived right on schedule", "Positive"),
    ("I received my package without any problems", "Positive"),
    ("The delivery experience was excellent", "Positive"),

    # Refund
    ("My refund was processed successfully", "Positive"),
    ("I received my refund successfully", "Positive"),
    ("The refund was completed quickly", "Positive"),
    ("My refund arrived without any problem", "Positive"),
    ("The refund process went smoothly", "Positive"),
    ("I received the money from my refund", "Positive"),
    ("My refund was handled quickly", "Positive"),
    ("The refund was credited successfully", "Positive"),
    ("Everything went smoothly with my refund", "Positive"),
    ("I am happy that my refund was completed", "Positive"),

    # Order
    ("My order arrived in perfect condition", "Positive"),
    ("I received exactly what I ordered", "Positive"),
    ("My purchase went smoothly", "Positive"),
    ("The product I received is excellent", "Positive"),
    ("I am very happy with my purchase", "Positive"),
    ("The order process was easy and smooth", "Positive"),
    ("My product arrived safely", "Positive"),
    ("Everything was perfect with my order", "Positive"),
    ("I am pleased with the product", "Positive"),
    ("The order was handled very well", "Positive"),

    # Cancellation
    ("My order was cancelled successfully", "Positive"),
    ("The cancellation was completed without any problem", "Positive"),
    ("My cancellation request was processed quickly", "Positive"),
    ("The order cancellation worked perfectly", "Positive"),
    ("I successfully cancelled my order", "Positive"),
    ("My subscription was cancelled successfully", "Positive"),
    ("The cancellation process was very easy", "Positive"),
    ("My cancellation request was handled quickly", "Positive"),
    ("Everything went smoothly with the cancellation", "Positive"),
    ("I am happy with how the cancellation was handled", "Positive"),

    # Technical
    ("The website is working properly again", "Positive"),
    ("The app is working smoothly now", "Positive"),
    ("The technical problem was fixed", "Positive"),
    ("The website issue was resolved quickly", "Positive"),
    ("The app is working perfectly now", "Positive"),
    ("The checkout problem was fixed", "Positive"),
    ("The website is running normally again", "Positive"),
    ("The technical issue has been completely resolved", "Positive"),
    ("Everything is working properly now", "Positive"),
    ("The application is working without any problems", "Positive"),

    # Subscription
    ("My subscription is working perfectly", "Positive"),
    ("I can access my premium features now", "Positive"),
    ("My subscription issue was resolved", "Positive"),
    ("The subscription was activated successfully", "Positive"),
    ("My premium access is working again", "Positive"),
    ("Everything is working with my subscription", "Positive"),
    ("My subscription payment was processed successfully", "Positive"),
    ("The subscription problem was fixed", "Positive"),
    ("I am happy with my subscription", "Positive"),
    ("My premium service is working perfectly", "Positive"),

    # Support / general
    ("The support team solved my problem", "Positive"),
    ("Customer support was very helpful", "Positive"),
    ("My issue was resolved quickly", "Positive"),
    ("The problem has been completely resolved", "Positive"),
    ("The support team provided excellent service", "Positive"),
    ("Thank you for solving my problem", "Positive"),
    ("Thank you for the quick support", "Positive"),
    ("I really appreciate the help", "Positive"),
    ("I am satisfied with the service", "Positive"),
    ("I am happy with how this was handled", "Positive"),
    ("The service was excellent", "Positive"),
    ("I had a great experience", "Positive"),
    ("I am pleased with the support", "Positive"),
    ("The problem was fixed without any trouble", "Positive"),
    ("Everything went smoothly", "Positive"),
    ("The issue was handled perfectly", "Positive"),
    ("I really appreciate the quick response", "Positive"),
    ("The support experience was excellent", "Positive"),
    ("I am very satisfied with the resolution", "Positive"),
    ("The service exceeded my expectations", "Positive"),
]


# ============================================================
# CREATE DATASET
# ============================================================

data = negative + neutral + positive

df = pd.DataFrame(
    data,
    columns=["ticket", "sentiment"]
)

# Remove exact duplicates
df = df.drop_duplicates(
    subset=["ticket", "sentiment"]
)

# Shuffle
df = df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)


# ============================================================
# CHECK DATASET
# ============================================================

print("Dataset created successfully!")
print("=" * 50)

print("Total rows:", len(df))

print("\nSentiment Distribution:")
print(df["sentiment"].value_counts())

print("\nDuplicate Rows:", df.duplicated().sum())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nExamples per sentiment:")

print("\nNEGATIVE:")
print(df[df["sentiment"] == "Negative"].head(5).to_string(index=False))

print("\nNEUTRAL:")
print(df[df["sentiment"] == "Neutral"].head(5).to_string(index=False))

print("\nPOSITIVE:")
print(df[df["sentiment"] == "Positive"].head(5).to_string(index=False))


# Save
df.to_csv(
    "./datasets/sentiment_tickets.csv",
    index=False
)

print("\nSaved as:")
print("./datasets/sentiment_tickets.csv")

