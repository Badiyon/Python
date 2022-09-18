path = '/users/badiy/desktop/days.txt'

days_file = open(path, 'r')

#print(days_file.read()) #reads the entire contents of the file

print(days_file.readline()) #read each line
print(days_file.readline())
print(days_file.readline())
print(days_file.readline())
print(days_file.readline())
print(days_file.readline())
print(days_file.readline())
print(days_file.readline())
print(days_file.readline())
print(days_file.readline())
print(days_file.readline())
if(days_file.readline() == ''):
    print("yo")

#print(days_file.readlines()) #reads each line into a list where each place in the list is the entire line in the file