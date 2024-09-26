class PersonType():
    def __init__(self):
        self.fName = input("First Name: ")
        self.lName = input("Last Name: ")
        
    def displayName(self):
        return f"First Name: {self.fName}\n Last Name: {self.lName}"

p1 = PersonType()

print(p1.displayName())