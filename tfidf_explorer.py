from sklearn.feature_extraction.text import TfidfVectorizer

# 5 sample documents
documents = [
    "AI is transforming the world with automation",
    "Machine learning and AI are closely related fields",
    "Natural language processing helps computers understand text",
    "Deep learning is a subset of machine learning",
    "AI applications include chatbots and recommendation systems"
]

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

feature_names = vectorizer.get_feature_names_out()

# Get top words per document
for i, doc in enumerate(X):
    print(f"\nDocument {i+1} Top Words:")
    scores = zip(feature_names, doc.toarray()[0])
    sorted_words = sorted(scores, key=lambda x: x[1], reverse=True)[:5]
    
    for word, score in sorted_words:
        print(f"{word}: {score:.3f}")