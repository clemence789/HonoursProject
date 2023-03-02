import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn import metrics
import pickle
import numpy as np
from sklearn.metrics import make_scorer, f1_score

#<!------------------------------------5 cat dataset----------------------------------------------------------->
#read dataframe of my dataset
df = pd.read_csv(r'C:\Users\cleme\Documents\1HonoursProject\Code\outside_dataset\stanfordDataset.csv', encoding='utf-8')

#<!------------------------------------their dataset----------------------------------------------------------->
#read dataframe other dataset
#df = pd.read_csv(r'code\outside_dataset\stanfordDataset.csv', encoding='utf-8')

#<!------------------------------------2 cat dataset----------------------------------------------------------->
#read dataframe 2 cat dataset
#df = pd.read_csv(r'C:\Users\cleme\Documents\1HonoursProject\Code\dataset_clean_lemmatized_2cat.csv', encoding='utf-8')


#get only the score and text columns that will be used for the classification
ml_df = df.filter(['Score', 'Text'], axis=1)

#declaring feature vector and target variable
x = ml_df['Text'].values.astype('U') #feature vector
y = ml_df['Score'].values.astype('U') #target variable

#Use TFIDF to vectorize tweets
vectoriser = TfidfVectorizer()

#Vectorise the tweets
x = vectoriser.fit_transform(x)

#save the tfidf model
file_name = 'tfidf_stanford.sav'
pickle.dump(vectoriser, open("tfidf_stanford.sav", "wb"))

x_train, x_test, y_train, y_test = tts(x, y, test_size = 0.2, random_state = 0)

#Use multinomial Naïve Bayes to classify test set
nb = MultinomialNB()
svm = SVC(kernel = 'linear')
lr = LogisticRegression()

#<!----------------------------------------weighted----------------------------------------------------------->

f1 = cross_val_score(estimator = nb, X= x, y=y, cv=10, scoring= 'f1_weighted')
recall = cross_val_score(estimator = nb, X= x, y=y, cv=10, scoring= 'recall_weighted')
precision = cross_val_score(estimator = nb, X= x, y=y, cv=10, scoring= 'precision_weighted')

#<!---------------------------------------unweighted----------------------------------------------------------->
#f1 = cross_val_score(estimator = nb, X= x, y=y, cv=10, scoring= 'f1_macro')
#recall = cross_val_score(estimator = nb, X= x, y=y, cv=10, scoring= 'recall_macro')
#precision = cross_val_score(estimator = nb, X= x, y=y, cv=10, scoring= 'precision_macro')

print("recall: ", np.mean(recall))
print("precision: ", np.mean(precision))
print("average f1: ", np.mean(f1))


nb.fit(x_train, y_train)


#save the nb model
filename = 'finalized_model_stanford.sav'
pickle.dump(nb, open(filename, 'wb'))


nb.score(x_test, y_test)


#print predictions of test set
y_pred = nb.predict(x_test)

#Find accuracy
score_nb = metrics.accuracy_score(y_test, y_pred)

#<!-------------------------------------------2 columns----------------------------------------------------------->

print(metrics.classification_report(y_test, y_pred, target_names = ['0', '1']))

#<!-------------------------------------------5 columns----------------------------------------------------------->

#print(metrics.classification_report(y_test, y_pred, target_names = ['1', '2', '3', '4', '5']))


print(metrics.confusion_matrix(y_test, y_pred))