import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

df = pd.read_csv(r'code\dataset1.csv', encoding='utf-8')

vectoriser = TfidfVectorizer()

test = vectoriser.fit_transform(df['Text'])
print(test)

