from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class DataEntryForm(forms.Form):
    
    #number of tweets input validator
    def validate_number(value):
        if value < 10:
            raise ValidationError(
                _('Must be a number between 10 and 100'),
                params={'value': value},
            )
        elif value > 100:
            raise ValidationError(
                _('Must be a number between 10 and 100'),
                params={'value': value},
            )
    
    #username input field validator
    def validate_username(value):
        punctuation = """!"#$%&'()*+, -./:;<=>?@[\]^`{|}~"""
        if any(char in punctuation for char in value) :
            raise ValidationError(
                _('Please enter a valid username'),
            )

    
    #add fields in form
    number_of_tweets = forms.IntegerField(label="Please enter a number between 10 and 100", validators=[validate_number]) #number of tweets
    keywords = forms.CharField(label = 'Keyword(s)', required=False) #keywords
    username = forms.CharField(label = 'Username', required=False, validators=[validate_username]) #username
