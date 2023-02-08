from django.db import models

# Create your models here.
class RequestedData(models.Model):
    #set fields in database objects
    tweet_text = models.CharField(max_length = 5000) #tweet text
    tweet_text_clean = models.CharField(max_length = 5000, default="na") #cleaned tweet text
    tweet_sentiment = models.CharField(max_length = 1) #sentiment
    request_number = models.IntegerField() #request number

class NegativeTweets(models.Model):
    tweet_text = models.CharField(max_length = 5000) #tweet text
    personal_tweet = models.CharField(max_length = 1) #Is it directed at someone directly or not
    first_subject = models.CharField(max_length = 5000) #subject of tweet
    second_subject = models.CharField(max_length = 5000) #subject of tweet
    request_number = models.IntegerField()

