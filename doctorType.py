#Person Class
class PersonType():
    def _init_(self):
        self.fName = input("First Name: ")
        self.lName = input("Last Name: ")

    def setFName(self, fName):
        self.fName = fName
     
    def getFName(self):
        return self.fName
           
    def setLName(self, lName):
        self.lName = lName
        
    def getLName(self):
        return self.lName

#Doctor Class
class DoctorType(PersonType):
    def _init_(self):
        PersonType._init_(self)
        self.specialty = input("Specialty: ")
    
    def setSpecialty(self, specialty):
        self.specialty = specialty

    def getSpecialty(self):
        return self.specialty
        
    def displayDoctor(self):
        return f"\n\nFirst Name: {PersonType.getFName(self)}\nLast Name: {PersonType.getLName(self)}\nSpecialty: {self.specialty}"


#Patient Class
class PatientType(PersonType):
    def _init_(self):
        PersonType._init_(self)
        self.patientID = int(input("Patient ID: "))
        self.age = int(input("Age: "))
        self.physicianName = input("Physician Name: ")

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
    
    def displayPatient(self):
        return f"\n\nFirst Name: {PersonType.getFName(PersonType)}\nLast Name: {PersonType.getLName(PersonType)}\nPatientID: {self.patientID}\nAge: {self.age}\nPhysician's Name: {self.physicianName}"

p1 = DoctorType()
print(p1.displayDoctor())

p2 = PatientType()
print(p2.displayPatient())