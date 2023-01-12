from django import forms

class DataEntryForm(forms.Form):
    #add fields in form
    bearerToken = forms.CharField(label="Bearer Token") #bearer token
    number_of_tweets = forms.IntegerField(label="Number of Tweets") #number of tweets
    keywords = forms.CharField(label = 'Keyword(s)', required=False) #keywords
    username = forms.CharField(label = 'Username', required=False) #username
