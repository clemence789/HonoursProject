from django.db import models

# Create your models here.
class BearerToken(models.Model):
    question_text = models.CharField(max_length=200)
    user_token = models.CharField(max_length = 200)
    def __str__(self):
        return self.question_text