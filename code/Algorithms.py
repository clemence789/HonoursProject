import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn import metrics
import sklearn.model_selection as model_selection
import pickle
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import make_scorer, f1_score

#read dataframe
df = pd.read_csv(r'code\dataset1.csv', encoding='utf-8')

#get only the score and text columns that will be used for the classification
ml_df = df.filter(['Score', 'Text'], axis=1)

#declaring feature vector and target variable
x = ml_df['Text'].values.astype('U') #feature vector
y = ml_df['Score'].values.astype('U') #target variable

#Use TFIDF to vectorize tweets
vectoriser = TfidfVectorizer()

#Vectorise the tweets
x_tfidf = vectoriser.fit_transform(x)

#save the tfidf model
file_name = 'tfidf.sav'
pickle.dump(vectoriser, open("tfidf.sav", "wb"))

#Use multinomial Naïve Bayes to classify test set
nb = MultinomialNB()
svm = SVC(kernel = 'linear')
lr = LogisticRegression()

f1 = cross_val_score(estimator = nb, X= x_tfidf, y=y, cv=10, scoring= 'f1_macro')
recall = cross_val_score(estimator = nb, X= x_tfidf, y=y, cv=10, scoring= 'recall_macro')
precision = cross_val_score(estimator = nb, X= x_tfidf, y=y, cv=10, scoring= 'precision_macro')

print("recall: ", np.mean(recall))
print("precision: ", np.mean(precision))
print("average f1: ", np.mean(f1))



#kf = model_selection.KFold(n_splits = 10, shuffle = True, random_state=42)

#print("%0.2f accuracy with a standard deviation of %0.2f" % (scores.mean(), scores.std(), scores.f1()))



#nb.fit(x_train_tfidf, y_train)


#save the nb model
#filename = 'finalized_model.sav'
#pickle.dump(nb, open(filename, 'wb'))


#nb.score(x_test_tfidf, y_test)

#print predictions of test set
#y_pred = nb.predict(x_test_tfidf)
#print(y_pred)



#Find accuracy
#score_nb = metrics.accuracy_score(y_test, y_pred)

#print(metrics.classification_report(y_test, y_pred, target_names = ['1', '2', '3', '4', '5']))
#print(metrics.confusion_matrix(y_test, y_pred))
#print(score_nb)


#repeat with Logistic regression
#lr = LogisticRegression()
#lr.fit(x_train_tfidf, y_train)

#lr.score(x_test_tfidf, y_test)

#y_pred = lr.predict(x_test_tfidf)

#score_lr = metrics.accuracy_score(y_test, y_pred)

#print(metrics.classification_report(y_test, y_pred, target_names = ['1', '2', '3', '4', '5']))
#print(metrics.confusion_matrix(y_test, y_pred))
#print(score_lr)

#repeat with SVM
#svm = SVC(kernel = 'linear')
#svm.fit(x_train_tfidf, y_train)

#svm.score(x_test_tfidf, y_test)

#y_pred = svm.predict(x_test_tfidf)

#score_svm = metrics.accuracy_score(y_test, y_pred)

#print(metrics.classification_report(y_test, y_pred, target_names = ['1', '2', '3', '4', '5']))
#print(metrics.confusion_matrix(y_test, y_pred))
#print(score_svm)