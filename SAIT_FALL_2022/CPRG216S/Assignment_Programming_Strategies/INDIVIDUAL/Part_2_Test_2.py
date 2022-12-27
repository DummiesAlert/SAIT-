print("Welcome to Circle Phones' Profit Calculator")
print("You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend.")
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

Sum1 = 0
Sum2 = 0
Sum3 = 0
Sum4 = 0
Sum5 = 0

i = 0

DayList = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

while i <= 5:
    
    if P_Days == 1: 

        S_Day = str(input("Enter a Specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]: "))
        
        P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
        while P_Days == 1:
            
            P_ValueNum = float(input("Enter Quantity Sold: "))
            P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))

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
    
            else:

                print("Thanks For Using Circle Phones Profit Calculator")
                break 

        i += 1
  
        T_Sum = (Sum1 + Sum2 + Sum3 + Sum4 + Sum5)
        print("Your Total Profit for Today is Exactly: ", T_Sum)
        print("Your Total Profit for", S_Day, "is Approxiately: ", round(T_Sum))
        break

    elif P_Days == 2:
    
        while P_Days == 2:
            
            a = 0
            
            print("For ",DayList[a])
            
            while i <= 7:
                P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
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
    
                else:

                    break 

        i += 1
        DayList[a] = DayList[a + 1]
  
        T_Sum = (Sum1 + Sum2 + Sum3 + Sum4 + Sum5)
        print("Your Total Profit for Today is Exactly: ", T_Sum)
        print("Your Total Profit for is Approxiately: ", round(T_Sum))
        break

    elif P_Days == 3:

        S_Day = str(input("Enter a Specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]: "))
        
        P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
        while P_Days == 3:
            
            P_ValueNum = float(input("Enter Quantity Sold: "))
            P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))

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
    
            else:

                print("Thanks For Using Circle Phones Profit Calculator")
                break 

        i += 1
  
        T_Sum = (Sum1 + Sum2 + Sum3 + Sum4 + Sum5)
        print("Your Total Profit for Today is Exactly: ", T_Sum)
        print("Your Total Profit for", S_Day, "is Approxiately: ", round(T_Sum))
        break

    elif P_Days == 4:

        S_Day = str(input("Enter a Specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]: "))
        
        P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))
        while P_Days == 4:
            
            P_ValueNum = float(input("Enter Quantity Sold: "))
            P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))

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
    
            else:

                print("Thanks For Using Circle Phones Profit Calculator")
                break 

        i += 1
  
        T_Sum = (Sum1 + Sum2 + Sum3 + Sum4 + Sum5)
        print("Your Total Profit for Today is Exactly: ", T_Sum)
        print("Your Total Profit for", S_Day, "is Approxiately: ", round(T_Sum))
        break
    
    elif P_Days == 0: 

        print("END")
        break