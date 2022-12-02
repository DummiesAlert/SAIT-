print("Welcome to Circle Phones' Profit Calculator")
print("You can calculate the profit of the company according to a specific day or by a week or divide the week into Weekdays and Weekend.")
P_Days = int(input(f'''''
Enter:
    1 - For Specific Day
    2 - For the Week
    3 - For Week Business Days 
    4 - For Weekend Days
    0 - Exit
'''''))
Ap_Iphone = 120.45
An_Phone = 99.50
Ap_Tablet = 75.69
An_Tablet = 65.73
Win_Tablet = 51.49
Sum1 = Sum2 = Sum3 = Sum4 = Sum5 = 0 # Did this to Save Space and Easier For Me to Control the Variables as = 0
DayList = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
if P_Days == 1: 
    S_Day = str(input("Enter a Specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]: "))  
    print("For", S_Day.capitalize(), ": ")
    P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
    while P_Num != 0:  
        P_ValueNum = float(input("Enter Quantity Sold: "))
        if P_Num == 1:
            Sum1 = P_ValueNum * Ap_Iphone
        elif P_Num == 2:
            Sum2 = P_ValueNum * An_Phone
        elif P_Num == 3:
            Sum3 = P_ValueNum * Ap_Tablet
        elif P_Num == 4:
            Sum4 = P_ValueNum * An_Tablet
        elif P_Num == 5:
            Sum5 = P_ValueNum * Win_Tablet
        P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))    
    T_Sum = (Sum1 + Sum2 + Sum3 + Sum4 + Sum5)
    print("Your Total Profit for", S_Day,"is: ", round(T_Sum,2))
    if T_Sum <= 10000:
        print("We DIDNT Reach Our Goal for This Period. More Work is Needed.")
    else :
        print("You DID Well This Period! Keep up the Great Work!")     
elif P_Days == 2:
    print("For ",DayList[1], ": ")
    P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
    Sum1 = Sum2 = Sum3 = Sum4 = Sum5 = 0
    while P_Num != 0:
        P_ValueNum = float(input("Enter Quantity Sold: "))
        if P_Num == 1:
            Sum1 = P_ValueNum * Ap_Iphone
        elif P_Num == 2:
            Sum2 = P_ValueNum * An_Phone
        elif P_Num == 3:
            Sum3 = P_ValueNum * Ap_Tablet
        elif P_Num == 4:
            Sum4 = P_ValueNum * An_Tablet
        elif P_Num == 5:
            Sum5 = P_ValueNum * Win_Tablet
        P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))      
    T_Sum1 = (Sum1 + Sum2 + Sum3 + Sum4 + Sum5)   
    print("For ",DayList[2], ": ")       
    P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
    Sum1 = Sum2 = Sum3 = Sum4 = Sum5 = 0
    while P_Num != 0:
        P_ValueNum = float(input("Enter Quantity Sold: "))
        if P_Num == 1:
            Sum1 = P_ValueNum * Ap_Iphone
        elif P_Num == 2:
            Sum2 = P_ValueNum * An_Phone
        elif P_Num == 3:
            Sum3 = P_ValueNum * Ap_Tablet
        elif P_Num == 4:
            Sum4 = P_ValueNum * An_Tablet
        elif P_Num == 5:
            Sum5 = P_ValueNum * Win_Tablet 
        P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))               
    T_Sum2 = (Sum1 + Sum2 + Sum3 + Sum4 + Sum5)    
    print("For ",DayList[3], ": ")       
    P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
    Sum1 = Sum2 = Sum3 = Sum4 = Sum5 = 0
    while P_Num != 0:
        P_ValueNum = float(input("Enter Quantity Sold: "))
        if P_Num == 1:
            Sum1 = P_ValueNum * Ap_Iphone
        elif P_Num == 2:
            Sum2 = P_ValueNum * An_Phone
        elif P_Num == 3:
            Sum3 = P_ValueNum * Ap_Tablet
        elif P_Num == 4:
            Sum4 = P_ValueNum * An_Tablet
        elif P_Num == 5:
            Sum5 = P_ValueNum * Win_Tablet               
        P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
    T_Sum3 = (Sum1 + Sum2 + Sum3 + Sum4 + Sum5)  
    print("For ",DayList[4], ": ")      
    P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
    Sum1 = Sum2 = Sum3 = Sum4 = Sum5 = 0
    while P_Num != 0:
        P_ValueNum = float(input("Enter Quantity Sold: "))
        if P_Num == 1:
            Sum1 = P_ValueNum * Ap_Iphone
        elif P_Num == 2:
            Sum2 = P_ValueNum * An_Phone
        elif P_Num == 3:
            Sum3 = P_ValueNum * Ap_Tablet
        elif P_Num == 4:
            Sum4 = P_ValueNum * An_Tablet
        elif P_Num == 5:
            Sum5 = P_ValueNum * Win_Tablet               
        P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: ")) 
    T_Sum4 = (Sum1 + Sum2 + Sum3 + Sum4 + Sum5)                
    print("For ",DayList[5], ": ")        
    P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
    Sum1 = Sum2 = Sum3 = Sum4 = Sum5 = 0
    while P_Num != 0:
        P_ValueNum = float(input("Enter Quantity Sold: "))
        if P_Num == 1:
            Sum1 = P_ValueNum * Ap_Iphone
        elif P_Num == 2:
            Sum2 = P_ValueNum * An_Phone
        elif P_Num == 3:
            Sum3 = P_ValueNum * Ap_Tablet
        elif P_Num == 4:
            Sum4 = P_ValueNum * An_Tablet
        elif P_Num == 5:
            Sum5 = P_ValueNum * Win_Tablet                
        P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))           
    T_Sum5 = (Sum1 + Sum2 + Sum3 + Sum4 + Sum5)                
    print("For ",DayList[6], ": ")           
    P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
    Sum1 = Sum2 = Sum3 = Sum4 = Sum5 = 0
    while P_Num != 0:  
        P_ValueNum = float(input("Enter Quantity Sold: "))
        if P_Num == 1:
            Sum1 = P_ValueNum * Ap_Iphone
        elif P_Num == 2:
            Sum2 = P_ValueNum * An_Phone
        elif P_Num == 3:
            Sum3 = P_ValueNum * Ap_Tablet
        elif P_Num == 4:
            Sum4 = P_ValueNum * An_Tablet
        elif P_Num == 5:
            Sum5 = P_ValueNum * Win_Tablet                
        P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))        
    T_Sum6 = (Sum1 + Sum2 + Sum3 + Sum4 + Sum5)        
    print("For ",DayList[0], ": ")            
    P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
    Sum1 = Sum2 = Sum3 = Sum4 = Sum5 = 0
    while P_Num != 0:  
        P_ValueNum = float(input("Enter Quantity Sold: "))
        if P_Num == 1:
            Sum1 = P_ValueNum * Ap_Iphone
        elif P_Num == 2:
            Sum2 = P_ValueNum * An_Phone
        elif P_Num == 3:
            Sum3 = P_ValueNum * Ap_Tablet
        elif P_Num == 4:
            Sum4 = P_ValueNum * An_Tablet
        elif P_Num == 5:
            Sum5 = P_ValueNum * Win_Tablet                
        P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
    T_Sum = (Sum1 + Sum2 + Sum3 + Sum4 + Sum5)
    T_Sum_Final = T_Sum + T_Sum1 + T_Sum2 + T_Sum3 + T_Sum4 + T_Sum5 + T_Sum6 
    print("Your Total Profit for the Week is: ", round(T_Sum_Final,2))    
    if T_Sum <= 10000:
        print("We DIDNT Reach Our Goal for This Period. More Work is Needed.")    
    else :
        print("You DID Well This Period! Keep up the Great Work!")              
elif P_Days == 3:
    print("For ",DayList[1], ": ")       
    P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
    Sum1 = Sum2 = Sum3 = Sum4 = Sum5 = 0
    while P_Num != 0:   
        P_ValueNum = float(input("Enter Quantity Sold: "))
        if P_Num == 1:
            Sum1 = P_ValueNum * Ap_Iphone
        elif P_Num == 2:
            Sum2 = P_ValueNum * An_Phone
        elif P_Num == 3:
            Sum3 = P_ValueNum * Ap_Tablet
        elif P_Num == 4:
            Sum4 = P_ValueNum * An_Tablet
        elif P_Num == 5:
            Sum5 = P_ValueNum * Win_Tablet                
        P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
    T_Sum = (Sum1 + Sum2 + Sum3 + Sum4 + Sum5)        
    print("For ",DayList[2], ": ")
    Sum1 = Sum2 = Sum3 = Sum4 = Sum5 = 0        
    P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
    while P_Num != 0:           
        P_ValueNum = float(input("Enter Quantity Sold: "))
        if P_Num == 1:
                Sum1 = P_ValueNum * Ap_Iphone
        elif P_Num == 2:
                Sum2 = P_ValueNum * An_Phone
        elif P_Num == 3:
                Sum3 = P_ValueNum * Ap_Tablet
        elif P_Num == 4:
                Sum4 = P_ValueNum * An_Tablet
        elif P_Num == 5:
                Sum5 = P_ValueNum * Win_Tablet               
        P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
    T_Sum1 = (Sum1 + Sum2 + Sum3 + Sum4 + Sum5)        
    print("For ",DayList[3], ": ")
    Sum1 = Sum2 = Sum3 = Sum4 = Sum5 = 0        
    P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
    while P_Num != 0:            
        P_ValueNum = float(input("Enter Quantity Sold: "))
        if P_Num == 1:
                Sum1 = P_ValueNum * Ap_Iphone
        elif P_Num == 2:
                Sum2 = P_ValueNum * An_Phone
        elif P_Num == 3:
                Sum3 = P_ValueNum * Ap_Tablet
        elif P_Num == 4:
                Sum4 = P_ValueNum * An_Tablet
        elif P_Num == 5:
            Sum5 = P_ValueNum * Win_Tablet                
        P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
    T_Sum2 = (Sum1 + Sum2 + Sum3 + Sum4 + Sum5)     
    print("For ",DayList[4], ": ")
    Sum1 = Sum2 = Sum3 = Sum4 = Sum5 = 0        
    P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
    while P_Num != 0:           
        P_ValueNum = float(input("Enter Quantity Sold: "))
        if P_Num == 1:
            Sum1 = P_ValueNum * Ap_Iphone
        elif P_Num == 2:
            Sum2 = P_ValueNum * An_Phone
        elif P_Num == 3:
            Sum3 = P_ValueNum * Ap_Tablet
        elif P_Num == 4:
            Sum4 = P_ValueNum * An_Tablet
        elif P_Num == 5:
            Sum5 = P_ValueNum * Win_Tablet                
        P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
    T_Sum3 = (Sum1 + Sum2 + Sum3 + Sum4 + Sum5)                
    print("For ",DayList[5], ": ")            
    P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
    Sum1 = Sum2 = Sum3 = Sum4 = Sum5 = 0
    while P_Num != 0:           
        P_ValueNum = float(input("Enter Quantity Sold: "))
        if P_Num == 1:
            Sum1 = P_ValueNum * Ap_Iphone
        elif P_Num == 2:
            Sum2 = P_ValueNum * An_Phone
        elif P_Num == 3:
            Sum3 = P_ValueNum * Ap_Tablet
        elif P_Num == 4:
            Sum4 = P_ValueNum * An_Tablet
        elif P_Num == 5:
            Sum5 = P_ValueNum * Win_Tablet                
        P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))       
    T_Sum4 = (Sum1 + Sum2 + Sum3 + Sum4 + Sum5)
    T_Sum_Final = (T_Sum + T_Sum1 + T_Sum2 + T_Sum3 + T_Sum4)
    print("Your Total Profit for the Weekdays is: ", round(T_Sum_Final,2))   
    if T_Sum <= 10000:
        print("We DIDNT Reach Our Goal for This Period. More Work is Needed.")    
    else :
        print("You DID Well This Period! Keep up the Great Work!")      
elif P_Days == 4:
    print("For ",DayList[6], ": ")           
    P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
    Sum1 = Sum2 = Sum3 = Sum4 = Sum5 = 0
    while P_Num != 0:           
        P_ValueNum = float(input("Enter Quantity Sold: "))
        if P_Num == 1:
            Sum1 = P_ValueNum * Ap_Iphone
        elif P_Num == 2:
            Sum2 = P_ValueNum * An_Phone
        elif P_Num == 3:
            Sum3 = P_ValueNum * Ap_Tablet
        elif P_Num == 4:
            Sum4 = P_ValueNum * An_Tablet
        elif P_Num == 5:
            Sum5 = P_ValueNum * Win_Tablet            
        P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
    T_Sum = (Sum1 + Sum2 + Sum3 + Sum4 + Sum5)        
    print("For ",DayList[0], ": ")        
    P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
    Sum1 = Sum2 = Sum3 = Sum4 = Sum5 = 0
    while P_Num != 0:            
        P_ValueNum = float(input("Enter Quantity Sold: "))
        if P_Num == 1:
            Sum1 = P_ValueNum * Ap_Iphone
        elif P_Num == 2:
            Sum2 = P_ValueNum * An_Phone
        elif P_Num == 3:
            Sum3 = P_ValueNum * Ap_Tablet
        elif P_Num == 4:
            Sum4 = P_ValueNum * An_Tablet
        elif P_Num == 5:
            Sum5 = P_ValueNum * Win_Tablet            
        P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
    T_Sum5 = (Sum1 + Sum2 + Sum3 + Sum4 + Sum5)
    T_Sum_Final = T_Sum + T_Sum5
    print("Your Total Profit for the Weekend Days is: ", round(T_Sum_Final,2))    
    if T_Sum <= 10000:
        print("We DIDNT Reach Our Goal for This Period. More Work is Needed.")    
    else :
        print("You DID Well This Period! Keep up the Great Work!")         
elif P_Days == 0: 
    print("")