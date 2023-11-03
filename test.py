import sys

def roomTwo():
    print("Wow! You made it to the next room!")

def roomOne():
    print("You find yourself in a dimly lit room. The pungent stench of mildew emanates from the wet dungeon walls around you. In front of you, you see a sturdy wooden door.")
    whatDo = input("What do you do?\n1. Open the door\n2. Examine the room\n3. Get a hint.")

    match whatDo:
        case "1":
            print("You try the door and find it is unlocked. You open the door and proceed.\n\n")
            roomTwo()
        case "2":
            print("It's a wet, stinky room.\n\n")
            roomOne()
        case "3":
            print("Buddy, it's a room with one door. If you need help now, you sure are in for it.\n\n")
            roomOne()

print("Welcome to the Dungeon.")
start = input("Are you ready to enter? Type 'Yes' or 'No' \n")

if start.lower() == "yes":
    print("Let us begin")
    roomOne()
else:
    print("Don't mess around, nerd.")
    sys.exit()
