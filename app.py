from flask import Flask, render_template
from textblob import TextBlob

app = Flask(__name__)

# Sample Amazon reviews
reviews = [
    "This product is amazing! Highly recommend it.",
    "Terrible quality, broke after one use.",
    "Good value for money.",
    "I am not happy with this purchase.",
    "Exceeded my expectations!",
]

# Function to get sentiment polarity
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

@app.route('/')
def home():
    review_sentiments = []
    for review in reviews:
        sentiment = get_sentiment(review)
        review_sentiments.append({"text": review, "sentiment": sentiment})
    return render_template('index.html', review_sentiments=review_sentiments)

if __name__ == '__main__':
    app.run(debug=True)
