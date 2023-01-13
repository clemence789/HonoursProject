from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class DataEntryForm(forms.Form):
    #add fields in form
    def validate_number(value):
        if value < 10:
            raise ValidationError(
                _('%(value)s is too small'),
                params={'value': value},
            )
        elif value > 100:
            raise ValidationError(
                _('%(value)s is too large'),
                params={'value': value},
            )
    bearerToken = forms.CharField(label="Bearer Token") #bearer token
    number_of_tweets = forms.IntegerField(label="Number of Tweets", validators=[validate_number]) #number of tweets
    keywords = forms.CharField(label = 'Keyword(s)', required=False) #keywords
    username = forms.CharField(label = 'Username', required=False) #username
