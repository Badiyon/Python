import tweepy

#some tests trying to get tweet information using tweepy

apikey='***'
apikeysecret='***'

accesstoken='***'
accesstokensecret='***'

auth = tweepy.OAuthHandler(apikey, apikeysecret)
auth.set_access_token(accesstoken, accesstokensecret)
api = tweepy.API(auth, wait_on_rate_limit=True)

target = "badiyonbot"
print("getting data for " + target)
item = api.get_user(target)
print("name: " + item.name)
print("description: " + item.description)
print("screen_name: " + item.screen_name)
print("id: " + str(item.id))

tweets = api.home_timeline(target, trim_user=item.id)
print(tweets)
