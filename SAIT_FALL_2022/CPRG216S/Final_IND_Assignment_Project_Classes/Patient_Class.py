class Patient:
    
    def __init__(Self, ID, Name, Diagnosis, Gender, Age):
        
        Self.ID = ID 
        Self.Name = Name
        Self.Diagnosis = Diagnosis 
        Self.Gender = Gender
        Self.Age = Age
        
    def Set_Name(Self, Name):
        
        Self.Name = Name 
        
    def Set_Diagnosis(Self, Diagnosis):
        
        Self.Diagnosis = Diagnosis
        
    def Set_Gender(Self, Gender): 
        
        Self.Gender = Gender
        
    def Set_Age (Self, Age):
        
        Self.Age = Age
        
    def Get_ID(Self):
        
        return Self.ID
        
    def __str__(Self):
        
        return f"{Self.ID:>10s}{Self.Name:>10s}{Self.Diagnosis:>10s}{Self.Gender:>10s}{Self.Age:>5s}"
    
    def formatPatientInfo(Self):
        
        return f"{Self.ID}_{Self.Name}_{Self.Diagnosis}_{Self.Gender}_{Self.Age} \n"