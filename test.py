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

class ShieldRoom:
    def __init__(self, shield):
        self.shield = shield

class SwordRoom:
    def __init__(self, sword):
        self.sword = sword

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

roomWithAShield = ShieldRoom(True)
roomWithASword = SwordRoom(True)
roomCuatro = RoomFour("locked")
roomTres = RoomThree("guarded", "alive")
eastPassage = EasternPassage("unsolved")
roomToo = RoomTwo("locked")
orc = Guy(10, ["key"], True)
playerCharacter = PC(10, [], True)

def searchOrc():
    print("""The orc has a key in his pocket.""")
    whatDo = input("""Do you take the key?
1. Yes
2. No\n""")
    match whatDo:
        case "1":
            print("You take the key from the dead orc.")
            playerCharacter.inventory.append("key")
            roomThree()
        case "2":
            print("You leave the orc alone.")
            roomThree()
        case _:
            print(stoop)
            roomThree()

def attackOrc():
    if "sword" and "shield" in playerCharacter.inventory:
        print("""The orc defends himself valiantly, but you best him with the
aid of your righteous weapons!""")
        orc.isAlive = False
        roomTres.door = "unguarded"
        roomTres.orc = "dead"

    else:
        print("""You struggle heroically against the orc, but he slays you with
              the fury of his martial prowess!""")
        playerCharacter.isAlive = False

def talkToOrc():
    print("You approach the orc.")
    print("'What do you want?' he says.")
    whatDo = input("""1. What is your name?
    2. May I pass through this door?
    3. What are you doing here, anyways?
    4. Never mind.\n""")

    match whatDo:
        case "1":
            print("'Douglas.'")
            talkToOrc()
        case "2":
            print("'You sure can't.'")
            talkToOrc()
        case "3":
            print("'I am guarding the door. And being nefarious.'")
            talkToOrc()
        case "4":
            print("'I didn't feel like talking anyways.")
            roomThree()
        case _:
            print(stoop)
            roomThree()


def exitRoom():
    pass

def shieldRoom():
    print("You first see the magnificent tapestries spanning the wall of this domed vault. Then your eyes alight on a sturdy wooden rack bearing a mighty iron shield, marked in the heraldry of an ancient house.")
    whatDo = input("What do you do?\n\n1. Examine the rack\n2. Go through the West Door\n3. Get a Hint")
    if roomWithAShield.shield == True:
        match whatDo:
            case "1":
               takeShield = input("The heavy shield beckons your hand. Do you take it?\n")
               if takeShield.lower() == "yes":
                   print("You remove the shield and wield it.")
                   roomWithAShield.shield = False
                   playerCharacter.inventory.append("shield")
                   shieldRoom()
            case "2":
                print("You return through the West Door.")
                roomThree()
            case "3":
                print("A big iron shield can soak up a lot of damage. You should take it.")
                shieldRoom()
            case _:
                print(stoop)
                shieldRoom()
    else:
        match whatDo:
            case "1":
                print("An empty rack striped with dust.")
            case "2":
                roomThree()
            case "3":
                print("You have what you came for. It's time to move on.")
            case _:
                print(stoop)

def swordRoom():
    print("You enter a room with a vaulted ceiling. Stained glass windows let colored light in from the twilight without, and the waning beams shine upon a metal shape upon an immaculately hewn stone altar.")
    whatDo = input("What do you do?\n\n1. Examine the Altar\n2. Examine the Windows\n3. Go through the East Door\n4. Get a Hint\n")
    match whatDo:
        case "1":
            if roomWithASword.sword == True:
                print("An altar of excellent craftsmanship. A glimmering steel blade lies across its surface.")
                takeSword = input("Do you take the sword?")
                if takeSword.lower() == "yes":
                    print("You take the sword in hand.")
                    playerCharacter.inventory.append("sword")
                    #print(PC.inventory)
                    roomWithASword.sword == False
                    swordRoom()
                else:
                    swordRoom()
            else:
                print("A bare stone altar. Sunbeams fall lightly across it.")
        case "2":
            print("Remarkably crafted mosaics that...")
            print("Seriously? Have you never seen a stained glass window?")
            print("Just use your imagination")
            swordRoom()
        case "3":
            print("You return through the Eastern Door")
            roomThree()
        case "4":
            print("If only there were a big, sharp sword lying around somewhere...")
        case _:
            print(stoop)
            swordRoom

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
                talkToOrc()
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
#talkToOrc()
start = input("Are you ready to enter? Type 'Yes' or 'No' \n")

if start.lower() == "yes":
    print("Let us begin")
    roomOne()
else:
    print("Don't mess around, nerd.")
    sys.exit()

