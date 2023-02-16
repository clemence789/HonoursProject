import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import pandas as pd

df = pd.read_csv(r'C:\Users\cleme\Documents\1HonoursProject\Code\dataset_clean_2.csv', encoding='utf-8')

def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

lemmatizer = WordNetLemmatizer()

def lmtz(sentence):
    return([lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in nltk.word_tokenize(sentence)])
    
values = df['Text'].values
texts = []
for i in range(len(values)):
    values[i] = str(values[i])
    lemmatized = lmtz(values[i])
    texts.append(lemmatized)

for i in range(len(texts)):
    texts[i] = ' '.join(texts[i])


df['Text'] = texts

#Write the changes to csv file
df.to_csv(r'C:\Users\cleme\Documents\1HonoursProject\Code\dataset_clean_lemmatized_2.csv')