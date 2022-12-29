#using Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
import nltk
from nltk.corpus import wordnet as wn

synonyms = []
for syn in wn.synsets('dog'):
    for i in syn.lemmas():
        synonyms.append(i.name())
print(synonyms)


#okay so:
#go through every tweet in dataframe
#select one non-stopword word per tweet randomly
#select the first of the synonyms for it
#create new tweet with replacement synonym
#another tweet with added synonym
#

