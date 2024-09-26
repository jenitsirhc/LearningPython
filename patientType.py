#Design the class patientType, inherited from the class personType, with additional data members
#to store a patient’s ID, age, date of birth, attending physician’s name, the date when the patient was
#admitted in the hospital, and the date when the patient was discharged from the hospital. Add appropriate constructors and member functions to
#initialize, access, and manipulate the data members. 
import personType as PersonType

class PatientType(PersonType):
    def __init__(self, fname, lname, patientID, age):
        PersonType.__init__(self, fname, lname)
        self.patientID = patientID
        self.age = age
    
    def getPatientID(self):
        return self.patientID

    def getAge(self):
        return self.age
