from django.db import models

# Create your models here.
class RequestedData(models.Model):
    tweet_text = models.CharField(max_length = 5000)
    tweet_text_clean = models.CharField(max_length = 5000, default="na")
    tweet_sentiment = models.CharField(max_length = 1)
    request_number = models.IntegerField()

