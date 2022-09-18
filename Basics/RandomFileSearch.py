

from random import seed
from random import randint

path = 'C:/Users/badiy/Desktop/RandomTestFile.txt'
TXTFILE = open(path, 'r')
#print(TXTFILE.readline()) #read each line
content = TXTFILE.readlines()

#for x in range(10):
#    print(content[x])

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





