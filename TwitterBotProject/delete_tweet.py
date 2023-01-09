import sys
from twython import Twython

tweet_id = 1547352919657390081

#learning how to use Twython to delete tweets

apikey='***'
apikeysecret='***'

accesstoken='***'
accesstokensecret='***'

api = Twython(apikey, apikeysecret, accesstoken, accesstokensecret)

api.destroy_status(id=tweet_id)
