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

        elif choice == 1: #view patients
            PatientType.printPatientDetails(patients)
            print("hi")
               
        elif choice == 2: #view doctors
          #  doctors = []
           # for i in doctors:
           #     print(doctors[i].displayName(), patients[i].displayDoctors())
           # return main()
           print("hi")

        elif choice == 3: #add patients
            print("Adding a patient..")
            #p1 = PatientType(input("\nFirst Name: "), input("Last Name: "), input("Age: "), input("Physician Name: ") )
            #patients.append(p1)

            print("Patient has been added.")
            return main()
            
        elif choice == 4: #add doctors
       #     p2 = DoctorType()
         #   doctors.append(p2)
            print("Doctor has been added.")
            return main()
            
        elif choice == 5: #delete patients
            return main()
            
        elif choice == 6: #delete doctors
            return main()
            
        else:
            print("> Please choose between 0 - 6 only.\n")

