import DVDclass
import DVDCustomerClass
import DVDBSTCustomer
import DVDLinkedlist
def main():

    DVD1=DVDclass.dvdType("JamesBond", "Ben", "Allison", "Steven", "Oliver", "Disney", 6)
    print(DVDclass)
    
    DVD1.printTitle()
    DVD1.updateStock(8)
   
    newcopies = DVD1.getNoOfDVDs()
    print("Number of copies: ", newcopies)

    
    listDVDs = []
    listDVDs.append('DVD1')
    listDVDs.append('DVD2')
    listDVDs.append('DVD3')

    Customer1 = DVDCustomerClass.customerType("John", "Smith", "abc123", listDVDs)
    Customer2 = DVDCustomerClass.customerType("Jane", "Doe", "otv123", listDVDs)
    Customer3 = DVDCustomerClass.customerType("Lily", "Pichu", "otv103", listDVDs)

    DVDlistofCus1 = Customer1.getRentedDVDs()
    
    for item in DVDlistofCus1:
        print ("Item: ",item)
    
    Customer1.printCustomerDetails()
    data1 = Customer1.getAccountNum()
    data2 = Customer2.getAccountNum()
    data3 = Customer3.getAccountNum()

    root = DVDBSTCustomer.NodeBST(data1) 
    root.insert(data2)
    root.insert(data3)
    root.printTree()

    # File Reading

    DVDStock = []

    try:
        input_file1 = open("DVDList.txt")

        for line in input_file1:
            columns = line.split(',')
            titlenew = columns [0]
            star1new = columns [1]
            star2new = columns [2]
            producernew = columns [3]
            directornew = columns [4]
            compnew = columns [5]
            nonew = int(columns [6])

            DVD_x = DVDclass.dvdType(titlenew, star1new, star2new, producernew, directornew, compnew, nonew)
            DVDStock.append(DVD_x)

    except Exception as e:
        print(e)
        
    finally:
        input_file1.close()
    
    print("Test 1")
    print()
    for std in DVDStock:
        print()
        print("Records:")
        print()
        print(std)
    
    DVDstock1 = DVDLinkedlist.SLinkedList()
    DVDstock1.headval = DVDLinkedlist.Node(DVD1)
    e2 = DVDLinkedlist.Node(DVD_x)
    e3 = DVDLinkedlist.Node(DVD1)

    DVDstock1.headval.nextval = e2
    e2.nextval = e3

    DVDstock1.listprint()

    

main()
