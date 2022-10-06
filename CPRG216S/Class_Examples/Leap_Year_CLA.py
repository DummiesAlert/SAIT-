is_leap_year = False 

Year = int(input("Enter Current Year: "))

if (Year %4) == 0:
    if (Year % 100) == 0:
       if (Year % 400) == 0:

            is_leap_year = True
    else: 

        is_leap_year = True 

if is_leap_year: 

    print(Year, "IS A LEAP YEAR")

else:

    print(Year, "IS A NOT LEAP YEAR")