class customerType:
    def __init__(self, fname, lname, accountNum):
        self.fname = fname
        self.lname = lname
        self.accountNum = accountNum

    def setfName(self, fname):
        self.fname = fname
    
    def setlName(self, lname):
        self.lname = lname
    
    def setAccountNum(self, accountNum):
        self.accountNum = accountNum
    
    def getfName(self):
        return self.fname
    
    def getlName(self):
        return self.lname
    
    def getAccountNum(self):
        return self.accountNum
    
    def __eq__(self, other):
        return self.accountNum == other.accountNum
    
    def __lt__(self, other):
        return self.accountNum < other.accountNum

    def __le__(self, other):
        return self.accountNum <= other.accountNum
    
    def __gt__(self, other):
        return self.accountNum > other.accountNum
    
    def __ge__(self, other):
        return self.accountNum > other.accountNum

    def printCustomerDetails(self):
        return f"Name: {self.fname} {self.lname} \nAccount Number: {self.accountNum}"
    
    
