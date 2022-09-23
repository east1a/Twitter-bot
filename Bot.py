from operator import contains
from pickle import TRUE
import tweepy
import time

bearerToken =  'AAAAAAAAAAAAAAAAAAAAAF6ZbQEAAAAAvfEb2M6Of4TzKnSDMwLz4Orcha0%3DhJJP8PWxPN3Mc0F3VQGkMlP0N8azHM64SG2mn3XCR4cMPQ41mQ'
apiKey = 'IyXNY0859xdxNlQNZkPDXZrCP'
apiKeySecret = 'qWMHKxN8lfwcmulcwdNaSiXTiI0woW0fupqejRoUguUSZxUUvQ'
accessToken = '1513691830323273729-9z9o2tuTlRYDN2TvcjsmDBtbNmbfMB'
accessTokenSecret = 'LWSXci3hJ0xSLBJY56qqmFmpqzUG8j9lOUh2FMqmAjfZZ'
hashtag = '#btc'
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
    user = api.get_user(screen_name = screen_name)
    ID = user.id_str
    print("ID of the user is : " + ID)

stream = Stream(bearer_token = bearerToken)
auth = tweepy.OAuth1UserHandler(apiKey, apiKeySecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)
Client = tweepy.Client(consumer_key=apiKey, consumer_secret= apiKeySecret, access_token= accessToken, access_token_secret= accessTokenSecret)
rule = tweepy.StreamRule("(from:@whale_alert) (-is:retweet -is:reply)")
#stream.filter(tweet_fields=["referenced_tweets"])
#response = api.get_users_tweets(user_id)
get_user_id("@whale_alert")
get_specific_tweets(whaleAlertID, 10, "BTC")
stream.add_rules(rule)
stream.filter()
for rules in stream.get_rules()[0]:
    stream.delete_rules()[0]


