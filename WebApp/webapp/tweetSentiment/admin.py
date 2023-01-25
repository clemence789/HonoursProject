from django.contrib import admin
from .models import RequestedData, NegativeTweets

# Register your models here.
admin.site.register(RequestedData)
admin.site.register(NegativeTweets)