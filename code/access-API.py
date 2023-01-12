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

#initialise iteration to get the amount of tweets needed
iteration = 0

#collect negative tweets
while iteration < 4:
    #get tweets based on keywords, in english and without retweets
    tweets = client.search_recent_tweets(
        "angry OR disgusted OR worst OR hate OR detest -is:retweet lang:en",
        max_results = max_results, 
        expansions=['author_id'], #expansions allows to get the username in 'user_fields'
        tweet_fields = ['id','created_at','text', 'lang'],
        user_fields = ['username']
        )

    #initialise array that will store tweets
    data = []

    #Format the date and time should be in
    time_format = "%A %B %d %H:%M:%S %Y" 
    
    #add necessary information from tweets to in_tweet array
    for i in tweets.data:
        in_tweet = []
        in_tweet.append(str(i.id))#tweet id
        times = datetime.strftime(i.created_at, time_format)#format date and time
        in_tweet.append(str(times))#date and time
        in_tweet.append(str(i.text))#text tweet
        data.append(in_tweet)#add to nested array
    
    len1 = len(tweets.data)
    len2 = len(tweets.includes['users'])

    #Equalize the number of tweets and users collected
    if len1 != len2:
        difference = len1 - len2
        j = 0
        while j < difference:
            tweets.includes['users'].append('')
            j+=1
    
    print('Tweets collected: ' + str(len(tweets.data)))

    i = 0
    #add the usernames to array of tweets
    while i < len(tweets.data):
        data[i].insert(2, str(tweets.includes['users'][i]))
        i+=1

    #write to csv
    with open(r'code\dataset.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        #rows
        writer.writerows(data)

        iteration+=1

#repeat to collect positive tweets
iteration = 0
while iteration < 4:
    tweets = client.search_recent_tweets(
        "happy OR joy OR love OR great OR amazing OR positive OR wonderful -is:retweet lang:en",
        max_results = max_results, #max results received, has to be number between 10 and 100
        expansions=['author_id'], #expansions allows to get the username in 'user_fields'
        tweet_fields = ['id','created_at','text', 'lang'],
        user_fields = ['username']
        )

    data = []
    time_format = "%A %B %d %H:%M:%S %Y" #Format the date and time should be in
    for i in tweets.data:
        in_tweet = []
        in_tweet.append(str(i.id))
        times = datetime.strftime(i.created_at, time_format)
        in_tweet.append(str(times))
        in_tweet.append(str(i.text))
        data.append(in_tweet)
    
    len1 = len(tweets.data)
    len2 = len(tweets.includes['users'])

    #Equalize the number of tweets and users collected
    if len1 != len2:
        difference = len1 - len2
        j = 0
        while j < difference:
            tweets.includes['users'].append('')
            j+=1
    
    print('Tweets collected: ' + str(len(tweets.data)))

    i = 0
    while i < len(tweets.data):
        data[i].insert(2, str(tweets.includes['users'][i]))
        i+=1

    #write to csv
    with open(r'code\dataset.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        #rows
        writer.writerows(data)

        iteration+=1