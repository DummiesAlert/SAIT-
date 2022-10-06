Year = int(input("Enter Current Year (Neative Value to Quit): "))

while Year >= 0:

    if (Year %4) == 0 and ((Year % 100) != 0 or (Year % 400) == 0):

        print(Year, "IS A LEAP YEAR")

    else :

        print(Year, "IS A NOT LEAP YEAR")

    Year = int(input("Enter Current Year (Neative Value to Quit): "))
