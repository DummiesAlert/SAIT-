print("Welcome to Circle Phones' Profit Calculator")

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

P_Num = float(input("Enter Product Number 1-5, or Enter 0 to STOP: "))

while P_Num !=0:

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

T_Sum = Sum1 + Sum2 + Sum3 + Sum4 + Sum5
print("Your Total Profit for Today is: ", round(T_Sum,2))