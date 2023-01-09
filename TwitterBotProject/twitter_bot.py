import sys
from twython import Twython
from random import seed
from random import randint
import time

def apisetup():
    apikey = '***'
    apikeysecret = '***'
    accesstoken = '***'
    accesstokensecret = '***'
    api = Twython(apikey, apikeysecret, accesstoken, accesstokensecret)
    return api

def filepath():
    path = '/home/pi/Desktop/testbot/test.txt'
    TXTFILE = open(path, 'r')
    content = TXTFILE.readlines()
    return content


def getvalue(arr):
    seed(1)
    value = randint(0, 11)
    while arr[value] == 1:
        value = randint(0, 11)
    arr[value] = 1
    return value



def main():
    api = apisetup()

    content = filepath()

    arr = [0 for i in range(12)]

    for y in range(12):
        value = getvalue(arr)
        tweetStr = content[value]
        api.update_status(status=tweetStr)
        time.sleep(3600)

if __name__ == "__main__":
    main()

