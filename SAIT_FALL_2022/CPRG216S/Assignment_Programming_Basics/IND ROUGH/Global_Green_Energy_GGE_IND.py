print("Welcome to Global Energy Bill Calculator!")
print("")

A_Number = int(input("Enter Account Number: "))
Mon = int(input("Enter the Current Month (ie, January, Enter 1): "))
E_Plan = str(input("Enter Current Electricity Plan (EFIR or EFLR): ").upper())
E_Used = float(input("Enter the Amount of Electricity Used (in KWH): "))
TNG_Plan = str(input("Enter Current Natural Gas Plan (GFIR or GFLR): ").upper())
ANG_Used = float(input("Enter the Amount of Natural Gas Used (in GJ): "))
Province = str(input("Enter Your Resident Province (ie; AB): ").upper())

FP = 120.62
FP2 = 1.32
CON = 0.01
Tax = 0.05

if E_Plan == "EFIR":
    if E_Used < 1000:

        Energy = float(E_Used * 8.36 * CON + FP)
        
    else: 

        Energy = float((E_Used - 1000) * 9.41 * CON + 83.6 + FP)
     
elif E_Plan == "EFLR":

    Energy = float(E_Used * 9.11 * CON + FP)

if TNG_Plan == "GFIR":

    if ANG_Used < 950:

        PriceG = float(ANG_Used * 4.56 * CON + FP2)
        
    else: 

        PriceG = float((ANG_Used - 950) * 5.89 * CON + 43.32 + FP2)

elif TNG_Plan == "GFLR": 

    PriceG = float(ANG_Used * 3.93 * CON + FP2)

if Province == "AB" + "BC" + "MB" + "NT" + "NU" + "QC" + "SK" + "YT": 

    Tax = 0.05

elif Province == "ON": 

    Tax = 0.13

elif Province == "NB" + "NL" + "NS" + "PE": 

    Tax = 0.15

TMB_Amount = (Energy + PriceG) + (Energy + PriceG) * Tax

print("")
print(f'''Thank You! 
Total Amount Due Now: ${round(TMB_Amount,2)}''')