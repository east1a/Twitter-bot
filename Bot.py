from operator import contains
from pickle import TRUE
import tweepy
import time

bearerToken =  'AAAAAAAAAAAAAAAAAAAAAF6ZbQEAAAAAHav7fG49AzdG1ToSh3kTEabeQYs%3D3bPQzsVkUa7bhaBxHeC2TYVjBqcDL2bo5VdsTjAKlp3FrZcOfy'
apiKey = 'IyXNY0859xdxNlQNZkPDXZrCP'
apiKeySecret = 'qWMHKxN8lfwcmulcwdNaSiXTiI0woW0fupqejRoUguUSZxUUvQ'
accessToken = '1513691830323273729-9z9o2tuTlRYDN2TvcjsmDBtbNmbfMB'
accessTokenSecret = 'LWSXci3hJ0xSLBJY56qqmFmpqzUG8j9lOUh2FMqmAjfZZ'
hashtag = '#btc'
myTweetId = 1517944950674968577
whaleAlertID = 1039833297751302144
search_terms = ["btc", "bitcoin"]

class Stream(tweepy.StreamingClient):
    def on_connect(self):
        print("Connected")

    def on_tweet(self, tweet):
        if tweet.referenced_tweets == None:
                print (tweet.text)
                time.sleep(0.2)


def get_tweets(username, number_of_tweets):
    tweets = api.user_timeline(user_id = username, count = number_of_tweets) 
    for tweet in tweets:
        print (tweet.text)

def get_specific_tweets(username, number_of_tweets, search_term):
    tweets = api.user_timeline(user_id = username, count = number_of_tweets) 
    for tweet in tweets:
        if search_term in tweet.text:
            print (tweet.text)

def get_user_id(screen_name):
    user = api.get_user(screen_name)
    ID = user.id_str
    print("ID of the user is : " + ID)

stream = Stream(bearer_token = bearerToken)
auth = tweepy.OAuth1UserHandler(apiKey, apiKeySecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)
Client = tweepy.Client(consumer_key=apiKey, consumer_secret= apiKeySecret, access_token= accessToken, access_token_secret= accessTokenSecret)

#stream.filter(tweet_fields=["referenced_tweets"])
#response = api.get_users_tweets(user_id)
#get_user_id("Whale_alert")
stream.filter(follow=[whaleAlertID])
#get_specific_tweets(whaleAlertID, 10, "BTC")
