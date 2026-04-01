from textblob import TextBlob

reviews = [
    "The movie was amazing and full of excitement!",
    "I really hated the film, it was boring.",
    "It was okay, not the best but not the worst.",
    "Absolutely fantastic acting and great story!",
    "Terrible plot and bad direction."
]

for review in reviews:
    blob = TextBlob(review)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    print(f"\nReview: {review}")
    print(f"Sentiment: {sentiment} (Score: {polarity})")