from django.shortcuts import render, redirect
from django.http import HttpResponse
from tweetSentiment.forms import DataEntryForm
from tweetSentiment import preprocessing
from tweetSentiment import ml_model
from .models import RequestedData, NegativeTweets

#view of index page
def index(request):
    return HttpResponse("You're at the sentiment analysis index.")


#view of entry page
def entry(request):
    
    #if the request is GET, show user blank form, if request is POST check data is valid
    if request.method == 'POST':
        form = DataEntryForm(request.POST)

        if form.is_valid():
            #get the last object in dataset
            last_object = RequestedData.objects.last()
            
            #use the last object to set the request number to +1
            request_number = last_object.request_number + 1

            #get bearer token, number of tweets, keywords, and username from the form
            bearer_token = form.cleaned_data['bearerToken']
            numberTweets = form.data['number_of_tweets']
            keywords = form.cleaned_data['keywords']
            username = form.cleaned_data['username']

            #perform analysis on the tweets if the user entered a username
            if keywords != '':
                tweet_text = preprocessing.collectTweetsKeywords(bearer_token, keywords, numberTweets) #collect tweets
                cleanTweets = preprocessing.cleanTweets(tweet_text) #preprocess
                tagged_tweets = preprocessing.tagTweets(cleanTweets) #POS tagging
            
            #perform analysis on the tweets if the user entered a keyword
            elif username != '':
                tweet_text = preprocessing.collectTweetsUsername(bearer_token, username, numberTweets) #collect tweets
                cleanTweets = preprocessing.cleanTweets(tweet_text) #preprocess
                tagged_tweets = preprocessing.tagTweets(cleanTweets) #POS tagging
                print(tagged_tweets)

            #go through the tweets array to apply algorithm
            for i in range(len(cleanTweets)):
                tweet_sentiment = str(ml_model.prediction_model(cleanTweets[i])) #apply model
                
                #remove the brackets from the sentiment returned
                tweet_sentiment = tweet_sentiment.replace("[", "")
                tweet_sentiment = tweet_sentiment.replace("]", "")

                tweet_sentiment = tweet_sentiment.replace("'", "")

                #remove the brackets from tweets
                tweet_text[i] = str(tweet_text[i])
                tweet_text[i] = tweet_text[i].replace("[", "")
                tweet_text[i] = tweet_text[i].replace("]", "")

                #add the tweets to database
                RequestedData.objects.create(tweet_text_clean = cleanTweets[i], request_number = request_number, tweet_sentiment = tweet_sentiment, tweet_text = tweet_text[i])

            negative_tweets = RequestedData.objects.filter(request_number = request_number, tweet_sentiment = '1').values('tweet_text_clean')

            tweetsSub = []

            for tweet in negative_tweets:
                tweetsSub.append(tweet['tweet_text_clean'])

            subject = preprocessing.tagTweets(tweetsSub)
            
            for i in range(len(subject)):
                if subject[i][0] is None:
                    subject[i][0] = "None"
                if subject[i][1] is None:
                    subject[i][1] = "None"
                
                if "they" in subject[i][0]:
                    personal = "1"
                elif "you" in subject[i][0]:
                    personal = "1"
                elif "them" in subject[i][0]:
                    personal = "1"
                elif "he" in subject[i][0]:
                    personal = "1"
                elif "she" in subject[i][0]:
                    personal = "1"
                else:
                    personal = "0"

                if "they" in subject[i][1]:
                    personal = "1"
                elif "you" in subject[i][1]:
                    personal = "1"
                elif "them" in subject[i][1]:
                    personal = "1"
                elif "he" in subject[i][1]:
                    personal = "1"
                elif "she" in subject[i][1]:
                    personal = "1"
                else:
                    personal = "0"

                print(negative_tweets[i])

                NegativeTweets.objects.create(tweet_text = tweetsSub[i], first_subject = subject[i][0], second_subject=subject[i][1], personal_tweet = personal, request_number = request_number)
            
            #redirect to results page
            return redirect('results')
    
    else:
        form = DataEntryForm()
        

    return render(request, 'tweetSentiment/data_entry.html', {'form': form})


#view of results page
def results(request):
    last_object = RequestedData.objects.last() #get the last object from the database
    number = last_object.request_number #get the last request number
    query_results = RequestedData.objects.filter(request_number = number) #fetch all data entered that has that request number
    negative_tweets = RequestedData.objects.filter(request_number = number, tweet_sentiment = '1').values('tweet_text')
    personal_tweets = NegativeTweets.objects.filter(request_number = number, personal_tweet = '1').values('tweet_text')
    context = {'query_results': query_results, 'negative_tweets': negative_tweets, 'personal_tweets': personal_tweets} #dictionary of results
    return render(request, 'tweetSentiment/response.html', context) #return the page with request results