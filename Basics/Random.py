
from random import seed
from random import randint

seed(1)

arr = []
arr = [0 for i in range(13)]

for y in range(13):
    value = randint(0, 12)
    while arr[value] == 1:
        value = randint(0, 12)

    arr[value] = 1
    print(value)




