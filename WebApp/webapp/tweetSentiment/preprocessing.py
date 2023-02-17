import tweepy
import emoji
import re
from tweetSentiment import dictionaries
import string
import nltk
from nltk.tokenize import word_tokenize
import spacy

#Collect tweets from keyword
def collectTweetsKeywords(keywords, numberTweets):
    #clean input data
    
    #turn all text to lower case
    keywords = keywords.lower()

    #replace comma with space
    keywords = keywords.replace(',', ' ')

    #Remove punctuation
    keywords = keywords.translate(str.maketrans('', '', string.punctuation))
    
    #get request string based on entered keywords
    keywords = str(keywords + ' -is:retweet lang:en')
    
    #remove brackets from number input
    numberTweets = numberTweets.replace("[", "")
    numberTweets = numberTweets.replace("]", "")
    numberTweets = int(numberTweets)

    #Access to API using OAuth
    client = tweepy.Client(bearer_token = 'AAAAAAAAAAAAAAAAAAAAABI%2BkgEAAAAAXWj%2B%2Bf6FxPZ9fu9kE1wu0NPZiQM%3DauGTgGLIg4RuJ0rj54Z5I5vVFFHOOm7b4tu21dopElGbR6GhFK', wait_on_rate_limit = True)
    
    #get tweets based on keywords, in english and without retweets
    tweets = client.search_recent_tweets(
        keywords,
        max_results = numberTweets, #max results received, has to be number between 10 and 100
        tweet_fields = ['text']
        )

    #initialise array that will store tweets    
    data = []

    #add necessary information from tweets to in_tweet array
    for i in tweets.data:
        in_tweet = []
        in_tweet.append(str(i.text))
        data.append(in_tweet)
          
    print('Tweets collected: ' + str(len(tweets.data)))

    return(data) #return tweets
        

#Collect tweets from username
def collectTweetsUsername(username, numberTweets):

    user = str(username)

    #remove brackets from number input
    numberTweets = numberTweets.replace("[", "")
    numberTweets = numberTweets.replace("]", "")
    numberTweets = int(numberTweets)

    client = tweepy.Client(bearer_token = 'AAAAAAAAAAAAAAAAAAAAABI%2BkgEAAAAAXWj%2B%2Bf6FxPZ9fu9kE1wu0NPZiQM%3DauGTgGLIg4RuJ0rj54Z5I5vVFFHOOm7b4tu21dopElGbR6GhFK', wait_on_rate_limit = True)
    
    #get user id based on username
    user = client.get_user(username = user)
    username = user.data['id']

    #returns dictionary so need to extract user id from it
    tweets = client.get_users_tweets(
        username,
        max_results = numberTweets,
        tweet_fields = ['text']
        )

    #add necessary information from tweets to in_tweet array
    data = []
    for i in tweets.data:
        in_tweet = []
        in_tweet.append(str(i.text))
        data.append(in_tweet)
    
    return(data) #return tweets


#pre-process tweets
def cleanTweets(tweets):

    cleanTweets = []
    
    #pre-process every tweet in the tweets array
    for i in tweets:
        
        #replace emojis in text if the text value is not NaN
        def emoji_to_text(text):
            if type(text) != float:
                return emoji.demojize(text)
            else:
                return text
        
        i = emoji_to_text(i)

        #remove URLs
        i = re.sub(r'http\S+', '', i)

        #Remove tags
        i = re.sub(r'[@]\w+', '', i)

        #turn all text to lower case
        i = i.lower()

        #expand contractions
        i = i.replace("’", "'") #replace instances of different apostrophe so they are recognized by the contraction dictionary
        def expand_contractions(text):
            return(re.sub(r"\b(\w+('\w+))\b", lambda x: dictionaries.CONTRACTIONS.get(x.group(1), x.group(1)), text)) #change regex from expanding acronyms to handle apostrophe
        i = expand_contractions(i)

        #remove stopwords
        #def remove_stopwords(tweet):
        #    return(re.sub(r"\b(\w+)\b", lambda x: dictionaries.STOPWORDS.get(x.group(1), x.group(1)), tweet))
        #i = remove_stopwords(i)

        #Remove punctuation
        i = re.sub(r'[^\w\s]+', ' ', i)
        i = re.sub('_', ' ', i)
        i = re.sub(r'\n', '', i)
        i = re.sub(r'[^\u0000-\u05C0\u2100-\u214F]+', '', i)
        i = re.sub('  ', ' ', i)

        #Remove numbers
        i = re.sub('\d+', '', i)

        #Remove duplicate letters
        i = re.sub(r'(\w)\1{2,}', r'\1', i)

        #Expand Acronyms using acronym dictionary
        def acronym_to_word(text):
            return(re.sub(r"\b(\w+)\b", lambda x: dictionaries.ACRONYM_TRANSLATE.get(x.group(1), x.group(1)), text))

        i = acronym_to_word(i)

        #remove double spaces
        i = re.sub('  ', ' ', i)
        cleanTweets.append(i)
    
    return(cleanTweets) #return pre-processed tweets

def tagTweets(tweets):

    nlp = spacy.load('en_core_web_sm') #loading the spacy engine
    def getSubjectPhrase(tweets):
        for token in tweets:
            if("subj" in token.dep_):
                subtree = list(token.subtree)
                start = subtree[0].i
                end = subtree[-1].i + 1
                return tweets[start:end]
    
    def getObjectPhrase(tweets):
        for token in tweets:
            if("dobj" in token.dep_):
                subtree = list(token.subtree)
                start = subtree[0].i
                end = subtree[-1].i + 1
                return tweets[start:end]
    tags = []
    for tweet in tweets:
        subjects = []
        tweet = nlp(tweet)
        subject_phrase = str(getSubjectPhrase(tweet))
        object_phrase = str(getObjectPhrase(tweet))

        subjects.append(object_phrase)
        subjects.append(subject_phrase)

        tags.append(subjects)
        
    return(tags)