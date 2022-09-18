
import objectperson

def printobject(person):
    print(person.firstname)
    print(person.lastname)
    print(person.ID)
    print(person.gradelevel)

def stkpop(stack):
    printobject(stack.pop())

def stkpush(stack, person):
    stack.append(person)

def stkadd(stack, firstname, lastname, ID, gradelevel):
    person = objectperson.objectPerson(firstname, lastname, ID, gradelevel)
    stack.append(person)

def stkpeek(stack):
    printobject(stack[-1])


def stksearch(stack, id):
    stack1 = []
    stack1 = stack.copy()
    found = 0
    p = stack1.pop()
    while(p.ID != 0):
        if (p.ID == id):
            found = 1
        p = stack1.pop()
    if(found == 1):
        print('The ID was found ')
    else:
        print('The ID was not found ')

