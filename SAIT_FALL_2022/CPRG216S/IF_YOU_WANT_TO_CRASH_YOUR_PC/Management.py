import Classes

def main():
    mainmenu_number= int(input("Main Menu\n0-Close application\n1-doctors\n2-Facilities\n3-Laboratories\n4-patients\nEnter option: "))
    while mainmenu_number != 0:
        if mainmenu_number == 1:
            doctor_menu()
        if mainmenu_number == 2:
            facilities_menu() 
        if mainmenu_number == 3:
            pass
        if mainmenu_number == 4:
            patient_main()

#Doctor Menu
def doctor_menu():
    docmenu_number= int(input("Doctor's Menu\n0-Return to main Menu\n1-Display Doctors List\n2-Search for doctor by ID\n3-Search for doctor by name\n4-Add doctor\n5- Edit doctor info\nEnter option: "))
    while docmenu_number != "":
        if docmenu_number == 0:
            main()
        elif docmenu_number == 1:
            displaydoctorList()

        elif docmenu_number == 2:
            searchdoctorByld()
            
        elif docmenu_number == 3:
            searchdoctorbyname()
        
        elif docmenu_number ==4:
            addPatientToList(doctor_list)
            writedoctorListToFile(doctor_list)
            
        elif docmenu_number == 5:
            editPatientInfo()
            writedoctorListToFile(doctor_list)
            displaydoctorList()
            
        docmenu_number= int(input("Doctor's Menu\n0-Return to main Menu\n1-Display Doctors List\n2-Search for doctor by ID\n3-Search for doctor by name\n4-Add doctor\n5- Edit doctor info\nEnter option: "))

#Facilities Menu

def facilities_menu():
    
    facmenu_num = int(input("\nFacilities Menu \n 0 - Return to Main Menu \n 1 - Display Facilities List \n 2 - Add Facility \nEnter option: "))
    
    while facmenu_num != " ": 
        
        if facmenu_num == 0:
            
            main()
            
        elif facmenu_num == 1: 
            
            displayFacilitiesList()
            
        elif facmenu_num == 2: 
            
            addFacilityToList()
            writeFacilitiesListToFile()
            
        facmenu_num = int(input("\nFacilities Menu \n 0 - Return to Main Menu \n 1 - Display Facilities List \n 2 - Add Facility \nEnter option: "))
    
#Doctor Starts Here
def readdoctorFile():
    doc_list=[]
    D_file= open(r"project/doctors.txt")
    for D_line in D_file:
        D_items = D_line.rstrip().split("_")
        object_doctor= Classes.Doctor(D_items[0], D_items[1], D_items[2], D_items[3], D_items[4],D_items[5])
        doc_list.append(object_doctor)
    D_file.close()
    return doc_list

def displaydoctorList():
    for d in doctor_list:
        print (d)

def searchdoctorByld():

    id_user = str(input("enter ID plz: "))
    for d_object in doctor_list:
        if d_object.get_id(id_user) == True:
            doctor_info=d_object
            break
        else :
            doctor_info= " "
        
    if doctor_info != " " :
        print (doctor_info)
        return doctor_info
    else:
        print (f"patient with ID {id_user} not in the patient file")

def searchdoctorbyname():

    name_user = str(input("enter name plz: "))
    for d_object in doctor_list:
        if d_object.get_name(name_user) == True:
            doctor_info=d_object
            break
        else :
            doctor_info= " "
        
    if doctor_info != " " :
        print (doctor_info)
        return doctor_info
    else:
        print (f"patient with name {name_user} not in the patient file")


def enterdoctorInfo():
    id = str(input("Enter Dr ID plz: "))
    name = str(input("Enter Dr name plz: "))
    specialty = str(input("Enter Dr Diagnsis plz: "))
    schedule = str(input("Enter Dr Gender plz: "))
    qualification= str(input("Enter Dr age plz: "))
    room_number = str(input("Enter Dr room number:"))
    new_info=Classes.Doctor(id,name,specialty,schedule,qualification,room_number)
    return new_info

def addPatientToList(doctor_list):
    d_new_info = enterdoctorInfo()
    doctor_list.append(d_new_info)

def writedoctorListToFile(dcotor_list):
    d_file=open(r"doctors.txt","w")
    for object in doctor_list:
        d_line= Classes.Doctor.formatPatientInfo(object)
        d_file.write(d_line)
    d_file.close()

def editPatientInfo():
    object_patient=searchdoctorByld()
    for D in doctor_list:
        if D.id == object_patient.id:
            D.name = input("Enter name plz: ")
            D.specialty = input("Enter specialty plz: ")
            D.schedule = input("Enter schedule plz: ")
            D.qualification = input("Enter qualification plz: ")
            D.age = input("Enter age plz: ")

def readPatientsFile():
    patient_list=[]
    P_file= open(r"project/patients.txt")
    for P_line in P_file:
        P_items = P_line.rstrip().split("_")
        object_patient= Classes.Patient(P_items[0], P_items[1], P_items[2], P_items[3], P_items[4])
        patient_list.append(object_patient)
    P_file.close()
    return patient_list

def enterPatientInfo():
    id = str(input("Enter ID plz: "))
    name = str(input("Enter name plz: "))
    diagnosis = str(input("Enter Diagnsis plz: "))
    gender = str(input("Enter Gender plz: "))
    age = str(input("Enter age plz: "))
    new_info=Classes.Patient(id,name,diagnosis,gender,age)
    return new_info

def addPatientToList(patient_list):
    P_new_info = enterPatientInfo()
    patient_list.append(P_new_info)

def writePatientsListToFile(patient_list):
    P_file=open(r"project/patients.txt","w")
    for object in patient_list:
        P_line= Classes.Patient.formatPatientInfo(object)
        P_file.write(P_line)
    P_file.close()

def displayPatientList():
    for p in patient_list:
        print (p)

def searchPatientByld():

    id_user = str(input("enter ID plz: "))
    for p_object in patient_list:
        if p_object.get_id(id_user) == True:
            patient_info=p_object
            break
        else :
            patient_info= " "
        
    if patient_info != " " :
        print (patient_info)
        return patient_info
    else:
        print (f"patient with ID {id_user} not in the patient file")

def editPatientInfo9(): 
    object_patient=searchPatientByld()
    for P in patient_list:
        if P.id == object_patient.id:
            P.name = input("Enter name plz: ")
            P.diagnosis = input("Enter Diagnsis plz: ")
            P.gender = input("Enter Gender plz: ")
            P.age = input("Enter age plz: ")


def patient_main():
    menu_number=int(input("Patient Menu\n0-Return to main Menu\n1-Display patient's List\n2-Search for patient by ID\n3-Add patient\n4-Edit patient info\nEnter option: "))
    while menu_number != "":
        if menu_number == 0:
            main()
        elif menu_number == 1:
            displayPatientList()
        elif menu_number == 2:
            searchPatientByld()
        elif menu_number == 3:
            addPatientToList(patient_list)
            writePatientsListToFile(patient_list)
        elif menu_number ==4:
            editPatientInfo9()
            writePatientsListToFile(patient_list)
            displayPatientList()
        
        menu_number=int(input("\n Patient Menu\n0-Return to main Menu\n1-Display patient's List\n2-Search for patient by ID\n3-Add patient\n4-Edit patient info\nEnter option: "))


#Faculty Starts Here: 

def addFacilityToList(): 
    
    F = str("Enter Facility Name: ")
    F = readFacilitiesFile()
    Facilities_list.append(F)

def readFacilitiesFile(): 
    
    Facilities_list=[]
    F_file= open(r"project/facilities.txt")
    
    for F_line in F_file:
        
        F_items = F_line.rstrip()
        object_Facilities = Classes.Facilities(Facilities_Name = F_items) #Because there is only one value
        Facilities_list.append(object_Facilities)
    F_file.close()
    
    return Facilities_list

def displayFacilitiesList():
    
    print("\n")
    
    for f in Facilities_list:
        
        print (f, end = " ")
        
def writeFacilitiesListToFile(): 
    
    f_file = open(r"project/facilities.txt","w")
    
    for f_object in Facilities_list:
        
        f_file.write(str((addFacilityToList())))
        
    f_file.close()

if __name__=="__main__":
    
    doctor_list = readdoctorFile()
    patient_list = readPatientsFile() 
    Facilities_list = readFacilitiesFile()
    main()