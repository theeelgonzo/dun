# Game Map for Dun 2

import attack.py as atk

class Room:
    def __init__(self, name, doors, monster, trap, secret):
        self.name = name
        self.doors = doors
        self.monster = monster
        self.trap = trap
        self.secret = secret

    def introduceSelf(self):
        numDoors = len(doors)
        nameDoors = []
        for door in doors:
            nameDoors.append(door.name)
        print(f"There are {numDoors} doors in this room.")
        print(*nameDoors)

class Door:
    def __init__(self, name, destination):
        self.name = name


newRoom = Room("Entry Chamber", )

