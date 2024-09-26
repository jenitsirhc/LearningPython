#Person Class

def main():
    patients = []
    while True:
        print("\n<<< " + "MAIN MENU " +" >>>")
        print("[0] - EXIT")
        print("[1] - VIEW PATIENTS")
        print("[2] - VIEW DOCTORS")
        print("[3] - ADD PATIENTS")
        print("[4] - ADD DOCTORS")
        print("[5] - DELETE PATIENTS")
        print("[6] - DELETE DOCTORS")

        try:
            choice = int(input("\nPlace your choice here: "))
        except ValueError:
            print("> Please enter a valid value in the given options.\n")
            continue

        if choice == 0: #exit
            print("> Program Terminated.")
            exit()

        elif choice == 1:
            p1 = (PatientType())
            patients.append(p1)
            print(p1.displayName(), p1.printPatientDetails())
        
               
        elif choice == 2: #view doctors
            doctors = []
            for i in doctors:
                print(doctors[i].displayName(), patients[i].displayDoctors())
            return main()

        elif choice == 3: #add patients
            p1 = PatientType()
            patients.append(p1)
            print("Patient has been added.")
            return main()
            
        elif choice == 4: #add doctors
            p2 = DoctorType()
            doctors.append(p2)
            print("Doctor has been added.")
            return main()
            
        elif choice == 5: #delete patients
            return main()
            
        elif choice == 6: #delete doctors
            return main()
            
        else:
            print("> Please choose between 0 - 6 only.\n")

class PersonType():
    def __init__(self):
        self.fName = input("First Name: ")
        self.lName = input("Last Name: ")
        pass
    
    def setfName(self, fName):
        self.fName = fName
    
    def setlName(self, lName):
        self.lName = lName

    def displayName(self):
        return f"First Name: {self.fName}\nLast Name: {self.lName}"

#Patient Class
class PatientType(PersonType):
    def __init__(self):
        PersonType.__init__(self)
        self.patientID = input("Patient ID: ")
        self.age = int(input("Age: "))
        self.physicianName = input("Physician's Name: ")
    
    def setPatientID(self, patientID):
        self.patientID = patientID

    def getPatientID(self):
        return self.patientID
    
    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age
    
    def setPhysicianName(self, physicianName):
        self.physicianName = physicianName

    def getPhysicianName(self):
        return self.physicianName
  
    def printPatientDetails(self):
        return f"\nPatientID: {self.patientID} \nAge: {self.age} \nPhysician's Name: {self.physicianName}"

#Doctor Class
class DoctorType(PersonType):
    def __init__(self):
        PersonType.__init__(self)
        self.specialty = input("Specialty: ")
    
    def setSpecialty(self, specialty):
        self.specialty = specialty
    
    def displaySpecialty(self):
        return f"\nSpecialty: {self.specialty}"




main()
