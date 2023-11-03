import sys
import time

stoop = "Try something else. Or maybe try writing a digit on the list instead of whatever that was."

class Guy:
    def __init__(self, health, inventory, isAlive):
        self.health = health
        self.inventory = inventory
        self.isAlive = isAlive


        if self.health <= 0:
            self.isAlive == False

    def printInventory(self):
        print(self.inventory)

class PC(Guy):
    def __init__(self, health, inventory, isAlive):
        super().__init__(health, inventory, isAlive)
        if self.isAlive == False:
            print("You Died!")
            sys.exit()

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

roomCuatro = RoomFour("locked")
roomTres = RoomThree("guarded", "alive")
eastPassage = EasternPassage("unsolved")
roomToo = RoomTwo("locked")
orc = Guy(10, ["key"], True)
playerCharacter = PC(10, [], True)

def searchOrc():
    pass

def attackOrc():
    pass

def talkToOrc():
    pass

def exitRoom():
    pass

def shieldRoom():
    pass

def swordRoom():
    pass

def roomThree():
    print("You find yourself in a well lit room.")
    print("There is a door to the South, a door to the West, a door to the East. Also, there is a door to the North guarded by an angry-looking orc.")
    if orc.isAlive == True:
        whatDo = input("What do you do?\n\n1. Go through the South Door\n2. Go through the West Door\n 3. Go through the North Door\n4. Go through the East Door\n5. Talk to the orc\n6. Attack the orc\n7. Get a hint\n")
        match whatDo:
            case "1":
                print("You go through the South Door")
                roomTwo()
            case "2":
                print("You traverse the Door to the West")
                swordRoom()
            case "3":
                if roomTres.door == "guarded":
                    print("You may not pass through this door while the orc defends it.")
                    roomThree()
                else:
                    print("You pass through the Northern Door.")
                    exitRoom()
            case "4":
                print("You journey beyond the East Door.")
                shieldRoom()
            case "5":
                print("You attempt to chat with the orc")
                talkOrc()
            case "6":
                artThouCertain = input("Are you sure you wish to attack the orc?")
                if artThouCertain.lower() == "yes":
                    attackOrc()
                else:
                    print("What? Are you afraid to commit?")
                    roomThree()
            case "7":
                print("What would you do if a big, angry, green orc was standing between you and freedom?")
                roomThree()
            case _:
                print(stoop)
                roomThree()

    else:
        whatDo = input("What do you do?\n\n1. Go through the South Door\n2. Go through the West Door\n 3. Go through the North Door\n4. Go through the East Door\n5. Search to the orc\n6. Get a hint\n")
        match whatDo:
            case "1":
                print("You go through the South Door")
                roomTwo()
            case "2":
                print("You traverse the Door to the West")
                swordRoom()
            case "3":
                if roomTres.door == "guarded":
                    print("You may not pass through this door while the orc defends it.")
                    roomThree()
                else:
                    print("You pass through the Northern Door.")
                    exitRoom()
            case "4":
                print("You journey beyond the East Door.")
                shieldRoom()
            case "5":
                searchOrc()
            case "6":
                print("You know, if there's no one around, it's not so bad to go through a dead guy's pockets...")
                roomThree()
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
#orc.printInventory()
#playerCharacter.printInventory()
playerCharacter.health = 0
print(playerCharacter.health)
print(playerCharacter.isAlive)
start = input("Are you ready to enter? Type 'Yes' or 'No' \n")

if start.lower() == "yes":
    print("Let us begin")
    roomOne()
else:
    print("Don't mess around, nerd.")
    sys.exit()
