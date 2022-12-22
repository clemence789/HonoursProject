import tweepy
import logging
import json
import csv
import pandas
import time
import datetime
import dateutil.parser
import unicodedata

print("hello")

#Authenticate with the API through tweepy
keys = {
    'consumer_key': 'HM2L20WSoeiDOGuBpWMBhO35Y', 
    'consumer_secret': 'lQF726OQxRqvFoGfUFEBgPSrV4vH8phzRhrmMt2WbHfuVfX4c4', 
    'access_token': '1604068859706855424-yHTZzJEtlJJbCYiv21RwfxMPmhTRYI', 
    'access_token_secret': 'WMwVZ2V7I3sNEQqmISUVy3BrczkCMyfo6oLaDlO6VWRXO',
    'bearer_token': 'AAAAAAAAAAAAAAAAAAAAABI%2BkgEAAAAAXWj%2B%2Bf6FxPZ9fu9kE1wu0NPZiQM%3DauGTgGLIg4RuJ0rj54Z5I5vVFFHOOm7b4tu21dopElGbR6GhFK'
}

#Access to API using OAuth
client = tweepy.Client(bearer_token = keys['bearer_token'], wait_on_rate_limit = True)

tweets = client.search_recent_tweets(
    "happy OR upset OR i -is:retweet lang:en",
    max_results = 10,
    tweet_fields = [],
    user_fields = []
)
print(tweets)

