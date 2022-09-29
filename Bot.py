from operator import contains
from pickle import TRUE
import tweepy
import time

bearerToken =  'XXXXXXX%XXXXXXX'
apiKey = 'XXXXXXX'
apiKeySecret = 'XXXXXXX'
accessToken = 'XXXXXXX-XXXXXXX'
accessTokenSecret = 'XXXXXXX'
hashtag = '#btc'
whaleAlertID = 1039833297751302144
search_terms = ["btc", "bitcoin"]
Client = tweepy.Client(consumer_key=apiKey, consumer_secret= apiKeySecret, access_token= accessToken, access_token_secret= accessTokenSecret)
auth = tweepy.OAuth1UserHandler(apiKey, apiKeySecret)
api = tweepy.API(auth)
auth.set_access_token(accessToken, accessTokenSecret)


class Stream(tweepy.StreamingClient):
    #upon connection to the stream it will print connected
    def on_connect(self):
        print("Connected")

    #upon encountering a tweet in the stream, it will print the tweet and wait .2 second until it starts looking for more tweets
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
rule = tweepy.StreamRule(
    {
        "value": "(#BTC) (from:whale_alert OR from:whaleAlertID) (-is:retweet)",
        "tag": "(#BTC)"
    }
)
stream.add_rules(rule)
print(stream.get_rules())
stream.filter()


#stream.filter(tweet_fields=["referenced_tweets"])
#response = api.get_users_tweets(user_id)
#get_user_id("@whale_alert")
#get_specific_tweets(whaleAlertID, 40, "#BTC")
#for rules in stream.get_rules()[0]:
#    stream.delete_rules("1575397673670090752")
#    stream.delete_rules("1573402414463401984")
