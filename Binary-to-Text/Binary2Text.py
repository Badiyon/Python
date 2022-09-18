binary_path = '/users/badiy/desktop/BINARY.txt'
binary_file = open(binary_path, 'r')


ascii_path = '/users/badiy/desktop/ASCII.txt'
ascii_file = open(ascii_path, 'w')

#TRANSLATE/CONVERT INTEGER TO AN ASCII CHARACTER
def asciichar(x):
    print(chr(x))
    return chr(x)

#what we will store the string into so we only have write to the file once
STRING = ''

#what we read the binary file into
#(this is just a basic version so the binary is a straight string of 1's and 0's
#on the first line so we don't need to read multiple lines of the text document.
#if this was to be used on a file with multiple lines of binary then it probably wouldnt work.)
LINE = binary_file.readline()

#used to calculate the ascii integer value from the 8 bit binary
cout = 0

#this is to reverse the input from the file so we can probably calculate/translate the int value
tester = LINE[::-1]

#this are used to keep track of how many bits we have read and then make sure we only read in 8 bits
setter = [0] * 8
pos = 0
k = 0

#when we have read in the binary input from the file, we are ASSUMING that it have enough bits so that it is visible
#by 8 (for 8 bit representation) so we only have to iterate through the length of the read in input and divide it by 8
#for how many characters we will need to translate. then from there we just iterate through 8 bits each, translate
#those 8 bits to a int value then call a function to translate it to a character represented by the int value.
#take the character and add it to the end of the output string.
for j in range(0, int(len(tester)/8)):
    while(pos <= 7):
        setter[pos] = tester[k]
        if(k < int(len(tester))-1):
            k = k + 1
        else:
            break
        pos = pos + 1
    for a in range(0, len(setter)):
        if(int(setter[a]) == 1):
            cout = cout + 2**int(a)
    STRING = STRING + asciichar(int(cout)) #send integer to fucntion that prints the corresponding ASCII CHARACTER.
    cout = 0
    pos = 0

#reverse the string since currently we read through the binary in reverse so our character are reversed also, so just
#reverse the string to have the complete and correct ascii output.
STRING = STRING[::-1]
ascii_file.write(STRING)