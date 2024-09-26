# insert a linked list at the end
# Creating a Node
class Node:
    def __init__(self, item):
        self.item = item    # Assigning value to a node
        self.next = None    # Assigning the initial value of a linked list
# Creating a class for a linked list
class SLinkedList:
    def __init__(self):
        self.head = None
    # Function to add new nodes
    def at_end(self, newdata):
        newNode = Node(newdata)
        if self.head is None:
            self.head = newNode
            return
        lastNode = self.head
        while(lastNode.next):
            lastNode = lastNode.next
        lastNode.next = newNode

    # Print the linked list
    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.item)
            printval = printval.next

newMonth = input("Enter month name: ")  # input from the user
list = SLinkedList()
list.head = Node("Jan")
L2 = Node("Feb")
L3 = Node("Mar")

list.head.next = L2
L2.next = L3

list.at_end(newMonth)

list.listprint()

