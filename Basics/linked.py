
class linkedlistnode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


node1 = linkedlistnode("3")
node2 = linkedlistnode("7")
node3 = linkedlistnode("10")

node1.nextNode = node2
node2.nextNode = node3

currentnode = node1
while True:
    print (currentnode.value, "->",)
    if currentnode.nextNode is None:
        print ("none")
        break
    currentnode = currentnode.nextNode