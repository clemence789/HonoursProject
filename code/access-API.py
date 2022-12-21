import tweepy
import logging
import json
import csv
import pandas
import time

print("hello")

#Authenticate with the API through tweepy (à voir)
keys = {
    'consumer_key': 'HM2L20WSoeiDOGuBpWMBhO35Y', 
    'consumer_secret': 'lQF726OQxRqvFoGfUFEBgPSrV4vH8phzRhrmMt2WbHfuVfX4c4', 
    'access_token': '1604068859706855424-yHTZzJEtlJJbCYiv21RwfxMPmhTRYI', 
    'access_token_secret': 'WMwVZ2V7I3sNEQqmISUVy3BrczkCMyfo6oLaDlO6VWRXO',
    'bearer_token': 'AAAAAAAAAAAAAAAAAAAAABI%2BkgEAAAAAXWj%2B%2Bf6FxPZ9fu9kE1wu0NPZiQM%3DauGTgGLIg4RuJ0rj54Z5I5vVFFHOOm7b4tu21dopElGbR6GhFK'
}

#Access to API using OAuth
auth = tweepy.OAuthHandler(keys['consumer_key'],
keys['consumer_secret'])
auth.set_access_token(keys['access_token'],
keys['access_token_secret'])

api = tweepy.API(auth)

#Enable logging to the console
logging.basicConfig(level=logging.DEBUG)

#Stream by language and keywords: the keywords are 10 of the most commonly used words on twitter so as to replicate live tweet collection without filter
keywords = ['the', 'i', 'to', 'a', 'and', 'is', 'in', 'it', 'you', 'new']

#Use the Stream class from tweepy to collect real-time tweets
class CollectTweets(tweepy.StreamingClient):
    def on_connect(self):
        print('connected')
    
    def on_tweet(self, tweet):
        if tweet.referenced_tweets == None and tweet.lang == "en":
            print(tweet.text) #this checks to see whether or not a tweet is a reply or not in english and discards it if it is
            
            time.sleep(0.5)


stream = CollectTweets(keys['bearer_token']) #Create instance of the class

for word in keywords:
    stream.add_rules(tweepy.StreamRule(word)) #Adds all the keywords as rules in the stream search, meaning that the tweets searched for must have one of the keywords

#Now actually stream and filter the tweets
stream.filter(tweet_fields=["referenced_tweets", "lang"])