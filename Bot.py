from operator import contains
from pickle import TRUE
import os
import tweepy
import time

bearerToken =  os.getenv('TWEEPY_BEARER_TOKEN')
apiKey = os.getenv('TWEEPY_API_KEY')
apiKeySecret = os.getenv('TWEEPY_API_KEY_SECRET')
accessToken = os.getenv('TWEEPY_ACCESS_TOKEN')
accessTokenSecret = os.getenv('TWEEPY_ACCESS_TOKEN_SECRET')
whaleAlertID = 1039833297751302144

Client = tweepy.Client(consumer_key=apiKey, consumer_secret= apiKeySecret, access_token= accessToken, access_token_secret= accessTokenSecret)
auth = tweepy.OAuth1UserHandler(apiKey, apiKeySecret)
api = tweepy.API(auth)
auth.set_access_token(accessToken, accessTokenSecret)


class Stream(tweepy.StreamingClient):
    #upon connection to the stream it will print connected
    def on_connect(self):
        print("Connected")

    #upon encountering a tweet in the stream, it will print the tweet and then retweet it from the bot account
    def on_tweet(self, tweet):
        print(tweet.text)
        try:
            Client.retweet(tweet.id)

        except Exception as error:
            print(error)
            time.sleep(0.2)

#returns a specific number of a twitter users most recent tweets
def get_tweets(username, number_of_tweets):
    tweets = api.user_timeline(user_id = username, count = number_of_tweets) 
    for tweet in tweets:
        print (tweet.text)

#checks a number of most recent tweets to see if they contain a search term and prints them if they do
def get_specific_tweets(username, number_of_tweets, search_term):
    tweets = api.user_timeline(user_id = username, count = number_of_tweets) 
    for tweet in tweets:
        if search_term in tweet.text:
            print (tweet.text)

#returns the ID of any user via their twitter handle
def get_user_id(screen_name):
    user = api.get_user(screen_name = screen_name)
    ID = user.id_str
    print("ID of the user is : " + ID)

stream = Stream(bearer_token = bearerToken)
rules = tweepy.StreamRule(
 "(from:whale_alert) (#BTC) (-is:retweet)"
)

stream.add_rules(rules)
print(stream.get_rules())
stream.filter()


#stream.filter(tweet_fields=["referenced_tweets"])
#get_user_id("@whale_alert")
#get_specific_tweets(whaleAlertID, 40, "#BTC")
#for rules in stream.get_rules()[0]:
#    stream.delete_rules("1575397673670090752")
