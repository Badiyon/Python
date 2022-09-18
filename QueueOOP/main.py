import objectperson
import queuefunctions

queue = []
cont = 1


def printmenu():
    print("What do you want to do? ")
    print("1. Add to the queue")
    print("2. Remove from front of the queue")
    print("3. Peek at the front of the queue")
    print("4. Search the queue for an ID")


queuefunctions.queueadd(queue, "john", "johnson", 1, 2)
queuefunctions.queueadd(queue, "bob", "bobby", 3, 4)
queuefunctions.queueadd(queue, "dan", "bowser", 5, 6)


print(len(queue))

while(cont != 0):
    printmenu()
    inp = input()

    match inp:
        case "1":
            firstname = input('What is the firstname ')
            lastname = input('What is the lastname ')
            ID = input('What is the ID ')
            gradelevel = input('What is the gradelevel ')
            queuefunctions.queueadd(queue, firstname, lastname, ID, gradelevel)
        case "2":
            queuefunctions.queuepop(queue)
        case "3":
            queuefunctions.queuepeek(queue)
        case "4":
            searchID = int(input('What ID are you looking for? '))
            queue1 = []
            queue1 = queue.copy()
            queuefunctions.queuesearch(queue1, searchID)
    cont = int(input('Do you want to continue? '))