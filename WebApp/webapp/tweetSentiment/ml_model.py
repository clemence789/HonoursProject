import pickle
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer, TfidfVectorizer
import numpy as np

#apply ml model
def prediction_model(tweet):
    loaded_vec = pickle.load(open(r'tweetSentiment/tfidf.sav', "rb"))
    tweet = loaded_vec.transform(np.array([tweet]))

    nb = pickle.load(open(r'tweetSentiment/finalized_model.sav', 'rb'))
    prediction = nb.predict(tweet)
    return prediction