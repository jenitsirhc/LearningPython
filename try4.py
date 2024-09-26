#Person Class

patients = [["Jane", "Doe", "A100", "19", "Barbara"]]
doctors = [[]]

def main():
    

    while True:
        print("\n<<< " + "   WELCOME TO THE MAIN MENU!  " +" >>>")
        print("<<< " + "PLEASE SELECT AN OPTION BELOW " +" >>>")
        print("[0] - EXIT")
        print("[1] - VIEW PATIENTS")
        print("[2] - VIEW DOCTORS")
        print("[3] - ADD PATIENT")
        print("[4] - ADD DOCTOR")
        print("[5] - DELETE PATIENTS")
        print("[6] - DELETE DOCTORS")

        try:
            choice = int(input("\nPlace your choice here: "))
        except ValueError:
            print(">>Please enter a valid value in the given options.\n")
            continue

        if choice == 0: #exit
            print("\n>>Program Terminated.")
            exit()

        elif choice == 1: #view patients
            PatientType.printPatientDetails(patients)
        
               
        elif choice == 2: #view doctors
            DoctorType.displaySpecialty(doctors)
            

        elif choice == 3: #add patients
            print("adding a patient..")
            p1 = PatientType(input("\nFirst Name: "), input("Last Name: "), input("Patient ID: "), int(input("Age: ")), input("Physician Name: "))
            patients.append(p1)
            print("Patient has been added.")
            pass
            
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
            print(">> Please choose between 0 - 6 only.\n")

class PersonType():
    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName
    
    def setfName(self, fName):
        self.fName = fName
    
    def setlName(self, lName):
        self.lName = lName
    
    def getfName(self):
        return self.fName
    
    def getlName(self):
        return self.lName

    def displayName(self):
        print(f"First Name: {self.fName}\nLast Name: {self.lName}")

#Patient Class
class PatientType(PersonType):
    def __init__(self, fName, lName, patientID, age, physicianName):
        PersonType.__init__(self, fName, lName)
        self.patientID = patientID
        self.age = age
        self.physicianName = physicianName
    
    def getPatientID(self):
        return self.patientID

    def setPatientID(self, patientID):
        self.patientID = patientID

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def getPhysicianName(self):
        return self.physicianName

    def setPhysicianName(self, physicianName):
        self.physicianName = physicianName
  
    def printPatientDetails(self):
        print(f"\nPatientID: {self.patientID} \nAge: {self.age} \nPhysician's Name: {self.physicianName}")

#Doctor Class
class DoctorType(PersonType):
    def __init__(self, fName, lName, specialty):
        PersonType.__init__(self, fName, lName)
        self.specialty = specialty
    
    def getSpecialty(self):
        return self.specialty

    def setSpecialty(self, specialty):
        self.specialty = specialty
    
    
    def displaySpecialty(self):
        print(f"\nSpecialty: {self.specialty}")

main()
