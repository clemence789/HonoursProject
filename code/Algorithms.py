import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn import metrics

df = pd.read_csv(r'code\dataset1.csv', encoding='utf-8')

#get only the score and text columns that will be used for the classification
ml_df = df.filter(['Score', 'Text'], axis=1)

#declaring feature vector and target variable
x = ml_df['Text']
y = ml_df['Score']

#split dataset into 80 for training and 20 for testing
x_train, x_test, y_train, y_test = tts(x, y, test_size = 0.2, random_state = 0)

#Use TFIDF to vectorize tweets
vectoriser = TfidfVectorizer(stop_words = 'english', analyzer='word')
#On the training set
x_train_tfidf = vectoriser.fit_transform(x_train)

#On the test set
x_test_tfidf = vectoriser.transform(x_test)

#Use multinomial Naïve Bayes to classify test set
nb = MultinomialNB()
nb.fit(x_train_tfidf, y_train)

nb.score(x_test_tfidf, y_test)

y_pred = nb.predict(x_test_tfidf)

#Find accuracy
score_nb = metrics.accuracy_score(y_test, y_pred)

print(metrics.classification_report(y_test, y_pred, target_names = ['1', '2', '3', '4', '5']))
print(metrics.confusion_matrix(y_test, y_pred))
print(score_nb)

#Logistic regression
lr = LogisticRegression()
lr.fit(x_train_tfidf, y_train)

lr.score(x_test_tfidf, y_test)

y_pred = lr.predict(x_test_tfidf)

score_lr = metrics.accuracy_score(y_test, y_pred)

print(metrics.classification_report(y_test, y_pred, target_names = ['1', '2', '3', '4', '5']))
print(metrics.confusion_matrix(y_test, y_pred))
print(score_lr)

#SVM
svm = SVC(kernel = 'linear')
svm.fit(x_train_tfidf, y_train)

svm.score(x_test_tfidf, y_test)

y_pred = svm.predict(x_test_tfidf)

score_svm = metrics.accuracy_score(y_test, y_pred)

print(metrics.classification_report(y_test, y_pred, target_names = ['1', '2', '3', '4', '5']))
print(metrics.confusion_matrix(y_test, y_pred))
print(score_svm)

