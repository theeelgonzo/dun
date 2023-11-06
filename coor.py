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
    newX, newY = math.cos(int(bearing)) * maxRange, math.sin(int(bearing)) * maxRange
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



getPlayerCoordinates()
setPlayerCoordinates(1,2)
moveRobot(maxRange)
print(playerCoordinates)
calculateRange([1,2], [4,6])