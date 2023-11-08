import math #get sine and cosine functions for coordinate update
playerCoordinates = []
maxRange = 10

def setPlayerCoordinates(x,y):
    if playerCoordinates == []:
        playerCoordinates.append(x)
        playerCoordinates.append(y)
    else:
        x = playerCoordinates[0]
        y = playerCoordinates[1]

def getPlayerCoordinates():
    if playerCoordinates == []:
        print("There are no player coordinates yet.")
    else:
        return playerCoordinates

def moveRobot(maxRange):
    radius = maxRange
    bearing = input("What is your bearing?")
    if int(bearing) %  90 != 0:
        newX, newY = math.cos(math.radians(int(bearing))) * maxRange, math.sin(math.radians(int(bearing))) * maxRange
    elif int(bearing) == 0 || int(bearing) == 360:
        newX, newY = maxRange, 0
    elif int(bearing) == 90:
        newX, newY = 0, maxRange
    elif int(bearing) == 180:

    else:
        pass

    updatePlayerCoordinates(newCoordinates = [round(newX), round(newY)])
    
    
    

def updatePlayerCoordinates(newCoordinates):
    print(newCoordinates)
    playerCoordinates[0] += newCoordinates[0]
    playerCoordinates[1] += newCoordinates[1]
    print(playerCoordinates)
    
def calculateRange(pointA, pointB):
    distance = []
    distance.append(pointB[0] - pointA[0])
    distance.append(pointB[1] - pointA[1])
    print(distance)
    cSquared = distance[0] ** 2 + distance[1] ** 2
    print(cSquared)
    print(int(math.sqrt(cSquared)))



#getPlayerCoordinates()
setPlayerCoordinates(1,2)
print(playerCoordinates)
moveRobot(maxRange)
#print(playerCoordinates)
#calculateRange([1,2], [4,6])
