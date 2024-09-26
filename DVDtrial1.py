import DVDLinkedlist
import DVDBSTCustomer


#USER OR ADMIN!
def main():
    print()

    while True:
        print()
        print("SELECT FROM THE FOLLOWING OPTIONS:")
        print("[0] - EXIT Program")
        print("[1] - USER MENU")
        print("[2] - ADMIN MENU")
        print()

        try:
            menu = int(input("Input your answer here>> "))
        except ValueError:
            print("\nPlease enter a valid value in the given options")

        if menu == 0:
            print("\nYou have terminated the program.")
            exit()
        
        elif menu == 1:
            choice_1()
        
        elif menu == 2:
            choice_2()


#USER MENU
def choice_1():
    DVDstock = DVDLinkedlist.SLinkedList()
    DVDstock = []
    try:
        data = open("DVDList.cvs")
        for line in data:
            columns = line.split(',')
            titlenew = columns [0]
            star1new = columns [1]
            star2new = columns [2]
            producernew = columns [3]
            directornew = columns [4]
            compnew = columns [5]
            nonew = int(columns [6])

            info = dvdType(titlenew, star1new, star2new, producernew, directornew, compnew, nonew)
            DVDstock.append(info)
            
    except Exception as e:
        print(e)
            
    finally:
        data.close()

    while True:
        print()
        print("Menu for Customers")
        print("[0] - RETURN TO MENU SELECTION")
        print("[1] - CHECK DVD and its AVAILABILITY")
        print("[2] - CHECK-OUT a DVD")
        print("[3] - CHECK-IN a DVD")
        print("[4] - List ALL DVD TITLES")
        print("[5] - List ALL DVD DETAILS")
        print()

        try:
            menu = int(input("\nPut in the value based on the given options>> "))

        except ValueError:

            print("\nPlease enter a valid value in the given menu")

        if menu == 0:
            print("\nYou have exited the USER menu")
            return main()
        
        # CHECK if DVD EXISTS and AVAILABLE COPIES
        elif menu == 1:
            title = input("\nEnter the title of the movie here>> ")
            found = False
            for item in DVDstock:
                if item.getTitle() == title:
                    print("\nDVD Found")
                    found = True
                    if found == True:
                        n = item.getNoOfDVDs()
                        print("Number of AVAILABLE copy/ies ", n)

            if found == False: 
                print("\nSorry. This DVD does not exist within the store.")
        

        #CHECK-OUT DVD
        elif menu == 2:
            title = input("\nEnter the title of the movie here>> ")
            found = False
            for item in DVDstock:
                if item.getTitle() == title:
                    print("Item found")
                    found = True
                    if found == True:
                        n = item.getNoOfDVDs()
                        if n > 0:
                            item.checkout()
                        else:
                            print("\nThis item is currently out of stock")
                
            if found == False:
                print("\nThis DVD does not exist.")


        #CHECK-IN DVD
        elif menu == 3:
            title = input("\nEnter the title of the movie here>> ")
            found = False
            for item in DVDstock:
                if item.getTitle() == title:
                    print("Item found")
                    found = True
                    if found == True:
                        item.checkin()

            if found == False:
                print("This DVD does not exist.")    

            

        #List of DVD TITLES
        elif menu == 4:
            print("List of ALL DVD TITLES")
            i = 1
            for std in DVDstock: 
                print(i,":",std.getTitle())
                i = i+1

        #List of DVD DETAILS
        elif menu == 5:
            i = 0
            print("\n\nViewing list of DVDs..\n")
            while i < len(DVDstock):
                print("\nDVD: " ,i+1)
                print(DVDstock[i].printDVD() + "\n")
                i += 1



#ADMIN MENU       
def choice_2():
    DVDstock = DVDLinkedlist.SLinkedList()
    DVDstock = []
    try:
        data = open("DVDList.cvs")
        for line in data:
            columns = line.split(',')
            titlenew = columns [0]
            star1new = columns [1]
            star2new = columns [2]
            producernew = columns [3]
            directornew = columns [4]
            compnew = columns [5]
            nonew = int(columns [6])

            info = dvdType(titlenew, star1new, star2new, producernew, directornew, compnew, nonew)
            DVDstock.append(info)

    except Exception as e:
        print(e)
            
    finally:
        data.close()
        print()

    customer = []
    try:
        data2 = open("DVDListOfCustomers.cvs")
        for line in data2:
            columns = line.split(',')
            fname = columns [0]
            lname = columns [1]
            accountNum = columns [2]

            info = customerType(fname, lname, accountNum, list)
            root = DVDBSTCustomer.NodeBST(info)
            customer.append(info)

    except Exception as e:
        print(e)
            
    finally:
        data.close()

    while True:
        print()
        print("Menu for Admin")
        print("[0] - RETURN TO MENU SELECTION")
        print("[1] - ADD Customer")
        print("[2] - SEARCH for Customer")
        print("[3] - VIEW ALL Customer details")
        print("[4] - UPDATE Customer details")
        print("[5] - ADD DVD")
        print("[6] - SEARCH DVD")
        print("[7] - VIEW ALL DVDs")
        print("[8] - UPDATE DVD details")
        print("[9] - REMOVE DVD details")

        try:
           menu = int(input("Put in the value based on the given options>> "))
        except ValueError:
            print("Please enter a valid value in the given menu")
        if menu == 0:
            print("You have exited the ADMIN menu")
            return main()
        
        elif menu == 1:
            fname = input("First Name: ")
            lname = input("Last Name: ")
            accountNum = int(input("Account Number:"))
            list = []
            newCustomer = customerType(fname, lname, accountNum, list)
            root.insert(newCustomer)

        
        elif menu == 2:
            search_customer()
        
        elif menu == 3:
            view_customer()
        
        elif menu == 4:
            update_customer()
        
        elif menu == 5:
            add_DVD()
        
        elif menu == 6:
            search_DVD()
        
        elif menu == 7:
            view_DVD()
        
        elif menu == 8:
            update_DVD()
        
        elif menu == 9:
            remove_DVD()



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



main()
