import json
import pandas as pd
import re

def clean_tweet(tweet):
    tweet = re.sub(r"http\S+|www\S+|https\S+", '', tweet, flags=re.MULTILINE)
    tweet = re.sub(r'\@\w+|\#', '', tweet)
    tweet = tweet.lower()
    tweet = re.sub(r'\s+', ' ', tweet)
    return tweet

def preprocess_tweets(input_file, output_file):
    with open(input_file, 'r') as f:
        tweets = json.load(f)
    
    data = []
    for tweet in tweets:
        text = tweet['full_text']
        clean_text = clean_tweet(text)
        data.append({
            'id': tweet['id_str'],
            'text': clean_text,
            'user': tweet['user']['screen_name'],
            'created_at': tweet['created_at'],
            'location': tweet['user']['location']
        })
    
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    print(f"Processados {len(df)} tweets.")

if __name__ == "__main__":
    preprocess_tweets('data/raw_tweets.json', 'data/twetts_processados.csv')
