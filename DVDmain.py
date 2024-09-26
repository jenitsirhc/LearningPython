import DVDLinkedlist
import DVDclass
import DVDCustomerClass
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

            info = DVDclass.dvdType(titlenew, star1new, star2new, producernew, directornew, compnew, nonew)
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
                        print("Number of AVAILABLE copy/ies: ", n)

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

            info = DVDclass.dvdType(titlenew, star1new, star2new, producernew, directornew, compnew, nonew)
            DVDstock.append(info)

    except Exception as e:
        print(e)
            
    finally:
        data.close()
        print()

    customer = DVDLinkedlist.SLinkedList()
    customer = []
    try:
        data2 = open("DVDListOfCustomers.cvs")
        for line in data2:
            columns = line.split(',')
            fname = columns [0]
            lname = columns [1]
            accountNum = columns [2]

            info = DVDCustomerClass.customerType(fname, lname, accountNum)
            customer.append(info)

    except Exception as e:
        print(e)
            
    finally:
        data2.close()

    while True:
        print()
        print("Menu for Admin")
        print("[0] - RETURN TO MENU SELECTION")
        print("[1] - ADD Customer")
        print("[2] - SEARCH for Customer")
        print("[3] - VIEW ALL Customer details")
        print("[4] - ADD DVD")
        print("[5] - SEARCH DVD")
        print("[6] - VIEW ALL DVDs")
        print("[7] - REMOVE DVD details")

        try:
           menu = int(input("\nPut in the value based on the given options>> "))
        except ValueError:
            print("\nPlease enter a valid value in the given menu")
        if menu == 0:
            print("\nYou have exited the ADMIN menu")
            return main()
        
        elif menu == 1: #Add Customer
            fname = input("\nFirst Name: ")
            lname = input("\nLast Name: ")
            accountNum = input("\nAccount Number:")

            newCustomer = DVDCustomerClass.customerType(fname, lname, accountNum)
            customer.append(newCustomer)
            print()
            print("\nYou have successfully added a Customer")

        
        elif menu == 2: #Search Customer
            name = input("First Name of the customer: ")
            found = False
            for person in customer:
                if person.getfName() == name:
                    print("Customer found")
                    found = True

            if found == False:
                print("This Customer profile does not exist.")
                 
        elif menu == 3: #View Customers
            i = 0
            print("\n\nViewing list of Customers..\n")
            while i < len(customer):
                print("\nCustomer: " ,i+1)
                print(customer[i].printCustomerDetails() + "\n")
                i += 1

        
        elif menu == 4: #Add DVD
            title = input("Title: ")
            star1 = input("Star 1: ")
            star2 = input("Star 2: ")
            producer = input("Producer: ")
            director = input("Director: ")
            company = input("Company: ")
            noOfDVDs = int(input("Number of DVDs: "))
            newDVD = DVDclass.dvdType(title, star1, star2, producer, director, company, noOfDVDs)
            DVDstock.append(newDVD)
            print("You have successfully added a DVD to the library.")
        
        elif menu == 5:#Search DVD
            title = input("Enter the title over here: ")
            found = False
            for search in DVDstock:
                if search.getTitle() == title:
                    print("DVD found")
                    found = True

            if found == False:
                print("This DVD title does not exist.")
        
        elif menu == 6: #View DVDs
            i = 0
            print("\n\nViewing list of DVDs..\n")
            while i < len(DVDstock):
                print("\nDVD: " ,i+1)
                print(DVDstock[i].printDVD() + "\n")
                i += 1
                
            

        elif menu == 7: #Remove DVD
            i = 0
            print("\nList of DVDs:")
            while i < len(DVDstock):
                print("DVD: " +str(i+1))
                print(DVDstock[i].printDVD() + "\n" )
                i += 1
            try:
                choice = int(input("Which DVD would you like to remove? Input the number here: "))
            except ValueError:
                print(">>Please enter a valid value in the given options. Please try again.\n")
                continue

            if choice > 0 and choice <= len(DVDstock):
                print("\nDVD: " + str(choice))
                print(DVDstock[choice-1].printDVD() + "\n")
                confirm = input("Are you sure? (Y/N): ")
                if confirm == "Y" or confirm == "y":
                    DVDstock.pop(choice-1)
                    print("DVD has been successfully deleted.\n")


                elif confirm == "N" or confirm == "n":
                    return
                    
                else:
                    print("Please enter a valid value in the given options.\n")
            else:
                print("Please enter between 1 to " + str(len(DVDstock)) + ".")

                


main()
