from django.db import models

# Create your models here.
class RequestedData(models.Model):
    tweet_text = models.CharField(max_length = 500)
    tweet_sentiment = models.CharField(max_length = 1)

