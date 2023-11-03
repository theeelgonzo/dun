import sys
import time

stoop = "Try something else. Or maybe try writing a digit on the list instead of whatever that was."

class Guy:
    def __init__(self, health, inventory):
        self.health = health
        self.inventory = inventory
    def printInventory:
        print(self.inventory)

class RoomFour:
    def __init__(self, door):
        self.door = door

class RoomThree:
    def __init__(self, door, orc):
        self.door = door
        self.orc = orc

class RoomTwo:
    def __init__(self, door):
        self.door = door

class EasternPassage:
    def __init__(self, puzzle):
        self.puzzle = puzzle
    def unlockDoor(self):
        if self.puzzle == "solved":
            print("You hear in the distance the sound of a heavy lock releasing.")
            roomToo.door = "unlocked"
        else:
            roomTwo.door = "locked"
eastPassage = EasternPassage("unsolved")
roomToo = RoomTwo("locked")

def exitRoom():
    pass

def shieldRoom():
    pass

def swordRoom():
    pass

def roomThree():
    print("You find yourself in a well lit room.")
    print("There is a door to the South, a door to the West, a door to the East. Also, there is a door to the North guarded by an angry-looking orc.")
    whatDo = input("What do you do?\n\n1. Go through the South Door\n2. Go through the West Door\n 3. Go through the North Door\n4. Go through the East Door\n4. Talk to the orc\n5. Attack the orc\n6. Get a hint\n")
    match whatDo:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case _:
            print(stoop)
            roomThree()

def easternPassage():
    #eastPassage = EasternPassage("unsolved")
    print("You enter a room lit by an aromatic brazier. There is a passage to your west. In an alcove marked by faded frescoes on the northern wall, you see a worn sculpture of a sphynx.")
    whatDo = input("What do you do?\n\n1. Go through the west passage\n2. Touch the sphynx\n3. Get a hint")
    match whatDo:
        case "1":
            roomTwo()
        case "2":
            print("You reach out and brush your fingertips against the smooth stone of the sphynx. You hear a voice in your head...")
            print("'What is two plus two?'")
            riddleAnswer = input("How do you respond?\n")
            if riddleAnswer == "4":
                print("You hear a voice in your head say, 'Well done!'")
                eastPassage.puzzle = "solved"
                eastPassage.unlockDoor()
                #roomToo.door = "unlocked"
                easternPassage()
            else:
                print(f"Seriously? You thought {riddleAnswer} was the answer? Get real!")
                easternPassage()
        case "3":
            print("Get a hint? More like Get A Life!")
            easternPassage()
        case _:
            print(stoop)
            easternPassage()

def roomTwo():
    #if eastPassage.puzzle == "solved":
        #roomToo = RoomTwo("unlocked")
    #else:
        #roomToo = RoomTwo("locked")
    print("Wow! You made it to the next room!")
    #if roomTwo.door == "locked":
        #print("You see a door, but it appears to be locked.")
    print("You find yourself in a room with a door to the north, a door to the south, and an open passageway eastward.\n")
    whatDo = input("What do you do?\n\n1. Go through the North Door\n2. Go through the South Door\n3. Go through the Eastern Passage\n4.Get a hint")
    match whatDo:
        case "1":
            if roomToo.door == "locked":
                print("You try the door, but it is locked.\n")
                roomTwo()
            else: roomThree()
        case "2":
            roomOne()
        case "3":
            easternPassage()
        case "4":
            print("If you are faced with a locked door, find a way to unlock it.")
            roomTwo()
        case _:
            print(stoop)
            roomTwo()


def roomOne():
    print("You find yourself in a dimly lit room. The pungent stench of mildew emanates from the wet dungeon walls around you. In front of you to the north, you see a sturdy wooden door.")
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
        case _:
            print(stoop)
            roomOne()

print("Welcome to the Dungeon.")
start = input("Are you ready to enter? Type 'Yes' or 'No' \n")

if start.lower() == "yes":
    print("Let us begin")
    roomOne()
else:
    print("Don't mess around, nerd.")
    sys.exit()
