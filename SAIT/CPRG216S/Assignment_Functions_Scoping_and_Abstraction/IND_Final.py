print ("Welcome to Shiny Paint Company For Indoor Painting! \n")

#Sets All Variables to 0 to Ensure No Errors
Rec_Area = 0 
Win_Door = 0 
T_Point = 0 
Area_Custom_Wall = 0 
Square_Walls_Area = 0 
T_Square = 0 
T_Gallons = 0
T_Paint_Cost = 0 
T_Cost = 0 
A_GALLON = 42

def computeRoomArea():
    
    print("placeholder")
    
#Function to Prompt Length, Width and Height to Calculate Area of Rectangular Romm 
def computeRectangleWallsArea():
    
    Length = float(input("Enter the Length of the Room in Feet: "))
    Width = float(input("Enter the Width of the Room in Feet: ")) 
    Height = float(input("Enter the Height of the Romm in Feet: "))
    Area_Rec_Room = Length * Height * 2 + Width * Height * 2 
    return Area_Rec_Room

def computeRectangleArea():
    
    print("placeholder")

#Function to Prompt Length and Height to Calculate Area of Square Room 
def computeSquareWallsArea(): 
    
    Length = float(input("Enter the Length of the Room in Feet: "))
    Height = float(input("Enter the Height of the Romm in Feet: "))
    Area_Square_Room = Length * Height * 4
    return Area_Square_Room 

def computeSquareArea():

    print("placeholder")
    
#Function to Prompt User for Amount of Windows and Doors and Then Prompt for Length and Width to Exclude Paint Job
def computeWindowsDoorsArea(): 
    
    Window_Value = int(input("How Many Windows or Doors are in the Room?: "))
    
    i = 1
    Sum_Win_Doo = 0 
    
    for i in range (1, Window_Value + 1):
        
        Window_Length = float(input(f"Enter Window Length for Window {i} in Feet: "))
        Window_Width = float(input(f"Enter Window Window for Window {i} in Feet: "))
        Area_Win = Window_Length * Window_Width 
        Sum_Win_Doo += Area_Win
        
    return Sum_Win_Doo

#Function to Prompt for Amount of Walls and Length, Width of Each Side to Calculate the Area of the Room 
def computeCustomWallsArea(): 
    
    Wall_Value = int(input("How Many Walls are There in the Room?: "))
    
    A = 1
    Area_T_Wall = 0 
    
    for A in range (1, Wall_Value + 1): 
        
        Wall_Length = float(input(f"Enter the Length of Wall {A} in Feet: "))
        Wall_Height = float(input(f"Enter the Width of Wall {A} in Feet: "))
        Area_Custom_Wall = Wall_Length * Wall_Height
        Area_T_Wall += Area_Custom_Wall
        
    return Area_T_Wall 

#Function to Calculate Gallons Needed
def computeGallons(T_Point): 
    
    Gallon = T_Point / 350 
    return Gallon

#Function to Calculate the Cost of the Paint Job
def computePaintPrice(Gallons): 
    
    Paint_Cost = Gallons * A_GALLON 
    return Paint_Cost

#Start of the Program and Prompt the Amound of Rooms
Room_Num = int(input("How Many Rooms Do You Want to Paint?: "))
print ("Thank You! \n")

i = 1

#Prompt the User Depending the Amount of Rooms Entered Above
while i <= Room_Num: 
    
    Sel = int(input(f"Room: {i}\n Select the Shape of the Room: \n 1. Rectangular \n 2. Square \n 3. Custom (More or Less Than 4 Walls), All Square or Rectangles \n Option: "))
            
    if Sel == 1: # If 1 (Rectangular), Call computeRectangleWallsArea() to Calculate Area and Exclude the Rooms and Doors by Calling computeWindowsDoorsArea(), and Cost of Paint and Prompt Results
        
        Rec_Area = computeRectangleWallsArea()
        Win_Door = computeWindowsDoorsArea()
        T_Point = Rec_Area - Win_Door
        Gallons = computeGallons(T_Point)
        Paint_Cost = computePaintPrice(Gallons)
        
        print(f"For Room: {i}, Area to be Painted is {round(T_Point, 2)} Square FT and Will Require {round(Gallons, 2)} Gallons to Paint. The Paint Will Cost Approximately ${round(Paint_Cost, 2)} ")
        
    elif Sel == 2: # If 2 (Square), Call computeSquareWallsArea() to Calculate Area and Exclude the Rooms and Doors by Calling computeWindowsDoorsArea(), and Cost of Paint and Prompt Results
        
        Square_Walls_Area = computeSquareWallsArea()
        Win_Door = computeWindowsDoorsArea()
        T_Point = Square_Walls_Area - Win_Door 
        Gallons = computeGallons(T_Point)
        Paint_Cost = computePaintPrice(Gallons)
        
        print(f"For Room: {i}, Area to be Painted is {round(T_Point, 2)} Square FT and Will Require {round(Gallons, 2)} Gallons to Paint. The Paint Will Cost Approximately ${round(Paint_Cost, 2)} ")

    elif Sel == 3: # If 3 (Custom), Call computeSquareWallsArea() to Calculate Area and Exclude the Rooms and Doors by Calling computeWindowsDoorsArea(), and Cost of Paint and Prompt Results
        
        CustomWalls_Area = computeCustomWallsArea()
        Win_Door = computeWindowsDoorsArea()
        T_Point = CustomWalls_Area - Win_Door
        Gallons = computeGallons(T_Point)
        Paint_Cost = computePaintPrice(Gallons)
        
        print(f"For Room: {i}, Area to be Painted is {round(T_Point, 2)} Square FT and Will Require {round(Gallons, 2)} Gallons to Paint. The Paint Will Cost Approximately ${round(Paint_Cost, 2)} ")

    #Calculate Final Cost
    T_Square += T_Point  
    T_Gallons += Gallons #Calculate Gallons 
    T_Gallons_F = round(T_Gallons) #Round Gallons 
    T_Paint_Cost = T_Gallons_F * A_GALLON  #Calcualte Paint Cost
    T_Cost = (T_Square * 0.15 + T_Paint_Cost) * 1.3 #Calcualte the Total Cost by Multiplying the Paint Cost, the Area, Labour Cost and Overhead 
    
    i += 1

#Display Result
print(f"Total Area to be Painted is {T_Square} Square FT and Will Require {round(T_Gallons_F)} Gallons to Paint. \nThe Total Customer Estimate Including Paint, Labour, and Overhead is ${round(T_Cost, 2)}")    