import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import numpy as np

df = pd.read_csv(r'code\dataset1.csv', encoding='utf-8')

#get only the score and text columns that will be used for the classification
ml_df = df.filter(['Score', 'Text'], axis=1)

#declaring feature vector and target variable
x = ml_df['Text']
y = ml_df['Score']

#y = list(y)
#y = np.array(y)
#y = [str(i) for i in y]
#x = list(x)
#x = np.array(x, dtype=str)
#y = [str(i) for i in x]

#split dataset into 80 for training and 20 for testing
x_train, x_test, y_train, y_test = tts(x, y, test_size = 0.2, random_state = 0)

#Use TFIDF to vectorize tweets
vectoriser = TfidfVectorizer(stop_words = 'english', analyzer='word')
x_train_tfidf = vectoriser.fit_transform(x_train)
x_test_tfidf = vectoriser.transform(x_test)

model = MultinomialNB()
model.fit(x_train_tfidf, y_train)

#x_train_tfidf = x_train_tfidf.reshape(-1,1)
#x_test_tfidf = x_test_tfidf.reshape(-1,1)

model.score(x_test_tfidf, y_test)

y_pred = model.predict(x_test_tfidf)

score1 = metrics.accuracy_score(y_test, y_pred)

print(score1)

#ml_df.to_csv(r'code\dataset2.csv')