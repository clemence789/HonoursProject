import tweepy
import csv
from datetime import datetime

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

max_results = 100
iteration = 0
while iteration < 4:
    tweets = client.search_recent_tweets(
        "happy OR upset OR angry OR fun OR disgusted OR best OR the -is:retweet lang:en",
        max_results = max_results,
        expansions=['author_id'],
        tweet_fields = ['id','created_at','text', 'lang'],
        user_fields = ['username']
        )

    data = []
    time_format = "%A %B %d %H:%M:%S %Y"
    for i in tweets.data:
        in_tweet = []
        in_tweet.append(str(i.id))
        times = times = datetime.strftime(i.created_at, time_format)
        in_tweet.append(str(times))
        in_tweet.append(str(i.text))
        data.append(in_tweet)

    print(len(tweets.data))

    i = 0
    while i < len(tweets.data)-1:
        data[i].insert(2, str(tweets.includes['users'][i]))
        i+=1

    #write to csv
    with open(r'C:\Users\cleme\Documents\1HonoursProject\code\dataset.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        #rows
        writer.writerows(data)

        iteration+=1