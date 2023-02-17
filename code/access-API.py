import tweepy
import csv
from datetime import datetime

#Authenticate with the API through tweepy
keys = {
    'bearer_token': 'AAAAAAAAAAAAAAAAAAAAABI%2BkgEAAAAAXWj%2B%2Bf6FxPZ9fu9kE1wu0NPZiQM%3DauGTgGLIg4RuJ0rj54Z5I5vVFFHOOm7b4tu21dopElGbR6GhFK'
}

#Access to API using OAuth
client = tweepy.Client(bearer_token = keys['bearer_token'], wait_on_rate_limit = True)

#max results per page, number between 10 and 100
max_results = 100

paginator = tweepy.Paginator(client.search_recent_tweets, 
        query = "angry OR disgusted OR worst OR hate OR detest -is:retweet lang:en",
        max_results = 100, 
        tweet_fields = ['id','created_at','text', 'lang'], limit = 900)

for page in paginator:

    #initialise array that will store tweets
    data = []

    #Format the date and time should be in
    time_format = "%A %B %d %H:%M:%S %Y" 

    for i in page.data:
        in_tweet = []
        in_tweet.append(str(i.id))#tweet id
        times = datetime.strftime(i.created_at, time_format)#format date and time
        in_tweet.append(str(times))#date and time
        in_tweet.append(str(i.text))#text tweet
        data.append(in_tweet)#add to nested array

    #write to csv
    with open(r'code\dataset.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        #rows
        writer.writerows(data)

#use paginator to collect 170000 tweets
paginator = tweepy.Paginator(client.search_recent_tweets, 
        query = "happy OR joy OR love OR great OR amazing OR positive OR wonderful -is:retweet lang:en",
        max_results = 100, #max results per page
        tweet_fields = ['id','created_at','text', 'lang'], limit = 900)

#format every tweet collected and add to csv dataset
for page in paginator:
    #initialise array that will store tweets
    data = []

    #Format the date and time should be in
    time_format = "%A %B %d %H:%M:%S %Y" 

    for i in page.data:
        in_tweet = []
        in_tweet.append(str(i.id))#tweet id
        times = datetime.strftime(i.created_at, time_format)#format date and time
        in_tweet.append(str(times))#date and time
        in_tweet.append(str(i.text))#text tweet
        data.append(in_tweet)#add to nested array
    
    print(data)

    #write to csv
    with open(r'code\dataset.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        #rows
        writer.writerows(data)