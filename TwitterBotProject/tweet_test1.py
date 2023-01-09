import sys
from twython import Twython
import time

#this is just a twitter bot test using Twython

tweetStr = "This is a test"
tweetStr1 = "This is another test"
apikey='***'
apikeysecret='***'

accesstoken='***'
accesstokensecret='***'

api = Twython(apikey, apikeysecret, accesstoken, accesstokensecret)

api.update_status(status=tweetStr)
api.update_status(status=tweetStr1)

time.sleep(300)

api.update_status(status="it worked")
api.update_status(status="wow very cool idea me")
