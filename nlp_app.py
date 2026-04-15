# Simple Keyword Extractor using Python

from collections import Counter
import re

def extract_keywords(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    words = re.findall(r'\b[a-z]+\b', text)

    # Remove common stopwords
    stopwords = {"the", "is", "in", "and", "to", "of", "a", "on", "for", "with", "as", "by", "an"}
    filtered_words = [word for word in words if word not in stopwords]

    # Count frequency
    word_count = Counter(filtered_words)

    # Get top 5 keywords
    keywords = word_count.most_common(5)

    return keywords


# Input text
text = input("Enter a paragraph:\n")

keywords = extract_keywords(text)

print("\nTop Keywords:")
for word, count in keywords:
    print(word, ":", count)