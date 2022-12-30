import pandas as pd
import emoji
import acronymDict as ad
import re
import dictionaries

df = pd.read_csv(r'code\dataset.csv', encoding='utf-8')
df.columns = ['ID', 'Date', 'Username', 'Text']

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
    return(re.sub(r"\b(\w+)\b", lambda x: ad.ACRONYM_TRANSLATE.get(x.group(1), x.group(1)), text))

df['Text'] = df['Text'].apply(acronym_to_word)
print('Replaced acronyms with their meaning')

#Write the changes to csv file
df.to_csv(r'code\dataset1.csv')