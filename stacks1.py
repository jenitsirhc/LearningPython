class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
        return item
    
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
    def __repr__(self):
        status = "Printing Stack:\n"
        for i in range(self.size()-1, -1, -1):
            status += str(self.items[i]) + "\n"
        status += "---"
        return status

s= Stack()

    

print("Stack is Empty", s.isEmpty())

print("Adding Itmes:",s.push(4))

print("Adding items",s.push(14))

print("Adding items",s.push(8))

print("Stack size",s.size())

print("peeking the top item", s.peek())

print(s)



print("Adding Items:",s.push(10))

print("Adding items",s.push(7))

print(s)



print("Removing",s.pop())

print("Removing",s.pop())

print("Removing",s.pop())

print("Stack is Empty:",s.isEmpty())

print(s)