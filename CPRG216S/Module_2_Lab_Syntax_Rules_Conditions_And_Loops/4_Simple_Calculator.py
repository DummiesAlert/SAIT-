from operator import sub


print("Welcome to Simple Calculator")

Op = int(input("Enter Your Operation (Add = 1, Sub = 2, Mul = 3, Div = 4): "))
Int1 = float(input("Enter Your First Integer: "))
Int2 = float(input("Enter Your Second Integer: "))

if (Op == 1):

    Add = Int1 + Int2
    print(Add)

elif  (Op == 2):

        Sub = Int1 - Int2
        print(Sub)

elif  (Op == 3):

        Mul = Int1 * Int2
        print(Mul)

elif  (Op == 4):

        Div = Int1 % Int2
        print(Div)

else:

        print("THE OPERATOR YOU HAVE ENTERED IS INVALID")

