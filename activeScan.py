import math
# define active scanning

def activeScan(scanRange, startCoordinates):
    xOne, yOne = startCoordinates[0], startCoordinates[1]


    levelOne = 12
    levelTwo = 23
    levelThree = 45

    print("What level scan will you perform?\n")
    level = input("1?\n2?\n3?\n")
    match level:
        case "1":
            theta = int(levelOne)
            bc = 84
        case "2":
            theta = int(levelTwo)
            bc = 78
        case "3":
            theta = int(levelThree)
            bc = 67
        case _:
            "Try something else"

    c = scanRange / bc

    print("What is your bearing?\n")
    bearing = input()


    if int(bearing) %  90 != 0:
        newX, newY = math.cos(math.radians(int(bearing))) * scanRange, math.sin(math.radians(int(bearing))) * scanRange
    elif int(bearing) == 0 or int(bearing) == 360:
        newX, newY = scanRange, 0
    elif int(bearing) == 90:
        newX, newY = 0, scanRange
    elif int(bearing) == 180:
        newX, newY = scanRange * (-1), 0
    elif int(bearing) == 270:
        newX, newY = 0, scanRange * (-1)

    else:
        pass
        
    scanPoint = [xOne + round(newX), yOne + round(newY)]
    print(scanPoint)

     

activeScan(10, [30,35])
