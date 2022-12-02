Year = int(input("Enter Current Year: "))

if (Year % 400 == 0) and (Year % 100 == 0):

    print("The Year", Year, "IS A LEAP YEAR")

elif (Year % 4 == 0) and (Year % 100 != 0):

    print("The Year", Year, "IS A LEAP YEAR")

else:

    print("The Year", Year, "IS NOT A LEAP YEAR")
    