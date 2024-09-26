#b. Design the class billType with data members to store a patient’s ID and a patient’s hospital
#charges, such as pharmacy charges for medicine, doctor’s fee, and room charges. Add appropriate
#constructors and member functions to initialize, access, and manipulate the data members. 

class BillType:
    def __init__(self, patientID, pharmacyCharges, docFee, roomCharges, totalHospitalBill):
        self.patientID = patientID
        self.pharmacyCharges = pharmacyCharges
        self.docFee = docFee
        self.roomCharges = roomCharges
        self.totalHospitalBill = totalHospitalBill

    def getID(self):
        return self.patientID

    def getPharmacyCharges(self):
        return self.pharmacyCharges

    def getDocFee(self):
        return self.docFee
    
    def getRoomCharges(self):
        return self.roomCharges
    
    def getTotalHospitalBill(self):
        return self.totalHospitalBill
    
    def setPharmacyCharges(self, pharmacyCharges):
        self.pharmacyCharges = pharmacyCharges

    def setDocFee(self, docFee):
        self.docFee = docFee
    
    def setRoomCharges(self, roomCharges):
        self.roomCharges = roomCharges
    
    def setTotalHospitalBill(self):
        return {self.pharmacyCharges} + {self.roomCharges} + {self.docFee}