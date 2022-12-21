import tweepy
import logging
import json
import csv


print("hello")

#Authenticate with the API through tweepy (à voir)
client = tweepy.Client(
    consumer_key="HM2L20WSoeiDOGuBpWMBhO35Y", 
    consumer_secret="lQF726OQxRqvFoGfUFEBgPSrV4vH8phzRhrmMt2WbHfuVfX4c4", 
    access_token="1604068859706855424-yHTZzJEtlJJbCYiv21RwfxMPmhTRYI", 
    access_token_secret="WMwVZ2V7I3sNEQqmISUVy3BrczkCMyfo6oLaDlO6VWRXO")

api = tweepy.API(client)

#enable logging to the console
logging.basicConfig(level=logging.DEBUG)

#use stream to use only one connection between the app and the API instead of repeated requests
streaming_client = tweepy.StreamingClient("AAAAAAAAAAAAAAAAAAAAABI%2BkgEAAAAAXWj%2B%2Bf6FxPZ9fu9kE1wu0NPZiQM%3DauGTgGLIg4RuJ0rj54Z5I5vVFFHOOm7b4tu21dopElGbR6GhFK")
#streaming_client.sample()
