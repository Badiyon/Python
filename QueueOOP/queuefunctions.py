
import objectperson
import copy

def printobject(person):
    print(person.firstname)
    print(person.lastname)
    print(person.ID)
    print(person.gradelevel)

def queuepop(queue):
    printobject(queue.pop(0))

def queuepush(queue, person):
    queue.append(person)

def queueadd(queue, firstname, lastname, ID, gradelevel):
    person = objectperson.objectPerson(firstname, lastname, ID, gradelevel)
    queue.append(person)

def queuepeek(queue):
    printobject(queue[0])

def getID(person):
    return person.ID

def queuesearch(queue1, id):

    found = 0

    for x in range(len(queue1)):
        p = getID(queue1.pop(0))
        if(p == id):
            found = 1
    if (found == 1):
        print('The ID was found')
    else:
        print('The ID was not found')





