import random
from textblob import TextBlob
from compliment_bank import positive_compliments, neutral_compliments, negative_compliments

def detect_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.3:
        return 'positive'
    elif polarity < -0.1:
        return 'negative'
    else:
        return 'neutral'
    
def sweet_sentiment_compliment(user_input, override_sentiment=None):
    """
    Returns a single compliment based on sentiment or emoji mood slider.
    :param user_input: User input string
    :param override_sentiment: float (-1.0 to 1.0) or string override
    :return: Single compliment string
    """
    user_input = user_input.strip()
    if not user_input:
        return 'You need no compliments? Humble and amazing I see!'
    
    # Determine sentiment
    if isinstance(override_sentiment, float):
        if override_sentiment > 0.3:
            sentiment = 'positive'
        elif override_sentiment < -0.1:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
    else:
        sentiment = detect_sentiment(user_input)

    # Select compliment list based on sentiment
    if sentiment == 'positive':
        compliment_list = positive_compliments
    elif sentiment == 'negative':
        compliment_list = negative_compliments
    else:
        compliment_list = neutral_compliments

    # Pick and return a random compliment
    compliment = random.choice(compliment_list)
    return compliment
