# Game Map for Dun 2

# import attack.py as atk

dunRooms = []

class Room:
    def __init__(self, name, doors, monster, trap, secret, pcHasVisited):
        self.name = name
        self.doors = doors
        self.monster = monster
        self.trap = trap
        self.secret = secret
        self.pcHasVisited = pcHasVisited

    def introduceSelf(self):
        numDoors = len(self.doors)
        nameDoors = []
        for door in self.doors:
            nameDoors.append(door.name)
            #print(door.name)
        print(f"There are {numDoors} doors in this room.")
        print(*nameDoors)

class Door:
    def __init__(self, name, destination, isLocked):
        self.name = name
        self.destination = destination
        self.isLocked = isLocked
    
    def openDoor(self):
        goTo(self.destination)
        

def roomA1():
    print(dunRooms)
    a1 = Room("a1", [Door("North Door", "a2", False)], None, None, None, True)
    dunRooms.append(a1)
    list(set(dunRooms))

# dungeon map switch set

def goTo(destination):
    match destination:
        case "a1":
            roomA1()
        case "a2":
            roomA2()
        case "a3":
            roomA3()
        case "a4":
            roomA4()
        case "a5":
            roomA5()
        case "a6":
            roomA6()
        case "a7":
            roomA7()
        case "a8":
            roomA8()
        case "a9":
            roomA9()
        case "a10":
            roomA10()
        case "a11":
            roomA11()
        case "a12":
            roomA12()
        case "a13":
            roomA13()
        case "a14":
            roomA14()
        case "a15":
            roomA15()
        case "a16":
            roomA16()
        case "a17":
            roomA17()
        case "a18":
            roomA18()
        case "a19":
            roomA19()
        case "a20":
            roomA20()
        case "a21":
            roomA21()
        case "a22":
            roomA22()
        case "a23":
            roomA23()
        case "a24":
            roomA24()
        case "a25":
            roomA25()
        case "a26":
            roomA26()
        case "a27":
            roomA27()
        case _:
            print("negatory ghost rider")
goTo("a1")
print(dunRooms)
goTo("a1")
