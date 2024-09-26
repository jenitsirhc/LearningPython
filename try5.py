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
        print("[7] - PRINT PATIENT BILL")

        try:
            choice = int(input("\nPlace your choice here: "))
        except ValueError:
            print(">>Please enter a valid value in the given options.\n")
            continue

        if choice == 0: #exit
            print(">>Program Terminated.")
            exit()

        elif choice == 1: #view patients
            i = 0
            print("\n\nViewing list of patients..\n")
            if i == len(patients):
                print("No patients found.\n")
            else:
                while i < len(patients):
                    print("\nPatient " + str(i+1))
                    print(patients[i].displayName(), patients[i].displayPatients(), patients[i].displayDates() + "\n")
                    i += 1
            return main()
               
        elif choice == 2: #view doctors
            i = 0
            print("\n\nViewing list of doctors..\n")
            if i == len(doctors):
                print("No doctors found.\n")
            else:
                while i < len(doctors):
                    print("\nDoctor " + str(i+1) + ":")
                    print(doctors[i].displayName(), doctors[i].displaySpecialty() + "\n")
                    i += 1
            return main()

        elif choice == 3: #add patients
            print("Adding a new patient.. ")
            print("\nPlease input the new patient's particulars below.")
            try:
                p1 = PatientType(input("First Name: "), input("Last Name: "), input("PatientID: "), int(input("Age:")), input("Physician Name: "), input("Birth date: "), input("Admission Date: "), input("Discharge Date: "))
            except ValueError:
                print(">>Please enter a valid answer and try again.\n")
                continue
            
            patients.append(p1)
            print("\nPatient has been added.")
            return main()
            
        elif choice == 4: #add doctors
            print("Adding a new doctor.. ")
            print("\nPlease input the new doctor's particulars below.")
            try:
                p2 = DoctorType(input("First Name: "), input("Last Name: "), input("Specialty: "))
            except ValueError:
                print(">>Please enter a valid answer and try again.\n")
                continue

            doctors.append(p2)
            print("\nDoctor has been added.")
            return main()
            
        elif choice == 5: #delete patients
            i = 0
            if i == len(patients):
                print("No patients found to be deleted.")
            else:
                print("\n\nList of patients:\n")
                while i < len(patients):
                    print("Patient " + str(i+1))
                    print(patients[i].displayName(), patients[i].displayPatients(), patients[i].displayDates() + "\n\n")
                    i += 1
                try:
                    choice = int(input("Which patient would you like to remove?: "))
                except ValueError:
                    print(">>Please enter a valid value in the given options. Please try again.\n")
                    continue

                if choice > 0 and choice <= len(patients):
                    print("\nPatient " + str(choice))
                    print(patients[choice-1].displayName(), patients[choice-1].displayPatients() + "\n")
                    confirm = input("Are you sure? (Y/N): ")
                    if confirm == "Y" or confirm == "y":
                        patients.pop(choice-1)
                        print("Patient has been successfully deleted.")
                        return main()

                    elif confirm == "N" or confirm == "n":
                        return
                    
                    else:
                        print("Please enter a valid value in the given options.")
                else:
                    print("Please enter between 1 to " + str(len(patients)) + ".")

            return main()
            
        elif choice == 6: #delete doctors
            i = 0
            if i == len(doctors):
                print("No doctors found to be deleted.")
            else:
                print("\n\nList of doctors:\n")
                while i < len(doctors):
                    print("Doctor " + str(i+1))
                    print(doctors[i].displayName(), doctors[i].displaySpecialty() + "\n\n")
                    i += 1
                try:
                    choice = int(input("Which doctors would you like to remove?: "))
                except ValueError:
                    print(">>Please enter a valid value in the given options. Please try again.\n")
                    continue

                if choice > 0 and choice <= len(doctors):                    
                    print("\Doctor " + str(choice))
                    print(doctors[choice-1].displayName(), doctors[choice-1].displaySpecialty() + "\n")
                    confirm = input("Are you sure? (Y/N): ")
                    if confirm == "Y" or confirm == "y":
                        doctors.pop(choice-1)
                        print("Doctor has been successfully deleted.")
                        return main()

                    elif confirm == "N" or confirm == "n":
                        return
                    
                    else:
                        print("Please enter a valid value in the given options.")
                else:
                    print("Please enter between 1 to " + str(len(doctors)) + ".")

            return main()
        
        elif choice == 7: #Print Patient Bill
            print("Hi")

        else:
            print("\t\t\t> Please choose between 0 - 6 only.\n")

#Person Class
class PersonType():
    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName
       
    def getfName(self):
        return self.fName
    
    def setfName(self, fName):
        self.fName = fName
     
    def getlName(self):
        return self.lName

    def setlName(self, lName):
        self.lName = lName


    def displayName(self):
        return f"First Name: {self.fName}\nLast Name: {self.lName}"

#Date Class
class DateType:
    def __init__(self, birthDate, admissionDate, dischargeDate):
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
    
    def displayDates(self):
        return f"\nBirth Date: {self.birthDate} \nAdmission Date: {self.admissionDate}\nDischarge Date: {self.dischargeDate}"

#Patient Class
class PatientType(PersonType, DateType):
    def __init__(self, fName, lName, patientID, age, physicianName, birthDate, admissionDate, dischargeDate):
        PersonType.__init__(self, fName, lName)
        DateType.__init__(self, birthDate, admissionDate, dischargeDate)
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
    
    def displayPatients(self):
        return f"\nPatientID: {self.patientID} \nAge: {self.age} \nPhysician's Name: {self.physicianName}"
        

#Doctor Class
class DoctorType(PersonType):
    def __init__(self, fName, lName, specialty):
        PersonType._init_(self, fName, lName)
        self.specialty = specialty
    
    def setSpecialty(self):
        return self.specialty
    
    def getSpecialty(self, specialty):
        self.specialty = specialty
    
    def displaySpecialty(self):
        return f"\nSpecialty: {self.specialty}"




patients = []
doctors = []
main()
