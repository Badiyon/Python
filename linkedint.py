
class linkedlistnode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class linkedlist:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = linkedlistnode(value)
        if self.head is None:
            self.head = node
            return

        currentnode = self.head
        while True:
            if currentnode.nextNode is None:
                currentnode.nextNode = node
                break
            currentnode = currentnode.nextNode


    def printlinkedlist(self):
        currentnode = self.head
        while currentnode is not None:
            print(currentnode.value, '->', end=" ",)
            currentnode = currentnode.nextNode
        print('none', )


ll = linkedlist()
ll.printlinkedlist()
ll.insert("3")
ll.printlinkedlist()
ll.insert("45")
ll.printlinkedlist()
ll.insert("100")
ll.printlinkedlist()