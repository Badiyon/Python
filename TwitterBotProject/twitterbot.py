

import sys
from twython import Twython
from random import seed
from random import randint
import time

tweetStr = "bruh"

apikey='TWdtedFsmDjmvBK8I8CnEU0tJ'
apikeysecret='7pB8W5kn4yIVv3ilqpiwnWxy5Y6lLRKwgPFcIITU7MpjTj2qWm'

accesstoken='1546188306475630600-8WnWsSqZVleqJv7ONcD6dFZCNemhjS'
accesstokensecret='OBnwnpq1pRPIXBsrrqcG5Xgvcn4GWjLr2Pm39aJR4lnbt'

api = Twython(apikey, apikeysecret, accesstoken, accesstokensecret)

path = '/home/pi/Desktop/testbot'
TXTFILE = open(path, 'r')
content = TXTFILE.readlines()


seed(1)

arr = []
arr = [0 for i in range(12)]

for y in range(12):
    value = randint(0, 11)
    while arr[value] == 1:
        value = randint(0, 11)
    arr[value] = 1
    print(value)
    print(content[value])
    tweetStr=content[value]
    api.update_status(status=tweetStr)
    time.sleep(3600)
