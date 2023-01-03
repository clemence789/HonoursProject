import PySimpleGUI as sg
import tweepy
import csv
from datetime import datetime
import pandas as pd
import emoji
import re
import dictionaries
from sklearn.model_selection import train_test_split as tts
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn import metrics

layout = [[sg.Text("Hello please enter your twitter bearer token")], [sg.Button("OK")]]
sg.Window("Twitter Sentiment Classifier", layout)

sg.theme('SandyBeach')
layout = [
[sg.Text('Please enter your Twitter API Bearer Token')],
[sg.Text('Token', size =(15, 1)), sg.InputText()],
[sg.Submit()]
]

window = sg.Window('Simple data entry window', layout)
event, values = window.read()

bearer_token = str(values[0])


client = tweepy.Client(bearer_token = bearer_token, wait_on_rate_limit = True)

##########################################################################################################################################

max_results = 100
iteration = 0
while iteration < 4:
    tweets = client.search_recent_tweets(
        "upset OR angry OR disgusted OR worst OR hate OR detest -is:retweet lang:en",
        max_results = max_results, #max results received, has to be number between 10 and 100
        tweet_fields = ['text']
        )

    data = []
    for i in tweets.data:
        in_tweet = []
        in_tweet.append(str(i.text))
        data.append(in_tweet)
    
    print('Tweets collected: ' + str(len(tweets.data)))

    #write to csv
    with open(r'code\dataset_user.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        #rows
        writer.writerows(data)

        iteration+=1

#########################################################################################################################################

df = pd.read_csv(r'code\dataset_user.csv', encoding='utf-8')
df.columns = ['Text']

#Remove rows with empty values
df = df.dropna(axis=0)

#replace emojis in text if the text value is not NaN
def emoji_to_text(text):
    if type(text) != float:
        return emoji.demojize(text)
    else:
        return text
df['Text'] = df['Text'].apply(emoji_to_text)
print("Replaced emojis")
#df.to_csv(r'code\dataset2.csv')

#remove URLs
df = df.apply(lambda x: x.replace({r'http\S+': ''}, regex=True))
(print('Removed URLs'))

#turn all text to lower case
df['Text'] = df['Text'].str.lower()
print('Turned text to lowercase')

#expand contractions
df['Text'] = df['Text'].str.replace("’", "'") #replace instances of different apostrophe so they are recognized by the contraction dictionary
def expand_contractions(text):
    return(re.sub(r"\b(\w+('\w+))\b", lambda x: dictionaries.CONTRACTIONS.get(x.group(1), x.group(1)), text)) #change regex from expanding acronyms to handle apostrophe
df['Text'] = df['Text'].apply(expand_contractions)

#remove stopwords
def remove_stopwords(tweet):
    return(re.sub(r"\b(\w+)\b", lambda x: dictionaries.STOPWORDS.get(x.group(1), x.group(1)), tweet))
df['Text'] = df['Text'].apply(remove_stopwords)
print('Removed Stopwords')

#Remove punctuation
df['Text'] = df['Text'].str.replace(r'[^\w\s]+', ' ', regex=True)
df['Text'] = df['Text'].str.replace('_', ' ')
df['Text'] = df['Text'].str.replace(r'\n', '', regex=True)
df['Text'] = df['Text'].str.replace(r'[^\u0000-\u05C0\u2100-\u214F]+', '', regex=True)
df['Text'] = df['Text'].str.replace('  ', ' ', regex=True)
print('Removed punctuation')

#Remove numbers
df['Text'] = df['Text'].str.replace('\d+', '', regex=True)
print('Removed numbers')

#Remove duplicate letters
df['Text'] = df['Text'].str.replace(r'(\w)\1{2,}', r'\1', regex=True)
print('Removed duplicate letters')

#Expand Acronyms using acronym dictionary
def acronym_to_word(text):
    return(re.sub(r"\b(\w+)\b", lambda x: dictionaries.ACRONYM_TRANSLATE.get(x.group(1), x.group(1)), text))

df['Text'] = df['Text'].apply(acronym_to_word)
print('Replaced acronyms with their meaning')

df['Text'] = df['Text'].str.replace('  ', ' ', regex=True)
#Write the changes to csv file
df.to_csv(r'code\dataset_user.csv')

###########################################################################################################################################

#Use models to do predictions


