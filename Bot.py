import tweepy
import time

bearerToken =  'AAAAAAAAAAAAAAAAAAAAAF6ZbQEAAAAAHav7fG49AzdG1ToSh3kTEabeQYs%3D3bPQzsVkUa7bhaBxHeC2TYVjBqcDL2bo5VdsTjAKlp3FrZcOfy'
apiKey = 'IyXNY0859xdxNlQNZkPDXZrCP'
apiKeySecret = 'qWMHKxN8lfwcmulcwdNaSiXTiI0woW0fupqejRoUguUSZxUUvQ'
accessToken = '1513691830323273729-9z9o2tuTlRYDN2TvcjsmDBtbNmbfMB'
accessTokenSecret = 'LWSXci3hJ0xSLBJY56qqmFmpqzUG8j9lOUh2FMqmAjfZZ'


class Stream(tweepy.StreamingClient):
    def on_connect(self):
        print("Connected")

    def on_tweet(self, tweet):
        if tweet.referenced_tweets == None:
            print(tweet.text)

            time.sleep(0.2)

stream = Stream(bearer_token = bearerToken)
auth = tweepy.OAuth1UserHandler(apiKey, apiKeySecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)
Client = tweepy.Client(consumer_key=apiKey, consumer_secret= apiKeySecret, access_token= accessToken, access_token_secret= accessTokenSecret)

myTweetId = 1517944950674968577

hashtag = '#btc'
screen_name = "@whale_alert"
search_terms = ["btc", "bitcoin"]

for term in search_terms:
    stream.add_rules(tweepy.StreamRule(term))

stream.filter(tweet_fields=["referenced_tweets"])


def tweet():
    tweets = api.user_timeline(user_id = screen_name, tweet_mode = 'extended')
    for tweet in reversed(tweets) :
        if '#btc' in tweet.full_text.lower:
            print (str(tweet.full_text.lower))
