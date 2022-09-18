




string = '00000010'
test = string[::-1]

count = 0

for i in range(0, len(test)):
    if(int(test[i]) == 1):
        count = count + 2**int(i)


#print(count)


#TRANSLATE/CONVERT INTEGER TO AN ASCII CHARACTER
def asciichar(x):
    print(chr(x))

#FINALLY THIS ALL WORKS.
#WHEN GIVEN A STRING OF 1'S AND 0'S. ASSUMING THAT WE ARE GIVEN A STRING WHOSE LENGTH IS DIVISIBLE BY 8.
#WE ARE ABLE TO ITERATE THROUGH THE STRING 8 BITS AT A TIME AND TRANSLATE THOSE VALUES TO AN INTEGER THAT
#WE SHOULD BE ABLE TO USE TO THEN TRANSLATE IT TO A ASCII CHARACTER.

bin = '000000100000001000000010010001001100110001010101'

#0010 0010 0100 0000 0100 0000 0100 0000

cout = 0
tester = bin[::-1]

setter = [0] * 8
pos = 0
k = 0

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
    asciichar(int(cout)) #send integer to fucntion that prints the corresponding ASCII CHARACTER.
    cout = 0
    pos = 0





#if(int(string[i]) == 1):
        #count = count + 2**int(i)

#TRANSLATE/CONVERT INTEGER TO AN ASCII CHARACTER
def asciichar(x):
    print(chr(x))