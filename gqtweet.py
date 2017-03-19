import tweepy
import os, json, random
from gqtr import get_quotes

url = 'https://goodreads.com/quotes/tag/'
current_dir = os.path.dirname(os.path.abspath(__file__))

try:
    with open(current_dir+ '/' + 'config.local.json') as f:
        config = json.load(f)
except FileNotFoundError:
    with open(current_dir + '/' + 'config.json') as f:
        config = json.load(f)


consumer_key= config["consumer_key"]
consumer_secret=config["consumer_secret"]
access_token=config["access_token"]
access_token_secret= config["access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print("logged in as:",api.me().name)

if __name__ == '__main__':
    
    tags = ['inspirational', "motivational", "abstract"]
    quotes = get_quotes(url, tags[random.randint(0, len(tags))], 200)
    selected_tweets = []
    for quote in quotes:
        if len(quote) <= 140:
            selected_tweets.append(quote)
    api.update_status(status=selected_tweets[random.randint(0, len(selected_tweets))])
