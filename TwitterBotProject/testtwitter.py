import tweepy
apikey='TWdtedFsmDjmvBK8I8CnEU0tJ'
apikeysecret='7pB8W5kn4yIVv3ilqpiwnWxy5Y6lLRKwgPFcIITU7MpjTj2qWm'

accesstoken='1546188306475630600-8WnWsSqZVleqJv7ONcD6dFZCNemhjS'
accesstokensecret='OBnwnpq1pRPIXBsrrqcG5Xgvcn4GWjLr2Pm39aJR4lnbt'

auth = tweepy.OAuthHandler(apikey, apikeysecret)
auth.set_access_token(accesstoken, accesstokensecret)
api = tweepy.API(auth, wait_on_rate_limit=True)

api.update_status(status="this is a test")