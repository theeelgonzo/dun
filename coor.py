import math #get sine and cosine functions for coordinate update
playerCoordinates = []

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
        print(playerCoordinates)

getPlayerCoordinates()
setPlayerCoordinates(1,2)
getPlayerCoordinates()

