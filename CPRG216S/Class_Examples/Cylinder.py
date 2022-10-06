radius = float(input("Enter Radius: "))
height = float(input("Enter Height: "))

pi = 3.14

volume = pi * height * radius ** 2  
area = (2 * pi * radius * height) + (2 * pi * radius ** 2)

print("The Volume is:", volume)
print("The Area is:", area)