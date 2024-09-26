# Creating a Node
class Node:
    def __init__(self, item):
        self.item = item          # Assigning value to a node
        self.next = None          # Assigning the initial value of a linked list
# Creating a class for a linked list
class LinkedList:
    def __init__(self):
        self.head = None
# reference variable to linked list
linked_list = LinkedList()

# Instantiation
# Assigning the head of a linked list
linked_list.head = Node(1)

# Assign values to nodes
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

# Connect the Linked Lists Node
linked_list.head.next = second      # point the head node to the second node
second.next = third                 # point the second node to the third node
third.next = fourth
fourth.next = fifth

# Display the Connected Nodes of a Linked Lists
while linked_list.head is not None:
    print(linked_list.head.item, end=" ")
    linked_list.head = linked_list.head.next