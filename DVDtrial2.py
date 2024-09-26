import DVDLinkedlist
import DVDBSTCustomer
import DVDCustomerClass
import DVDclass


#USER OR ADMIN!
def main():
    print()
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


    listDVDs = []

    try:
        print()
        data = open("DVDListOfCustomers.cvs")

        for line in data:
            columns = line.split(',')
            fname = columns [0]
            lname = columns [1]
            accountNum = columns [2]

            info = DVDCustomerClass.customerType(fname, lname, accountNum, listDVDs)
            root = DVDBSTCustomer.NodeBST(info)
            root.insert(info)
            root.printTree()
    
    except Exception as e:
        print(e)
            
    finally:
        data.close()
    
    while True:
        print()
        print("SELECT FROM THE FOLLOWING OPTIONS:")
        print("[0] - EXIT Program")
        print("[1] - USER MENU")
        print("[2] - ADMIN MENU")
        print()
        try:
            menu = int(input("\nPut in the value based on the given options>> "))

        except ValueError:
            print("\nPlease enter a valid value in the given menu")
        
        if menu == 0:
            print("\nYou have exited the USER menu")
            return main()
        
        elif menu == 1:
            choice_1()
            break
        elif menu == 2:
            choice_2()
            break
        else:
            print("Please select from the given menu.")
            continue



#USER MENU
    def choice_1():
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
                    print("The DVD does not exist.")    

                

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
                newCustomer = DVDCustomerClass.customerType(fname, lname, accountNum, list)
                root.insert(newCustomer)

            
            elif menu == 2:
                search_customer()
            
            elif menu == 3:
                view_customer()
            
            elif menu == 4:
                update_customer()
            
            #elif menu == 5:
                #add_DVD()
            
            #elif menu == 6:
                #search_DVD()
            
            elif menu == 7:
                view_DVD()
            
            #elif menu == 8:
                #update_DVD()
            
            #elif menu == 9:
                #remove_DVD()
    
    def search_customer(Customer_x):
        root.searchBST(Customer_x)

    def view_customer():
        Listofcustomer = root.inorderTraversal(root)

        for item in Listofcustomer:
            print()
            print(item)
            print()
    
    def update_customer(accountNum):
        print()
        print("What do you want to update?")
        print()
        print("[1] - First Name")
        print("[2] - Last Name")

        listofcustomer = root.inorderTraversal(root)
        found = False
        for item in listofcustomer:
            if item.getAccountNum == accountNum:
                print("Data exists")
                found = True
                break
        
        if found == True:
            answer = int(input("PLace your choice here: "))
            if answer == 1:
                fn = input("First Name: ")
                item.setfName(fn)
            elif answer == 2:
                ln = input("Last Name: ")
                item.setlName(ln)
        else:
            print("This Account Number does not exist.")
            return


    #def add_DVD():
    #def search_DVD():
    def view_DVD():
        i = 0
        print("\n\nViewing list of DVDs..\n")
        while i < len(DVDstock):
            print("\nDVD: " ,i+1)
            print(DVDstock[i].printDVD() + "\n")
            i += 1

    #def update_DVD():
            

    #def remove_DVD():


main()
