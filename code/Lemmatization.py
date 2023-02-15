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


sentence = "this is an example sentence used for this example"
def lmtz(sentence):
    return([lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in nltk.word_tokenize(sentence)])
    
for i in df['Text']:
    
print(lmtz(df.loc[1, 'Text']))

#df['Text'] = df['Text'].apply(lmtz)
#print(type(df['Text']))

#print(df['Text'])