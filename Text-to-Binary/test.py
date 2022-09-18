#This file is for testing out different ideas about ascii and text file handling
#The goal is to read in a text file and then output the results to another text file
#with the original text files binary equivalent

#The binary representation we are aiming for is 8-bit binary representation:
#Examples:
# 'A' = 65 = 0100 0001
# 'a' = 97 = 0110 0001
# 'abc' = 0110 0001 0110 0010 0110 0011

#when we have a string or line of text I want to be able to iterate through the line of characters
#one by one until we reach the end of the line and then send the results to the textfile and move
#down a line and do this until we reach the end of the original file.


#first test is making sure we can have a string and access different positions of it and print out the
# value of that position

x = "hello"
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])

for i in range(0, len(x)):
    print(ord(x[int(i)]))

#this for loop should allow use to take in a entire line of a file and then iterate through
#until we reach the end indicated by "len(x)" (hopefully)


#next part would be to get a loop that takes the "ord()" result and turns it into a binary string

#this is a example of how the algorithm might work
set = [0] * 8
y = "Hey"
x = ord(y[2])
hold1 = 0
hold2 = x

if(hold2 > 127):
    set[7] = 1
for i in range(0, 7):
    hold1 = hold2 % 2
    hold2 = int(hold2 / 2)
    set[i] = hold1

#we now have the binary position but now need to reverse it to get the actual binary code for it.
print(set)
test = set[::-1]
print(test)






#most of what is left is to read in a line from a file and then see if we can iterate through it and then
#output the results to a file.
#the following is the basic idea
path = '/users/badiy/desktop/ASCIITEST.txt'

days_file = open(path, 'r')

linetest = days_file.readline()

for i in range(0, len(linetest)):
    print(linetest[i])

#anothe test might be to read in the entire file and then work through it completely?



