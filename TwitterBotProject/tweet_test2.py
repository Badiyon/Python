import tweepy
apikey='***'
apikeysecret='***'

accesstoken='***'
accesstokensecret='***'

auth = tweepy.OAuthHandler(apikey, apikeysecret)
auth.set_access_token(accesstoken, accesstokensecret)
api = tweepy.API(auth, wait_on_rate_limit=True)

api.update_status(status="this is a test")

