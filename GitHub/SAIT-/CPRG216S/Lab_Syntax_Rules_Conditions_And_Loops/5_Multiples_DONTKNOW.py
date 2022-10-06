Int1 = float(input("Enter Your First Integer: "))
Int2 = float(input("Enter Your Second Integer: "))

if Int1 > Int2 and Int1 % Int2 == 0:

    print(Int1, "Is Divible To", Int2) 

elif Int1 < Int2 and Int2 % Int1 == 0:

    print(Int2, "Is Divible To", Int1) 

else :

    print("") 

