class Employee: 
    
    def __init__(Self, Name = "", Hours_Worked = 0, Rate_of_Pay = 0):
        
        Self.__Name = Name
        Self.__Hours_Worked = Hours_Worked
        Self.__Rate_of_Pay = Rate_of_Pay
        
    def __str__(Self):
        
        Result = f"Name: {Self.__Name}\nHours: {Self.__Hours_Worked}" +\
                 f" Rate: ${Self.__Rate_of_Pay:.2f} Gross Pay: ${Self.Calc_Gross_Pay:.2f}"

        return Result
    
    def Get_Name(Self):
        
        return Self.__Name
    
    def Get_Hours_Worked(Self):
        
        return Self.__Hours_Worked
    
    def Get_Rate_of_Pay(Self):
        
        return Self.__Rate_of_Pay
    
    def Set_Name(Self, Name):
        
        Self.__Name = Name 
        
    def Set_Hours_Worked(Self, Hours_Worked): 
        
        Self.__Hours_Worked = Hours_Worked  
    
    def Set_Rate_of_Pay(Self, Rate_of_Pay): 
        
        Self.__Rate_of_Pay = Rate_of_Pay
        
    def Add_Hours_Worked(Self, Additional_Hours):
        
        Self.__Hours_Worked +- Additional_Hours
        
    def Calc_Gross_Pay(Self):
        
        return Self.__Hours_Worked * Self.__Rate_of_Pay