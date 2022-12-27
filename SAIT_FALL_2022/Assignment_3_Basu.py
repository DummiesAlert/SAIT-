profit = 0.3
labourCost = .15
paintCover = 350.0
paintCost = 42.00
plus = .40
loop = True
total_WinDo = 0.0

print("Welcome to Shiny Paint Company for indoor painting! ")
roomNum = int(input("How many Rooms do you want to paint?: "))
print("Thank you! ")

if roomNum >= 2:
    while (loop):      
        option = 0
        option = int(input("Select the shape of room:\n 1 - Rectangular\n 2 - Square\n 3 - Custom (more or less than 4 walls, all square or rectangles\nOption: "))
        if option == 1:
            length = int(input("Enter the length of the room in feet: "))
            width = int(input("Enter the width of the room in feet: "))
            height = int(input("Enter the height of the room in feet: "))

            int(input("How many windows and doors are in the room: "))

            winLength1 = int(input("Enter window/door length for window/door 1 in feet: "))
            winWidth1 = int(input("Enter window/door width for window/door 1 in feet: "))
            winLength2 = int(input("Enter window/door length for window/door 2 in feet: "))
            winWidth2 = int(input("Enter window/door width for window/door 2 in feet: "))

            def rectangleArea(length, width, height):
                return (length * width) * 2 + (width * height) * 2 + (length * height) * 2

            def rectangleWallsArea(length, height, width):
                return ((length * height) * 2) + ((width * height) * 2)

            def windowsDoorsArea(winLength1,winWidth1, winLength2 ,winWidth2):
                return (winLength1 * winWidth1) + (winLength2 * winWidth2)


            tobePaintedArea1 = float(rectangleWallsArea(length, height, width) - windowsDoorsArea(winLength1, winWidth1, winLength2, winWidth2))
            gallon = float(tobePaintedArea1 / paintCover)
            paint = float(gallon * paintCost)
            print("For Room: 1, Area to be painted is ", tobePaintedArea1, " square ft and will require ", format(gallon,'.2f'), " gallons to paint. The paint will cost approximately $", format(paint,'.2f'), sep='')

            print("Room: 2 ")
        
        
        elif option == 2:    
            oneSide = int(input("Enter one side length of the room: "))
            heightRoom = int(input("Enter the height of the room in feet: "))

            int(input("How many windows and doors are in the room: "))

            winLength1 = int(input("Enter window/door length for window/door 1 in feet: "))
            winWidth1 = int(input("Enter window/door width for window/door 1 in feet: "))
            winLength2 = int(input("Enter window/door length for window/door 2 in feet: "))
            winWidth2 = int(input("Enter window/door width for window/door 2 in feet: "))
            winLength3 = int(input("Enter window/door length for window/door 3 in feet: "))
            winWidth3 = int(input("Enter window/door width for window/door 3 in feet: "))

            def squareWallsArea(heightRoom, oneSide):
                return (oneSide * 4) * heightRoom 

            def windowsDoorsArea(winLength1,winWidth1, winLength2 ,winWidth2, winLength3 , winWidth3):
                return (winLength1 * winWidth1) + (winLength2 * winWidth2) + (winLength3 * winWidth3)

            tobePaintedArea2 = float(squareWallsArea(heightRoom, oneSide) - windowsDoorsArea(winLength1, winWidth1, winLength2, winWidth2, winLength3, winWidth3))
            gallon = float(tobePaintedArea2 / paintCover)
            paint = float(gallon * paintCost)
            print("For Room: 2, Area to be painted is ", tobePaintedArea2, " square ft and will require ", format(gallon, '.2f'), " gallons to paint. The paint will cost approximately $", format(paint, '.2f'), sep='')

            print("Room: 3 ")
        
        elif option == 3:      
            int(input("How many walls are there in the room: "))

            lengthWall1 = int(input("Enter length of wall 1 in feet: "))
            heightWall1 = int(input("Enter height of wall 1 in feet: "))
            lengthWall2 = int(input("Enter length of wall 1 in feet: "))
            heightWall2 = int(input("Enter height of wall 1 in feet: "))
            lengthWall3 = int(input("Enter length of wall 1 in feet: "))
            heightWall3 = int(input("Enter height of wall 1 in feet: "))

            int(input("How many windows and doors are in the room: "))

            winLength1 = int(input("Enter window/door length for window/door 1 in feet: "))
            winWidth1 = int(input("Enter window/door width for window/door 1 in feet: "))

            def customWalls(lengthWall1, heightWall1, lengthWall2, heightWall2, lengthWall3, heightWall3):
                return (lengthWall1 * heightWall1) + (lengthWall2 * heightWall2) + (lengthWall3 * heightWall3)

            def windowsDoorsArea(winLength1, winWidth1):
                return (winLength1 * winWidth1)


            tobePaintedArea3 = float(customWalls(lengthWall1, heightWall1, lengthWall2, heightWall2, lengthWall3, heightWall3) - windowsDoorsArea(winLength1, winWidth1))
            gallon = float(tobePaintedArea3 / paintCover)
            paint = float(gallon * paintCost)
            print("For Room: 3, Area to be painted is ", tobePaintedArea3, " square ft and will require ", format(gallon,'.2f'), " gallons to paint. The paint will cost approximately $", format(paint, '.2f'), sep='')

            def totalArea(lengthWall1, heightWall1, lengthWall2, heightWall2, lengthWall3, heightWall3, height, oneSide, length, width):
                return float(customWalls(lengthWall1, heightWall1, lengthWall2, heightWall2, lengthWall3, heightWall3) + squareWallsArea(height, oneSide) + rectangleWallsArea(length, height, width))

            totalPaintedArea = (tobePaintedArea1 + tobePaintedArea2) + tobePaintedArea3 #float(customWalls(lengthWall1, heightWall1, lengthWall2, heightWall2, lengthWall3, heightWall3) + squareWallsArea(height, oneSide) + rectangleWallsArea(length, height, width))
            totalLabour = totalPaintedArea * labourCost #totalArea(lengthWall1, heightWall1, lengthWall2, heightWall2, lengthWall3, heightWall3, height, oneSide, length, width)
            totalGallon = (totalPaintedArea / paintCover) + plus #totalArea(lengthWall1, heightWall1, lengthWall2, heightWall2, lengthWall3, heightWall3, height, oneSide, length, width) / paintCover
            totalPaintCost = (totalGallon * paintCost) 
            cost = (totalLabour + totalPaintCost) * profit
            totalCost = (totalLabour + totalPaintCost) + cost
            print("Total area to be painted is ", totalPaintedArea, " square ft and will require ", format(totalGallon,'.2f'), " gallons to paint. ") 
            print("The total customer estimate including paint, labor, and overhead is $", format(totalCost,'.2f'), sep='')
        else:
            print("Invalid number, try again! ")
else:
    roomNum == 1
    print("Room: 1 ")
    option = int(input("Select the shape of the room:\n 1 - Rectangular\n 2 - Square\n 3 - Custom (more or less than 4 walls, all square or rectangless\nOption: "))
    if option == 1:
        length = int(input("Enter the length of the room in feet: "))
        width = int(input("Enter the width of the room in feet: "))
        height = int(input("Enter the height of the room in feet: "))
                       
        WinDoor = int(input("How many windows and doors are in the room: "))
        if WinDoor != 0:
            for num in range(1, WinDoor+1):              
                winLength = float(input("Enter window/door length for window/door " + str(num) + " in feet: "))
                winWidth = float(input("Enter window/door width for window/door " + str(num) + " in feet: "))
                total_WinDo += winLength * winWidth
                

            def rectangleArea(length, width, height):
                return float((length * width) * 2 + (width * height) * 2 + (length * height) * 2)

            def rectangleWallsArea(length, height, width):
                return float((length * height) * 2) + ((width * height) * 2)

            
            tobePaintedArea1 = float(rectangleWallsArea(length, height, width) -  total_WinDo) #windowsDoorsArea(winLength1, winWidth1, winLength2, winWidth2))
            gallon = float(tobePaintedArea1 / paintCover)
            paint = float(gallon * paintCost)
            totalGallon = gallon + .10
            totalLabour = tobePaintedArea1 * labourCost
            cost = (totalLabour + paintCost) * profit
            totalCost = (totalLabour + paintCost) + cost

            print("For Room: 1, Area to be painted is ", tobePaintedArea1, " square ft and will require ", format(gallon,'.2f'), " gallons to paint. The paint will cost approximately $", format(paint,'.2f'), sep='')
            print("Total area to be painted is ", tobePaintedArea1, " square ft and will require ",int(totalGallon), " gallons to paint. ")
            print("The total customer estimate including paint, labour, and overhead is ", format(totalCost,'.2f'), sep='') 
        
    else:
        print("Invalid Select ")