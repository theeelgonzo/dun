import sys
import classes.py as ro
# intialize game and start main game loop

def playGame:
    pass

def gameStart:
    game = ro.Game(True)
    while game == True:
        playGame()
    else:
        sys.exit()

print("Are you ready to play a game?")
gameStart = input("1. Yes\n2. No\n")
if gameStart == "1":
    startGame()
elif gameStart =="2":
    print("Fuck off, peasant")
    sys.exit()
else:
    print("That's not an option, scrub.")
    sys.exit()
