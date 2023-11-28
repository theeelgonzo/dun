# Game Map for Dun 2

# import attack.py as atk

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


newRoom = Room("Entry Chamber", [Door("A Door to the North", "north"), Door("A door to the south", "south")], None, None, None)

newRoom.introduceSelf()
