from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to get stars and scores
def vader_to_stars(review):
    scores = analyzer.polarity_scores(review)
    compound = scores['compound']
    if compound <= -0.6: # 0.6
        stars = 1
    elif compound <= -0.4: # 0.4
        stars = 2
    elif compound <= 0.0: #0.0
        stars = 3
    elif compound <= 0.7: #0.7
        stars = 4
    else:
        stars = 5
    return stars, scores