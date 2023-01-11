from django.shortcuts import render, redirect
from django.http import HttpResponse
from tweetSentiment.forms import DataEntryForm
from tweetSentiment import preprocessing
from tweetSentiment import ml_model
from .models import RequestedData


def index(request):
    return HttpResponse("You're at the sentiment analysis index.")



def entry(request):
    
    #handling if the request is GET, show user blank form, if request is POST check data is valid
    if request.method == 'POST':
        form = DataEntryForm(request.POST)

        if form.is_valid():
            last_object = RequestedData.objects.last()
            request_number = last_object.request_number + 1

            bearer_token = form.cleaned_data['bearerToken']
            numberTweets = form.data['number_of_tweets']
            keywords = form.cleaned_data['keywords']
            username = form.cleaned_data['username']

            if keywords != '':
                tweet_text = preprocessing.collectTweetsKeywords(bearer_token, keywords, numberTweets)
                cleanTweets = preprocessing.cleanTweets(tweet_text)
            
            elif username != '':
                tweet_text = preprocessing.collectTweetsUsername(bearer_token, username, numberTweets)
                cleanTweets = preprocessing.cleanTweets(tweet_text)

            for i in range(len(cleanTweets)):
                tweet_sentiment = str(ml_model.prediction_model(cleanTweets[i]))
                RequestedData.objects.create(tweet_text_clean = cleanTweets[i], request_number = request_number, tweet_sentiment = tweet_sentiment, tweet_text = tweet_text[i])
            return redirect('results')
    
    else:
        form = DataEntryForm()

    return render(request, 'tweetSentiment/data_entry.html', {'form': form})



def results(request):
    #user_input = request.GET["age"]
    last_object = RequestedData.objects.last()
    number = last_object.request_number
    query_results = RequestedData.objects.filter(request_number = number)
    context = {'query_results': query_results}
    return render(request, 'tweetSentiment/response.html', context)