# CLASS DVDTYPE
class dvdType:
    
    def __init__(self, title, star1, star2, producer, director, company, noOfDVDs):
        self.title = title
        self.star1 = star1
        self.star2 = star2
        self.producer = producer
        self.director = director
        self.company = company
        self.noOfDVDs = noOfDVDs

    def __str__(self):
        return f"({self.title}, {self.star1},{self.star2},{self.producer},{self.director},{self.company},{self.noOfDVDs})"


    def setTitle(self, title):
        self.title = title
    
    def setStar1(self, star1):
        self.star1 = star1
    
    def setStar2(self, star2):
        self.star2 = star2
    
    def setProducer(self, producer):
        self.producer = producer
    
    def setDirector(self, director):
        self.director = director
    
    def setCompany(self, company):
        self.company = company

    def setNoOfDVDs(self, noOfDVDs):
        self.noOfDVDs = noOfDVDs
    
    def getTitle(self):
        return self.title 
    
    def getStar1(self):
        return self.star1
    
    def getStar2(self):
        return self.star2

    def getProducer(self):
        return self.producer
    
    def getDirector(self):
        return self.director
    
    def getCompany(self):
        return self.company

    def getNoOfDVDs(self):
        return self.noOfDVDs

    def printDVD(self):
        return  f"Title: {self.title} \nStar1: {self.star1} \nStar2: {self.star2} \nProducer: {self.producer} \nDirector: {self.director} \nCompany: {self.company} \nNumber of copies available: {self.noOfDVDs}"
    
    def checkout(self):
        if self.noOfDVDs == 0:
           print("Unavailable. This DVD is currently out of stock.")
        
        elif self.noOfDVDs > 0: 
            self.noOfDVDs = self.noOfDVDs -1
            print("\nYou have successfully checked out the DVD")
            print("Number of DVDs left: ", self.noOfDVDs)
        
        else:
            print("Error. Please Try again.")
            

    def checkin(self):
        self.noOfDVDs = self.noOfDVDs +1
        print("You have successfully checked in the DVD")
        print("Number of DVDs: ", self.noOfDVDs)

    def printTitle(self):
        print("DVD Title: ", self.title)
    
    def checkTitle(self, title):
        return(self.title == title)
    
    def updateStock(self, num):
        self.noOfDVDs = self.noOfDVDs + num

class customerType:
    def __init__(self, fname, lname, accountNum):
        self.fname = fname
        self.lname = lname
        self.accountNum = accountNum
        #self.rentedDVDs = rentedDVDs

    def setfName(self, fname):
        self.fname = fname
    
    def setlName(self, lname):
        self.lname = lname
    
    def setAccountNum(self, accountNum):
        self.accountNum = accountNum
    
    def setRentedDVDs(self, rentedDVDs):
        self.rentedDVDs = rentedDVDs
    
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
        return f"Name: {self.fname}{self.lname} \nAccount Number: {self.accountNum} " 
        
        """\nRented DVDs: {self.rentedDVDs}"""
    
    
