import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pandas as pd

df = pd.read_csv(r'code\dataset1.csv', encoding='utf-8')

vectoriser = TfidfVectorizer(stop_words = 'english', analyzer='word',ngram_range=(1,2))
vectorised_values = vectoriser.fit_transform(df['Text'])

print(vectorised_values)
