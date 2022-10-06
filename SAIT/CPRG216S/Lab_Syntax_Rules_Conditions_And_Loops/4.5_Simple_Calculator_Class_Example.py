Op = int(input("Enter Your Operation (Add, Sub, Mul, Div): "))
Int1 = float(input("Enter Your First Integer: "))
Int2 = float(input("Enter Your Second Integer: "))

if Op == 'Add':

    Result = Int1 + Int2
    print(Int1, "+", Int2, "=", Result)

elif Op == 'Sub':

    Result = Int1 - Int2
    print(Int1, "-", Int2, "=", Result)

elif Op == 'Mul':

    Result = Int1 * Int2
    print(Int1, "x", Int2, "=", Result)

elif Op == 'Div':

    Result = Int1 % Int2
    print(Int1, "/", Int2, "=", Result)

else :

    print("THE OPERATOR YOU HAVE ENTERED IS INVALID")