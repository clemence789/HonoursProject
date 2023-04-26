import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import pandas as pd

#open and read dataset
df = pd.read_csv(r'C:\Users\cleme\Documents\1HonoursProject\Code\dataset_clean_2.csv', encoding='utf-8')

#function to get the part of speech tag of every word
def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

#initialize lemmatizer
lemmatizer = WordNetLemmatizer()

#function to lemmatize every word in sentence
def lmtz(sentence):
    return([lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in nltk.word_tokenize(sentence)])
    
values = df['Text'].values
texts = []

#add all lemmatized sentences to array
for i in range(len(values)):
    values[i] = str(values[i])
    lemmatized = lmtz(values[i])
    texts.append(lemmatized)

#join individual tweet arrays into one string
for i in range(len(texts)):
    texts[i] = ' '.join(texts[i])

#replace tweets columns with lemmatized tweets
df['Text'] = texts

#Write the changes to csv file
df.to_csv(r'C:\Users\cleme\Documents\1HonoursProject\Code\dataset_clean_lemmatized_2.csv')