import tweepy
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
client = tweepy.Client(bearer_token = keys['bearer_token'], wait_on_rate_limit = True, return_type=dict)

tweets = client.search_recent_tweets(
    "happy OR upset OR angry OR fun OR disgusted OR best -is:retweet lang:en",
    max_results = 10,
    tweet_fields = ['id','created_at','text'],
    user_fields = ['username'])

tweets_data = tweets['data']

df = pandas.DataFrame.from_dict(tweets_data)

df.to_csv(r'C:\Users\cleme\Documents\1HonoursProject\code\dataset.csv', index = True, header = True)
print(df)

#print(tweets)
#print(tweets['data'])

#json_data = [r._json for r in tweets]
#df = pandas.json_normalize(tweets)

#print(df)

#tweets_df = pandas.DataFrame(tweets[i] for i in range(len(tweets)))

#FILE_PATH = r"C:\Users\cleme\Documents\1HonoursProject\code\dataset.csv"

#tweets_df.to_csv(FILE_PATH)

#columns = ['Tweet ID', 'Date', 'User', 'Text']
#dataframe = pandas.DataFrame(tweets)

#print(dataframe)
#print(tweets)

#tweets_data = tweets_dataset['data']

#df = pandas.json_normalize(tweets_data)

#print(df)