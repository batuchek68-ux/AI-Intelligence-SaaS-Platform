from collections import Counter
import re

STOPWORDS = {
    "the","is","and","to","of","in","for","on","a","an"
}

def clean(text):
    text = text.lower()
    text = re.sub(r"[^a-z ]", "", text)
    return text

def analyze_trends(news):

    words = []

    for item in news:
        words += clean(item["title"]).split()

    words = [
        w for w in words
        if w not in STOPWORDS and len(w) > 2
    ]

    return Counter(words).most_common(10)
