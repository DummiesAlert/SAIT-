# Group 2 Zhuo Xi Hong, Batsuren D, Savanna Piscitelli
# Assignment 3: Functions, Scoping, and Abstraction
# The purpose of this program is to calculate the client's room area that Rectangular, Square, and Custom to paint and total cost.
# The user will be able to specify whether they want the total room area or single room area.

# Initialize Constant Variables
PROFIT = 0.30
LABOUR_COST = 0.15
PAINTCOVER = 350.0
PAINTCOST = 42.00

print("Welcome to Shiny Paint Company for Indoor Painting! \n ")

#Prompt User for Amount of Rooms
roomNum = int(input("How many Rooms do you Want to Paint?: "))
print("Thank you!\n")

#Function for Rectangle Area, Prompts User for Room Length, Width and Height, and Calculates Total Rectanglar Room Area
def rectangleArea():
    T_RecArea = 0
    Length = int(input("Enter the Length of the Room in Feet: "))
    Width = int(input("Enter the Width of the Room in Feet: "))
    Height = int(input("Enter the Height of the Room in Feet: "))
    RectangleArea = (Width * Height) * 2 + (Length * Height) * 2
    T_RecArea += RectangleArea
    return T_RecArea

#Function for Rectangle Wall Area, Prompts User for Length, Width and Height, and Calculates Rectangle Wall Area
def rectangleWallArea():
    T_RecWall = 0
    Length = int(input("Enter the Length of the Room in Feet: "))
    Width = int(input("Enter the Width of the Room in Feet: "))
    Height = int(input("Enter the Height of the Room in Feet: "))
    RecWallArea = ((Length * Height) * 2) + ((Width * Height) * 2)
    T_RecWall += RecWallArea
    return T_RecWall

#Function for Square Wall Area, Prompts User for OneSide of a Room (Length and Height), and Calculate Square Wall 
def squareWallArea():
    oneSide = int(input("Enter One Side Length of the Room: "))
    heightRoom = int(input("Enter the Height of the Room in Feet: "))
    T_SquareWall = (oneSide * 4) * heightRoom 
    return T_SquareWall

#Function for Custom Wall Area, and Prompts for Length and Height
def customWall():
    wallSum = 0
    walls = int(input("\nHow many Walls are There in the Room: "))
    
    for o in range(1, walls + 1):
        
        Length_Wall = float(input("Enter Length of Wall " + str(o) + " in Feet: "))
        Height_Wall = float(input("Enter Height of Wall " + str(o) + " in Feet: "))
        T_WallSum = Length_Wall * Height_Wall 
        wallSum += T_WallSum
        
    return wallSum

#Function for Windows/Doors, Prompts User for Windows/Doors (Length and Width), and Calculates Total Windows/Doors Area
def windowDoorArea():
    T_WinDoor = 0 
    winDoor = int(input(" \nHow Many Windows and Doors are in the Room? "))
   
    for num in range(1, winDoor + 1):
        
        winLength = float(input("Enter Window/Door length for Window/Door " + str(num) + " in Feet: "))
        winWidth = float(input("Enter Window/Door width for Window/Door " + str(num) +  " in Feet: "))   
        total = winLength * winWidth 
        T_WinDoor += total 
        
    return T_WinDoor

#Function for Room Area If Client, If Room Size = 1, and Calculate Separately
def roomArea():
    
    if Option == 1: 
              
        T_Area = RectWallArea - WinDoorArea
        return T_Area
    
    elif Option == 2:
        
        T_Area = SquareWalls - WinDoorArea
        return T_Area
    
    else: # Which Means Option == 3
        
        T_Area = CustWall - WinDoorArea
        return T_Area
    
#Function for Total Room Area, and Calculate Total Room Size
def AllRoomArea():
    
    if roomNum >= 2:
        
        T_RoomArea = (T_Area1 + T_Area2) + T_Area3
        
    else: # roomNum == 1
        
        T_RoomArea = T_Area1
        
    return T_RoomArea

#Function For Gallons, and Calculate Gallons Per Room
def Gallons():
    
    if Option == 1:
        
        T_Gallons = T_Area1 / PAINTCOVER
        return T_Gallons
    
    elif Option == 2:
        
        T_Gallons = T_Area2 / PAINTCOVER
        return T_Gallons
    
    else: # Which Means Option == 3
        
        T_Gallons = T_Area3 / PAINTCOVER
        return T_Gallons

def PaintPrice():
    T_PaintPrice = gallons * PAINTCOST
    return T_PaintPrice

#If Room Number is > 2, Would Loop and Prompt User for Each Room Size
Room = 0

while roomNum != 0 and roomNum != Room: 
    
    Room += 1
    Option = int(input("Room: " + str(Room) + "\n Select the Shape of Room: \n 1 - Rectangular\n 2 - Square\n 3 - Custom (More or Less Than 4 Walls, All Square or Rectangles\n\nOption: "))    
    
    if Option == 1: 
        
    #Calling Functions 
        RectWallArea = rectangleWallArea()
        WinDoorArea = windowDoorArea()                   
        T_Area1 = roomArea()
        gallons = Gallons()  
        T_PaintCost = PaintPrice() 
        print("\nFor Room: " + str(Room) + ", Area to be Painted is ", T_Area1, " Square ft and Will Require ", format(gallons,'.2f'), " Gallons to Paint. The Paint Will Cost Approximately $", format(T_PaintCost,'.2f'), "\n", sep='')
    
    elif Option == 2:
        
    #Calling Functions 
        SquareWalls = squareWallArea()
        WinDoorArea = windowDoorArea()
        T_Area2 = roomArea()
        gallons = Gallons()  
        T_PaintCost = PaintPrice() 
        print("\nFor Room: " + str(Room) + ", Area to be Painted is ", T_Area2, " Square ft and Will Require ", format(gallons,'.2f'), " Gallons to Paint. The Paint Will Cost Approximately $", format(T_PaintCost,'.2f'), "\n", sep='')
    
    elif Option == 3:
    # calling functions 
        CustWall = customWall()
        WinDoorArea = windowDoorArea()
        T_Area3 = roomArea()
        gallons = Gallons()  
        T_PaintCost = PaintPrice() 
        print("\nFor Room: " + str(Room) +  ", Area to be Painted is ", T_Area3, " Square ft and Will Require ", format(gallons,'.2f'), " Gallons to Paint. The Paint Will Cost Approximately $", format(T_PaintCost,'.2f'), "\n", sep='') 

    else: #Valididate User Input
        
        print("Invalid Selection, Try Again ") 

#Caculate Total Room Area to be Painted, gallons and Cost, Including Labor Cost and Profit
if roomNum >= 2:
    
    T_PaintedArea = AllRoomArea()
    T_Gallon = round(T_PaintedArea / PAINTCOVER)
    T_Paint = float(T_Gallon * PAINTCOST)
    T_Labour = T_PaintedArea * LABOUR_COST
    cost = (T_Labour + T_Paint) * PROFIT
    T_Cost = (T_Labour + T_Paint) + cost
    print("Total Area to be Painted is ", format(T_PaintedArea, '.2f'), " Square ft and Will Require ", format(T_Gallon, '.2f'), " Gallons to Paint. ") 
    print("The Total Customer Estimate Including Paint, Labor, and Overhead is $", format(T_Cost, '.2f'),"")    # Missing ,""

else: 
    
    gallon = float(T_Area1 / PAINTCOVER)
    paint = float(gallon * PAINTCOST)
    T_Gallon = gallon + .10
    T_Labour = T_Area1 * LABOUR_COST
    cost = (T_Labour + PAINTCOST) * PROFIT
    T_Cost = (T_Labour + PAINTCOST) + cost
    print("Total Area to be Painted is ", format(T_Area1, '.2f'), " Square ft and Will Require ", format(T_Gallon, '.0f'), "Gallons to Paint. ") 
    print("The Total Customer Estimate Including Paint, Labor, and Overhead is $", format(T_Cost, '.2f'))    