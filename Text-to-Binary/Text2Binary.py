#NAME:
#DATE:
#PURPOSE/USE:
#CHANGES:
#
#
#

text_path = '/users/badiy/desktop/TEXT.txt'
text_file = open(text_path, 'r')


binary_path = '/users/badiy/desktop/BINARY.txt'
binary_file = open(binary_path, 'w')

line = text_file.readline()
string = ''

while(line != ''):
    for i in range(0, len(line)):
        set = [0] * 8
        x = ord(line[i])
        hold1 = 0
        hold2 = x
        if (hold2 > 127):
            set[7] = 1
        for i in range(0, 7):
            hold1 = hold2 % 2
            hold2 = int(hold2 / 2)
            set[i] = hold1
        test = set[::-1]
        #print(test)
        for i in range(0, len(test)):
            string = str(test[i]) + string
        string = string[::-1]
        print(string)
        binary_file.write(string)
        string = ''
    line = text_file.readline()