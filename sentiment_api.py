from flask import Flask, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    review_text = data.get('review', '')
    
    score = analyzer.polarity_scores(review_text)
    
    sentiment = 'neutral'
    if score['compound'] >= 0.05:
        sentiment = 'positive'
    elif score['compound'] <= -0.05:
        sentiment = 'negative'

    return jsonify({
        'sentiment': sentiment,
        'compound': score['compound']
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)
