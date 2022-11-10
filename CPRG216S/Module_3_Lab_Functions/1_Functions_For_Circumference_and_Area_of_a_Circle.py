import math 

def Circumference(Radius):

    return 2 * math.pi * Radius 

def Area(Radius):

    return math.pi * Radius ** 2

R = float(input("Enter Circle Radius: "))
C = Circumference(R)
A = Area(R)

print("Cicumference C =: {0}, Area A =: {1}".format(C,A))