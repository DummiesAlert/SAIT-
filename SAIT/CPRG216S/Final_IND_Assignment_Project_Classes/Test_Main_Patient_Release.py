import Test_Patient_Class 

def enterPatientInfo():
    
    ID = str(input("Enter Patient ID: "))
    Name = str(input("Enter Patient Name: "))
    Diagnosis = str(input("Enter Patient Diagnosis: "))
    Gender = str(input("Enter Patient Gender: "))
    Age = str(input("Enter Patient Age: "))
    Info = Test_Patient_Class.Patient(ID, Name, Diagnosis, Gender, Age)
    return Info

def readPatientsFile():
    
    Patient_List = []
    Patient_File = open(r"patients.txt")
    
    for Patient_Line in Patient_File: 
        
        Pat_Info = Patient_Line.rstrip().split("_")
        Pat = Test_Patient_Class.Patient(Pat_Info[0], Pat_Info[1], Pat_Info[2], Pat_Info[3], Pat_Info[4]) 
        Patient_List.append(Pat)
    
    Patient_File.close()
    return Patient_List 

def searchPatientById():
    
    User_ID = str(input("Enter the Patient ID: "))
    
    for ID1 in Patient_List:
        
        if ID1.Get_ID(User_ID) == True: 
            
            Pat_Info = ID1
            break
        else: 
            Pat_Info = " "
            
    if Pat_Info != " ":
        
        print(Pat_Info)
        return Pat_Info
    
    else: 
        
        print(f"Patient With ID {User_ID} NOT in the Patient File!")
        
def editPatientInfo():
    
    New_Patient = searchPatientById()
    
    for New in Patient_List: 
        
        if New.ID == New_Patient.ID: 
            
            New.Name = str(input("Enter NEW Name: "))
            New.Diagnosis = str(input("Enter NEW Diagnsis: "))
            New.Gender = str(input("Enter NEW Gender: "))
            New.Age = str(input("Enter NEW Age: "))
    
def displayPatientList(): 
    
    for N_Pat1 in Patient_List: 
        
        print(N_Pat1)
        
def writePatientsListToFile(Patient_List):
    
    Patient_File = open(r"patients.txt", "w")
    
    for ID2 in Patient_List:
        
        Patient_Line = Test_Patient_Class.Patient.formatPatientInfo(ID2)
        Patient_File.write(Patient_Line)
    
    Patient_File.close()
    
def addPatientToList(Patient_List):
    
    P_Info = enterPatientInfo()
    Patient_List.append(P_Info)
    
def main(): 
    
    Menu_Num = int(input("\nPatient Menu \n 0 - Return to Main Menu \n 1 - Display Patient's List \n 2 - Search for Patient by ID \n 3 - Add Patient \n 4 - Edit Patient Info \n Enter Option: "))
    
    while Menu_Num != 0:
        
        if Menu_Num == 1: 
            
            displayPatientList()
            
        elif Menu_Num == 2: 
            
            searchPatientById()
            
        elif Menu_Num == 3: 
            
            addPatientToList(Patient_List)
            writePatientsListToFile(Patient_List)
            
        elif Menu_Num == 4: 
            
            editPatientInfo()
            writePatientsListToFile(Patient_List)
            displayPatientList() 
        
        Menu_Num = int(input("\nPatient Menu \n 0 - Return to Main Menu \n 1 - Display Patient's List \n 2 - Search for Patient by ID \n 3 - Add Patient \n 4 - Edit Patient Info \n Enter Option: "))

if __name__ == "__main__":
    
    Patient_List = readPatientsFile()
    main()