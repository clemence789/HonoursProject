#Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

df = pd.read_csv(r'code\dataset1.csv', encoding='utf-8')

# modified code from https://www.geeksforgeeks.org/python-sentiment-analysis-using-vader/
def sentiment_scores(sentence):
    sentiment = ""
    sentiment_analyser = SentimentIntensityAnalyzer()
    sentiment_dict = sentiment_analyser.polarity_scores(sentence)
    if sentiment_dict['compound'] < -0.65 :
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

#df['Text'] = df['Text'].to_string()
df['Score'] = df['Text'].apply(sentiment_scores)

#Shift classification column to the front
df = df[['Score'] + [col for col in df.columns if col != 'Classification']]

#delete extra column created by appending classification to the dataframe
df = df.drop(df.columns[1], axis=1)

print("Added classification to every tweet")

#Write the changes to csv file
df.to_csv(r'code\dataset1.csv')