import sys
from twython import Twython
from random import seed
from random import randint
import time

#testing


tweetStr = "bruh"

apikey='***'
apikeysecret='***'

accesstoken='***'
accesstokensecret='***'

api = Twython(apikey, apikeysecret, accesstoken, accesstokensecret)

path = '/home/pi/Desktop/testbot/test.txt'
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
