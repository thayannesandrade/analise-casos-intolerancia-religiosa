import tweepy
import json
from config.config import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

def authenticate():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth, wait_on_rate_limit=True)

def collect_tweets(query, max_tweets=1000):
    api = authenticate()
    tweets = []
    
    for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="pt", tweet_mode='extended').items(max_tweets):
        tweets.append(tweet._json)
    
    with open('data/raw_tweets.json', 'w') as f:
        json.dump(tweets, f, indent=4)
    
    print(f"Coletados {len(tweets)} tweets.")
    return tweets

if __name__ == "__main__":
    query = "#intoleranciareligiosa OR #racismoreligioso"
    collect_tweets(query)
