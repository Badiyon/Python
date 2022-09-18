import sys
from twython import Twython

tweet_id = 1547352919657390081

apikey='TWdtedFsmDjmvBK8I8CnEU0tJ'
apikeysecret='7pB8W5kn4yIVv3ilqpiwnWxy5Y6lLRKwgPFcIITU7MpjTj2qWm'

accesstoken='1546188306475630600-8WnWsSqZVleqJv7ONcD6dFZCNemhjS'
accesstokensecret='OBnwnpq1pRPIXBsrrqcG5Xgvcn4GWjLr2Pm39aJR4lnbt'

api = Twython(apikey, apikeysecret, accesstoken, accesstokensecret)

api.destroy_status(id=tweet_id)
