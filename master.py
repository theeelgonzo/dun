# start of game

gameMap = [["david", "francis"],
           ["doug", "peter"],
           ["ralph", "harry"],
           ["darkRoom", "darkerRoom"]]

playerPosition = gameMap[3][0]

print(playerPosition)

class Room:
    def __init__(self, name, description, look):
        self.name = name
        self.description = description
        self.look = look

    def tellName(self):
        print(f"You are in {self.name}")

    def descSelf(self):
        print(self.description)

    def charLook(self):
        print(self.look)

def getPlayerPosition():
    if playerPosition == True:
        print("Player position value is {playerPosition}")

def moveNorth():
    x = gameMap
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] == playerPosition:
                print(x[i][j])
                print(x[i-1][j])
                x[i][j] = x[i-1][j]
                print(playerPosition)
                print(i, j)
                i -= 1
                print(i, j)
                print(gameMap[i][j])


darkRoom = Room("a Dark Room", "It is like many other rooms, but strangely without light.", "It is hard to see much in this dark room.")
darkerRoom = Room("an Even Darker Room", "Such dark. Much scary. Wow.", "If you could not see in this other room, you sure will not here.")
darkRoom.tellName()
darkRoom.descSelf()
darkRoom.charLook()
moveNorth()
getPlayerPosition()
