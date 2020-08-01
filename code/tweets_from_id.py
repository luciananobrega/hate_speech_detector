"""
Script to get tweet text from tweet ID, got on twitter data set
(data/B2Share_eudat/twitter_dataset.csv)
"""

import pandas as pd
import tweepy
import tqdm

consumer_key = 'xxxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxx'

access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

twitter_dataset = pd.read_csv('data\\B2Share_eudat\\dataset_dummy_classes.csv')
list_tweet_id = twitter_dataset['tweet_id']
list_tweet = []


for tweet_id in tqdm.tqdm(list_tweet_id):
    try:
        tweet = api.get_status(int(tweet_id))
        list_tweet.append(tweet.text)
    except tweepy.TweepError:
        list_tweet.append('NA')

        
# With this, I decided to save list_tweet on the csv file, so we'll already have those information when we import.
# it took about 1h30 to get all tweets from Twitter ID

twitter_dataset['data'] = list_tweet
twitter_dataset.to_csv('data\\B2Share_eudat\\twitter_dataset.csv', index=False)
