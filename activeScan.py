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
            thetaOne = round(int(levelOne) / 2)
            thetaTwo = 360 - (round(int(levelOne) / 2))
            bc = 84
        case "2":
            thetaOne = round(int(levelTwo) / 2)
            thetaTwo = 360 - (round(int(levelTwo) / 2))
            bc = 78
        case "3":
            thetaOne = round(int(levelThree) / 2)
            thetaTwo = 360 - (round(int(levelThree) / 2))
            bc = 67
        case _:
            "Try something else"

    c = scanRange / math.sin(math.degrees(int(bc)))
    

    print("What is your bearing?\n")
    bearing = input()

    def calcEndPoint(bearing, length):
        if int(bearing) %  90 != 0:
            newX, newY = math.cos(math.radians(int(bearing))) * length, math.sin(math.radians(int(bearing))) * length
        elif int(bearing) == 0 or int(bearing) == 360:
            newX, newY = length, 0
        elif int(bearing) == 90:
            newX, newY = 0, length
        elif int(bearing) == 180:
            newX, newY = length * (-1), 0
        elif int(bearing) == 270:
            newX, newY = 0, length * (-1)

        else:
            pass
        
        scanPoint = [xOne + round(newX), yOne + round(newY)]
        print(scanPoint)

    calcEndPoint(bearing, scanRange)
    calcEndPoint(thetaOne, c)
    calcEndPoint(thetaTwo, c)

activeScan(10, [30,35])
