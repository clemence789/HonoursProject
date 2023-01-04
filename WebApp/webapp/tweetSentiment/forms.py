from django import forms

class DataEntryForm(forms.Form):
    bearerToken = forms.CharField(label="Bearer Token")
    keywords = forms.CharField(label = 'Keyword(s)')
