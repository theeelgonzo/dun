import sys
import classes as ro
import random
# intialize game and start main game loop

def playGame():
    print("Game starting")
    #instantiate player Combatant mobileUnit
    player = ro.MobileUnit("Combatant", 10, 5, 0, 10, [], 10, weaponOne = ro.Weapon("laser", 0, 10, 2, 999999, 3), weaponTwo = ro.Weapon("cannon", 0, 20, 1, 50, 5))
    print(player.name)

    #instantiate enemy turrets
    turretOne = ro.StatGun("Laser Turret", 0, 10, 0, 20, [], weapon = ro.Weapon("laser", 0, 10, 2, 999999, 3))

    turretTwo = ro.StatGun("Missle Turret", 0, 10, 0, 20, [], weapon = ro.Weapon("missile array", 5, 30, 1, 50, 3))
    
    #define max boundaries of area map and initialize coordinates
    gameMap = [150, 150]
    turretOne.setPlayerCoordinates(random.randrange(0, gameMap[0]),(random.randrange(0,gameMap[1])))
    print(turretOne.coordinates)
    turretTwo.setPlayerCoordinates(random.randrange(0, gameMap[0]),(random.randrange(0,gameMap[1])))
    print(turretTwo.coordinates)
    

def startGame():
    game = ro.Game(True)
    while game == True:
        playGame()
    else:
        sys.exit()

print("Are you ready to play a game?")
gameStart = input("1. Yes\n2. No\n")
if gameStart == "1":
    playGame()
elif gameStart =="2":
    print("Fuck off, peasant")
    sys.exit()
else:
    print("That's not an option, scrub.")
    sys.exit()
