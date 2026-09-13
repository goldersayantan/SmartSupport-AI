import pickle
import re

with open("./models/category_model.pkl", "rb") as file:
    category_model = pickle.load(file)

with open("./models/category_tfidf_vectorizer.pkl", "rb") as file:
    category_tfidf = pickle.load(file)

with open("./models/priority_model.pkl", "rb") as file:
    priority_model = pickle.load(file)

with open("./models/priority_tfidf_vectorizer.pkl", "rb") as file:
    priority_tfidf = pickle.load(file)

with open("./models/sentiment_model.pkl", "rb") as file:
    sentiment_model = pickle.load(file)

with open("./models/sentiment_tfidf_vectorizer.pkl", "rb") as file:
    sentiment_tfidf = pickle.load(file)

with open("./models/resolution_model.pkl", "rb") as file:
    resolution_model = pickle.load(file)

with open("./models/resolution_tfidf_vectorizer.pkl", "rb") as file:
    resolution_tfidf = pickle.load(file)

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def predict_ticket(ticket):
    cleaned_ticket = clean_text(ticket)

    category_input = category_tfidf.transform([cleaned_ticket])
    category_prediction = category_model.predict(category_input)[0]

    priority_input = priority_tfidf.transform([cleaned_ticket])
    priority_prediction = priority_model.predict(priority_input)[0]

    sentiment_input = sentiment_tfidf.transform([cleaned_ticket])
    sentiment_prediction = sentiment_model.predict(sentiment_input)[0]

    resolution_input = resolution_tfidf.transform([cleaned_ticket])
    resolution_prediction = resolution_model.predict(resolution_input)[0]

    return {
        "category": category_prediction,
        "priority": priority_prediction,
        "sentiment": sentiment_prediction,
        "resolution_time_hours": round(resolution_prediction, 2)
    }

tickets = [
    "I cannot log into my account because I forgot my password",
    "I need to change the email address associated with my account",
    "Someone accessed my account without my permission",
    "My package has been delayed for five days",
    "Where is my order? It was supposed to arrive yesterday",
    "My package arrived damaged",
    "I was charged twice for the same purchase",
    "My payment failed but the money was deducted from my bank account",
    "There is a transaction on my card that I do not recognize",
    "I want a refund for the product I purchased",
    "I requested a refund several days ago but have not received it",
    "I want to cancel my order before it is shipped",
    "I accidentally placed the wrong order and need to cancel it",
    "The website keeps crashing whenever I try to checkout",
    "The payment page is not loading",
    "I cannot access my premium subscription",
    "I was charged for my subscription even though I cancelled it",
    "My entire order is missing from my account",
    "I received the wrong product",
    "I need to update my delivery address"
    "My payment failed but money was deducted from my bank account",
    "My package has been delayed for three days",
    "How can I change my email address?",
    "Someone used my account and I cannot log in",
    "I received my refund successfully",
    "The website keeps crashing",
    "I want to cancel my order"
]

print("=" * 70)
print("                    SMARTSUPPORT AI")
print("=" * 70)

for ticket in tickets:

    result = predict_ticket(ticket)

    print("\nTicket:")
    print(ticket)

    print("\nPredictions:")
    print("-" * 70)
    print(f"Category        : {result['category']}")
    print(f"Priority        : {result['priority']}")
    print(f"Sentiment       : {result['sentiment']}")
    print(f"Resolution Time : {result['resolution_time_hours']} hours")
    print("-" * 70)