class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None
    
class SLinkedList:
    def __init__(self):
        self.headval = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    
def search(self, x):
        current = self.head
        while current != None:
            if current.data == x:
                return True
            current = current.next
         
        return False
      
def AtBeginning(self, newInfo):
    newNode = Node(newInfo)
    newNode.nextval = self.headVal
    self.headval = newNode

def AtEnd(self, newInfo):
    newNode = Node(newInfo)
    if self.headval is None:
       self.headval = newNode
       return
    
    last = self.headval
    while(last.nextval):
        last = last.nextval
    last.nextval = newNode

def RemoveNode (self, removeKey):
    Headval = self.headval

    if ( Headval is not None ):
        if (Headval.dataval == removeKey):
            self.headval = Headval.next
            Headval = None
            return
    
    while(Headval is not None):
        if (Headval.dataval == removeKey):
            break
        prev = Headval
        Headval = Headval.next
            
        if(Headval == None):
            return
        
        prev.next = Headval.next
        Headval = None

def listprint(self):
    printval = self.headval
    while printval is not None:
        print(printval.dataval)
        printval = printval.nextval
        print()

def iterate_item(self):
    current_item = self.headval
    while current_item:
        val = current_item.dataval
        current_item = current_item.nextval
        yield val 


