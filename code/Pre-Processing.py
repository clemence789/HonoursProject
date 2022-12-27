import pandas as pd
import emoji

df = pd.read_csv(r'code\dataset.csv', encoding='utf-8')
df.columns = ['ID', 'Date', 'Username', 'Text']

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

#Expand Acronyms

#Write the changes to csv file
df.to_csv(r'code\dataset1.csv')