from django import forms

class DataEntryForm(forms.Form):
    bearerToken = forms.CharField(label="Bearer Token")
    number_of_tweets = forms.IntegerField(label="Number of Tweets")
    keywords = forms.CharField(label = 'Keyword(s)', required=False)
    username = forms.CharField(label = 'Username', required=False)
