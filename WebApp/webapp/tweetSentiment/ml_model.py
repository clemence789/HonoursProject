import pickle
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer, TfidfVectorizer
import numpy as np

#apply ml model
def prediction_model(tweet):
    loaded_vec = pickle.load(open(r'tweetSentiment/tfidf.sav', "rb")) #load saved tfidf model
    tweet = loaded_vec.transform(np.array([tweet])) #apply tfidf model to tweets

    nb = pickle.load(open(r'tweetSentiment/finalized_model.sav', 'rb')) #load saved algorithm
    prediction = nb.predict(tweet) #apply algorithm to tweets
    
    return prediction #return sentiment predictions