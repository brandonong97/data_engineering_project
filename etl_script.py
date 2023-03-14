import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

access_key = '1y0d7ppGO1ZxDm8nP5IruYO3F'
access_secret = '9IslAKBRxySU3HPvvhvNfacEu6iSR4YhBcz6OmtYlWUH16IobY'
consumer_key = '354908163-oAPjCJa8itxN0eBqQN9sVwljAl0YlAkJTD6YoC06'
consumer_secret = '0NX70v1YOUGnPDnCjI8bzcatJqfB7zoQs2cmkZyQBU3wo'

#authentication
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

#creating API
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='@KDTrey5ls',
                           count = 200,
                           include_rts = False,
                           tweet_mode = 'extended')

tweet_list = []
for tweet in tweets:
    text = tweet._json['full_text']

    refined_tweet = {"user": tweet.user.screen_name,
                    "text" : text,
                    'favourite_count' : tweet.favorite_count,
                    'retweet_count': tweet.retweet_count,
                    'created_at' : tweet.created_at}
    tweet_list.append(refined_tweet)

df = pd.DataFrame(tweet_list)
df.to_csv('twitter_test')