from django.shortcuts import render, redirect
from django.http import HttpResponse
from tweetSentiment.forms import DataEntryForm
from tweetSentiment import preprocessing

def index(request):
    return HttpResponse("You're at the sentiment analysis index.")



def entry(request):
    #handling if the request is GET, show user blank form, if request is POST check data is valid
    if request.method == 'POST':
        form = DataEntryForm(request.POST)

        if form.is_valid():
            bearer_token = form.cleaned_data['bearerToken']
            keywords = form.cleaned_data['keywords']
            preprocessing.collectTweets(bearer_token, keywords)
            preprocessing.cleanTweets()

            return redirect('results')

    else:
        form = DataEntryForm()
    return render(request, 'tweetSentiment/data_entry.html', {'form': form})



def results(request):
    response = "You're looking at the request response"
    return HttpResponse(response)