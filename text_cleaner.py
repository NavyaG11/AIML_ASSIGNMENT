import nltk
import string
from nltk.corpus import stopwords

# Download stopwords (run only first time)
nltk.download('stopwords')

# Sample messy sentences (you can replace with your 20 sentences)
sentences = [
    "Hey!!! How r u?? 😊",
    "This is sooo coool!!!",
    "I can't beleive this!!! 😡",
    "LOL 😂 that's funny!!!",
    "Visit www.example.com now!!!",
    "Hiiiii, what's up???",
    "Thiss is a typoooo sentence",
    "Good morning!!! 🌞",
    "OMG!!! This is amazingggg",
    "He is goood at coding!!!"
]

# Load stopwords
stop_words = set(stopwords.words('english'))

# Text cleaning function
def clean_text(text):
    # 1. Lowercase
    text = text.lower()
    
    # 2. Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # 3. Tokenization (split words)
    words = text.split()
    
    # 4. Remove stopwords
    words = [word for word in words if word not in stop_words]
    
    # Join back to sentence
    cleaned_text = " ".join(words)
    
    return cleaned_text

# Apply cleaning
print("---- Cleaned Sentences ----\n")
for i, sentence in enumerate(sentences):
    cleaned = clean_text(sentence)
    print(f"{i+1}. Original: {sentence}")
    print(f"   Cleaned: {cleaned}\n")