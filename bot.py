#import libraries and packages
import tweepy
from textblob import TextBlob
import csv
import os
import re

#authentication 
consumerKey = "Type your consumer key here"
consumerSecret = "Type your consumer secret here"

accessToken = "Type your access token here"
accessTokenSecret = "Type your access token secret here"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

#search tweets
tweets = api.search_tweets(q="Just Stop Oil", lang="en", result_type="mixed", count=100)

#function to clean tweets
def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

#function to append tweet sentiments to csv file
def append_list_to_csv(tweets, filename):
    file_exists = os.path.isfile(filename)
    with open(filename, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if not file_exists:
            writer.writerow(['Tweet', 'Polarity', 'Subjectivity'])  # write header only if the file is newly created
        for tweet in tweets:
            text = clean_tweet(tweet.text)
            analysis = TextBlob(text)
            polarity = analysis.polarity
            subjectivity = analysis.subjectivity
            writer.writerow([text, polarity, subjectivity])