def Add (num1, num2): 
    
    return num1 + num2 

def Sub (num1, num2): 
    
    return num1 - num2 

def Multi (num1, num2): 
    
    return num1 * num2 

def Divid (num1, num2): 
    
    return num1 / num2 

Operation = input("Enter the Operation (Add, Sub, Multi, Divid): ")
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

if Operation == 'Add':
    
    print(num1, "+", num2, "=", Add(num1, num2))
    
elif Operation == 'Sub':
    
    print(num1, "-", num2, "=", Sub(num1, num2))
    
elif Operation == 'Multi':
    
    print(num1, "*", num2, "=", Multi(num1, num2))
    
elif Operation == 'Divid':
    
    print(num1, "/", num2, "=", Divid(num1, num2))