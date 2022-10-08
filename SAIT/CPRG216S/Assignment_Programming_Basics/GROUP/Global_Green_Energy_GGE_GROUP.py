print("Welcome to Global Energy Bill Calculator! \n") # Welcome/Greets User

A_Number = int(input("Enter Account Number: ")) #Prompts User for Account Number (A_Number)
Mon = int(input("Enter the Month (ie, January, Enter 1): ")) #Prompts User for Month (Mon)
E_Plan = str(input("Enter Electricity Plan in (EFIR or EFLR): ").upper()) #Prompts User for Electricity Plan (E_Plan)
E_Used = float(input("Enter the Amount of Electricity Used (in KWH): ")) #Prompts User for Amount of Electricity Used Number (E_Used)
TNG_Plan = str(input("Enter Natural Gas Plan (GFIR or GFLR): ").upper()) #Prompts User for Natural Gas Plan (TNG_Plan)
ANG_Used = float(input("Enter the Amount of Natural Gas Used (in GJ): ")) #Prompts User for Amount of Natural Gas Used (ANG_Used)
Province = str(input("Enter Your Resident Province (ie; AB): ").upper()) #Prompts User for Resident Province (Province)

FP = 120.62 #Declare Variable For Fixed Month Rate
FP2 = 1.32 #Declare Variable For Fixed Gas Rate
CON = 0.01 #Declare Variable to Convert Cents to Full Dollars
Tax_Rate = Tax = 0.05

#Calculates Energy Used Based off of Energy Plan Chosen and Amount Used
if E_Plan == "EFIR":
    if E_Used < 1000:

        Energy = float(E_Used * 8.36 * CON + FP)
        
    else: 

        Energy = float((E_Used - 1000) * 9.41 * CON + 83.6 + FP)
     
elif E_Plan == "EFLR":

    Energy = float(E_Used * 9.11 * CON + FP)

#Calculates Gas Used Based off of Gas Plan Chosen and Amount Used
if TNG_Plan == "GFIR":

    if ANG_Used < 950:

        PriceG = float(ANG_Used * 4.56 * CON + FP2)
        
    else: 

        PriceG = float((ANG_Used - 950) * 5.89 * CON + 43.32 + FP2)

elif TNG_Plan == "GFLR": 

    PriceG = float(ANG_Used * 3.93 * CON + FP2)

#Declares and Stores Tax Rate Based off of the Users Inputed Province
if (Province == "AB" + "BC" + "MB" + "NT" + "NU" + "QC" + "SK" + "YT"): 

    Tax_Rate = 0.05

elif (Province == "ON"): 

    Tax_Rate = 0.13

elif (Province == "NB" + "NL" + "NS" + "PE"): 

    Tax_Rate = 0.15

#Calculates the Total Cost By Combining All The Collected Data (Energy, PriceG and Tax Rate)
TMB_Amount = (Energy + PriceG) + (Energy + PriceG) * Tax_Rate 

#Be Polite and Thank the User For Using the Program
print(f'''\nThank You! 
Total Amount Due Now: ${round(TMB_Amount,2)}''') # Display Total Cost to User