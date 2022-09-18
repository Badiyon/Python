#fizz if by 3
#buzz if by 5
#fizzbuzz if by both 3 and 5

def fizz_buzz(input):
    if((input % 3 == 0) & (input % 5 == 0)):
        return "FizzBuzz"
    elif(input % 3 == 0):
        return "Fizz"
    elif(input % 5 == 0):
        return "Buzz"
    else:
        return "Fuck you"



print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(30))
print(fizz_buzz(11))