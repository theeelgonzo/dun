import sys
import classes as ro
# intialize game and start main game loop

def playGame():
    print("Game starting")
    player = ro.MobileUnit("Combatant", 10, 5, 0, 10, [], 10, weaponOne = ro.Weapon("laser", 0, 10, 2, 999999, 3), weaponTwo = ro.Weapon("cannon", 0, 20, 1, 50, 5))
    print(player.name)

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
