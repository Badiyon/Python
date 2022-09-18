import sys
from twython import Twython
import time


tweetStr = "This is a test"
tweetStr1 = "This is another test"
apikey='TWdtedFsmDjmvBK8I8CnEU0tJ'
apikeysecret='7pB8W5kn4yIVv3ilqpiwnWxy5Y6lLRKwgPFcIITU7MpjTj2qWm'

accesstoken='1546188306475630600-8WnWsSqZVleqJv7ONcD6dFZCNemhjS'
accesstokensecret='OBnwnpq1pRPIXBsrrqcG5Xgvcn4GWjLr2Pm39aJR4lnbt'

api = Twython(apikey, apikeysecret, accesstoken, accesstokensecret)

api.update_status(status=tweetStr)
api.update_status(status=tweetStr1)

time.sleep(300)

api.update_status(status="it worked")
api.update_status(status="wow very cool idea me")
