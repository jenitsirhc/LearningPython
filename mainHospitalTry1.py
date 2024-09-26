# Gatuz, Jna ; PSB202IT
""" a. Create a personType class with first name and last name as data menbers. Add appropriate
constructors and member functions to initialize, access, and manipulate the data members.

Design the class doctorType, inherited from the class personType, with an additional data member
to store a doctor’s speciality. Add appropriate constructors and member functions to initialize,
access, and manipulate the data members.

b. Design the class billType with data members to store a patient’s ID and a patient’s hospital
charges, such as pharmacy charges for medicine, doctor’s fee, and room charges. Add appropriate
constructors and member functions to initialize, access, and manipulate the data members.

c. Design the class patientType, inherited from the class personType, with additional data members
to store a patient’s ID, age, date of birth, attending physician’s name, the date when the patient was
admitted in the hospital, and the date when the patient was discharged from the hospital. 

(Use the class dateType to store the date of birth, admit date, discharge date, and the class doctorType to
store the attending physician’s name.) Add appropriate constructors and member functions to
initialize, access, and manipulate the data members.
Write a program to test your classes."""

patients = []
doctors = []


#Main Menu
def main():

    while True:
        print("\n\t\t<<<" + "-" * 37 + "MAIN MENU" + "-" * 37 + ">>>")
        print("\t\t\t\t[0] - EXIT")
        print("\t\t\t\t[1] - VIEW PATIENTS")
        print("\t\t\t\t[2] - VIEW DOCTORS")
        print("\t\t\t\t[3] - ADD PATIENTS")
        print("\t\t\t\t[4] - ADD DOCTORS")
        print("\t\t\t\t[5] - DELETE PATIENTS")
        print("\t\t\t\t[6] - DELETE DOCTORS")
        print("\t\t-" + "-" * 88)

        try:
            choice = int(input("\t\tPlace your choice here: "))
        except ValueError:
            print("\t\t\t> Please enter a valid value in the given options.\n")
            continue

        if choice == 0:
            print("> Program Terminated.")
            exit()

        elif choice == 1:
            print("hi1")
        elif choice == 2:
            print("hi2")
        elif choice == 3:
            print("hi3")
        elif choice == 4:
            print("hi4")
        elif choice == 5:
            print("hi5")
        elif choice == 6:
            print("hi6")
        else:
            print("\t\t\t> Please choose between 0 - 6 only.\n")
            

#Person Class
class PersonType():
    def __init__(self):
        self.fName = input("First Name: ")
        self.lName = input("Last Name: ")
    
    def setNameInput(self, fName, lName):
        self.fName = fName
        self.lName = lName

    def displayName(self):
        return f"First Name: {self.fName}\nLast Name: {self.lName}"

#Doctor Class
class DoctorType(PersonType):
    def __init__(self):
        PersonType.__init__(self)
        self.specialty = input("Specialty: ")
    
    def setSpecialty(self, specialty):
        self.specialty = specialty
    
    def displaySpecialty(self):
        return f"\nSpecialty: {self.specialty}"

p1 = DoctorType()

print(p1.displayName(), p1.displaySpecialty())


#Patient Class
class PatientType(PersonType):
    def __init__(self, fname, lname, patientID, age, physicianName):
        PersonType.__init__(self, fname, lname)
        self.patientID = patientID
        self.age = age
        self.physicianName = physicianName
    
    def getPatientID(self):
        return self.patientID

    def getAge(self):
        return self.age
    
    def getPhysicianName(self):
        return self.physicianName
    
    def setPatientID(self, patientID):
        self.patientID = patientID

    def setAge(self, age):
        self.age = age
    
    def setPhysicianName(self, physicianName):
        self.physicianName = physicianName
    
    def printPatientDetails(self):
        return f"PatientID: {self.patientID} \n Age: {self.age} \n Physician's Name: {self.physicianName}"


#Date Class
class dateType(DoctorType):
    def __init__(self, birthDate, admissionDate, dischargeDate, physicianName):
        PatientType.__init__(self, physicianName)
        self.birthDate = birthDate
        self.admissionDate = admissionDate
        self.dischargeDate = dischargeDate

    def getBirthDate(self):
        return self.birthDate
    
    def getAdmissionDate(self):
        return self.admissionDate
    
    def getDischargeDate(self):
        return self.dischargeDate
    
    def setBirthDate(self, birthDate):
        self.birthDate = birthDate

    def setAdmissionDate(self, admissionDate):
        self.admissionDate = admissionDate
    
    def setDischargeDate(self, dischargeDate):
        self.dischargeDate = dischargeDate
    
    def printDate(self):
        return f"Birthdate: {self.birthDate} \n Admission Date: {self.admissionDate} \n Discharge Date: {self.dischargeDate} "


#Bill Class
class BillType:
    def __init__(self, patientID2, pharmacyCharges, docFee, roomCharges):
        self.patientID2 = patientID2
        self.pharmacyCharges = pharmacyCharges
        self.docFee = docFee
        self.roomCharges = roomCharges
        self.totalVal = 0

    def getPatientID2(self):
        return self.patientID2

    def getPharmacyCharges(self):
        return self.pharmacyCharges

    def getDocFee(self):
        return self.docFee
    
    def getRoomCharges(self):
        return self.roomCharges
    
    def __add__(self):
        self.totalVal = self.docFee + self.pharmacyCharges + self.roomCharges
        return self.totalVal
    
    def setPatientID2(self, patientID2):
        self.patientID2 = patientID2

    def setPharmacyCharges(self, pharmacyCharges):
        self.pharmacyCharges = pharmacyCharges

    def setDocFee(self, docFee):
        self.docFee = docFee
    
    def setRoomCharges(self, roomCharges):
        self.roomCharges = roomCharges

    def displayBill(self):
        return f"Bill for {self.patientID2} \n Doctor Fee: {self.docFee} \n Pharmacy Charges: {self.pharmacyCharges} \n Room Charges: {self.roomCharges} \n Total Cost: {self.__add__()}"


#Appending Stuff
p1 = DoctorType()
patients.append(p1)
print(p1.displayName(), p1.displaySpecialty)

main()

