#importing required packages

import tweepy
from textblob import TextBlob

#authenticating twitter we need four variables

consumer_key = 'copy your consumer key here'
consumer_secret = 'cop your consumer secret key here'

access_token = 'copy your access token here'
access_token_secret = 'copy your access token secret key here'

#Now lets login via code

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

#note: instead of trump you provide any of the keyword
# we are collecting tweets which contain a certain keyword 
public_tweets = api.search('Trump')


#for printing the tweets and for getting the polarity and subjectivity
for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)