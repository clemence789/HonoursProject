#Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

df = pd.read_csv(r'code\dataset1.csv', encoding='utf-8') #read the dataframe with pre-processed tweets

# modified code from https://www.geeksforgeeks.org/python-sentiment-analysis-using-vader/
#add sentiment score using VADER lexicon
def sentiment_scores(sentence):
    sentiment = ""
    sentiment_analyser = SentimentIntensityAnalyzer()
    sentiment_dict = sentiment_analyser.polarity_scores(sentence) #addscore to each tweet
    
    #give sentiment score based on lexicon score
    if sentiment_dict['compound'] < -0.45 :
        sentiment = '1'
    elif sentiment_dict['compound'] <= -0.05 :
        sentiment = '2'
    elif sentiment_dict['compound'] <= 0.05:
        sentiment = '3'
    elif sentiment_dict['compound'] <= 0.65:
        sentiment = '4'
    else:
        sentiment = '5'
    return sentiment

#ranked 1 to 5 with 1 being very negative and 5 being very positive

df['Score'] = df['Text'].apply(sentiment_scores) #add score to score column

#Shift score column to the front
df = df[['Score'] + [col for col in df.columns if col != 'Classification']]

#delete extra column created by appending classification to the dataframe
df = df.drop(df.columns[1], axis=1)

print("Added classification to every tweet")

#Write the changes to csv file
df.to_csv(r'code\dataset1.csv')