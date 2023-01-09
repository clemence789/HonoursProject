import pickle
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
import numpy as np

#apply ml model
def prediction_model(tweet):
    transformer = TfidfTransformer()
    loaded_vec = CountVectorizer(decode_error = "replace", vocabulary=pickle.load(open(r'tweetSentiment/tfidf.sav', "rb")))
    tweet = transformer.fit(loaded_vec.fit_transform(np.array([tweet]).flatten()))

    
    nb = pickle.load(open(r'tweetSentiment/finalized_model.sav', 'rb'))
    prediction = nb.predict(tweet)
    return prediction