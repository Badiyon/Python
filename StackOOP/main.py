

import objectperson
import stackfunctions

stack = []
cont = 1

def printmenu():
    print("What do you want to do? ")
    print("1. Add to the stack")
    print("2. Remove from the top of the stack")
    print("3. Peek at the top of the stack")
    print("4. Search the stack for an ID")

stackfunctions.stkadd(stack, "", "", 0, 0)
stackfunctions.stkadd(stack, "john", "johnson", 1, 2)
stackfunctions.stkadd(stack, "bob", "bobby", 3, 4)
stackfunctions.stkadd(stack, "dan", "bowser", 5, 6)


while(cont != 0):
    printmenu()
    inp = input()

    match inp:
        case "1":
            firstname = input('What is the firstname ')
            lastname = input('What is the lastname ')
            ID = input('What is the ID ')
            gradelevel = input('What is the gradelevel ')
            stackfunctions.stkadd(stack, firstname, lastname, ID, gradelevel)
        case "2":
            stackfunctions.stkpop(stack)
        case "3":
            stackfunctions.stkpeek(stack)
        case "4":
            searchID = int(input('What ID are you looking for? '))
            stackfunctions.stksearch(stack, searchID)
    cont = int(input('Do you want to continue? '))




