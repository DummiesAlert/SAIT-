print ("Welcome to Shiny Paint Company For Indoor Painting!")

RectangArea=0
windows_doors=0
total_point=0
CustomWallsArea=0
SquareWallsArea=0
total_squre=0
total_gallons=0
total_paint_cost=0
total_cost=0

def computeRectangleWallsArea():
    length=float(input("Enther the length of the room in feet: "))
    width=float(input("Enther the width of the room in feet: "))
    height=float(input("Enther the height of the room in feet: "))
    Area_of_rectangular_room= length *height*2 +width *height*2
    return Area_of_rectangular_room


def computeSquareWallsArea():
    length=float(input("Enther the length of the room in feet: "))
    height=float(input("Enther the height of the room in feet: "))
    Area_of_square_room= length *height*4
    return Area_of_square_room

def computeWindowsDoorsArea():
    windows_num= int(input("How many windows/doors are in the room?: "))
    i=1
    sum_windowdoor=0
    for i in range (1,windows_num+1):
        window_length= float(input(f"Enter window length for window {i} in feet: "))
        window_width = float(input(f"Enter window width for window {i} in feet: "))
        area_windows= window_length*window_width
        sum_windowdoor+=area_windows
    return  sum_windowdoor

def computeCustomWallsArea():
    walls_num=int(input("How many walls are there in the room?: "))
    A=1
    Area_of_total_wall=0
    for  A in range (1,walls_num+1):
        wall_length=float(input(f"Enter the length of wall {A} in feet: "))
        wall_height=float(input(f"Enter the height of wall {A} in feet: "))
        area_of_customwall=wall_length*wall_height
        Area_of_total_wall += area_of_customwall
    return Area_of_total_wall

def computeGallons(total_point):
    gallons= total_point/350
    return gallons
def computePaintPrice(Gallons):
    cost_paint= Gallons*42
    return cost_paint


Room_num = int(input("how many rooms do you want to paint?: "))
print('Thank you!')
i=1
while i <= Room_num :
    Option = int(input(f"Room {i}\n Select the shape of the room: \n 1. Rectangular\n 2. Square \n 3. Custom (more or less than 4 walls, all square or rectangles \n Option: "))
    if Option == 1:
        RectangArea=computeRectangleWallsArea()
        windows_doors=computeWindowsDoorsArea()
        total_point= RectangArea-windows_doors
        gallons=computeGallons(total_point)
        cost_paint= computePaintPrice(gallons)
        print(f"For Room: {i}, Area to be painted is {round(total_point,2)} square ft and will require {round(gallons,2)}gallons to paint. The paint will cost approximately{round(cost_paint,2)} $")
    elif Option ==2 :
        SquareWallsArea=computeSquareWallsArea()
        windows_doors=computeWindowsDoorsArea()
        total_point= SquareWallsArea-windows_doors
        gallons=computeGallons(total_point)
        cost_paint= computePaintPrice(gallons)
        print(f"For Room: {i}, Area to be painted is {round(total_point,2)} square ft and will require {round(gallons,2)} gallons to paint. The paint will cost approximately{round(cost_paint,2)} $")
    elif Option ==3:
        CustomWallsArea=computeCustomWallsArea()
        windows_doors=computeWindowsDoorsArea()
        total_point= CustomWallsArea-windows_doors
        gallons=computeGallons(total_point)
        cost_paint= computePaintPrice(gallons)
        print(f"For Room: {i}, Area to be painted is {round(total_point,2)} square ft and will require {round(gallons,2)} gallons to paint. The paint will cost approximately{round(cost_paint,2)} $")
    total_squre+=total_point
    total_gallons+=gallons
    Tgallons=round(total_gallons)
    total_paint_cost=Tgallons*42
    total_cost=(total_squre*0.15+total_paint_cost)*1.3
    i+=1
print(f"Total area to be painted is {total_squre} square ft and will require {Tgallons} gallons to paint.\nThe total customer estimate including paint, labor, and overhead is ${round(total_cost,2)}")