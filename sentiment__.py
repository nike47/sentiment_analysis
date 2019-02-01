import tweepy
from textblob import TextBlob 


consumer_key='LcOC1S1FjfJ3RAhSyIzZxdPUT'
consumer_secret='NUJh5NpvMGYzZfZni6q5bbA7RsxbpsMUWBovjjBfbojWbWke63'

access_token='3298019112-TdaTMoI6fRwR6dkN0jWFoZ3ZsIgCvmbUuyUEnE7'
access_token_secrets='1S3TndMD6cyU03OHMLXID3R5Lr8YpPWGWxQesVWR1Bf94'


auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secrets) 

api=tweepy.API(auth)

public_tweets= api.search('nikhil')

for tweet in public_tweets:
	print(tweet.text)
	analysis=TextBlob(tweet.text)
	print(analysis.sentiment)