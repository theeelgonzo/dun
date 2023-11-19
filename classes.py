import math
import coor as coor
import weakref

#define game class and attributes

class Game:
    def __init__(self, game):
        self.game = game

# define base classes

class Machine:
    instances = []
    def __init__(self, name, armor, hull, heat, maxHeat, coordinates, passScanRange, actScanRange):
        self.__class__.instances.append(weakref.proxy(self))
        self.name = name
        self.armor = armor
        self.hull = hull
        self.heat = heat
        self.maxHeat = maxHeat
        self.coordinates = coordinates
        self.passScanRange = passScanRange
        self.actScanRange = actScanRange

    def setPlayerCoordinates(self, x,y):
        if self.coordinates == []:
            self.coordinates.append(x)
            self.coordinates.append(y)
        else:
            x = self.coordinates[0]
            y = self.coordinates[1]
    
    def passiveScan(self):
        minX, maxX = self.coordinates[0] - self.passScanRange, self.coordinates[0] + self.passScanRange
        minY, maxY = self.coordinates[1] - self.passScanRange, self.coordinates[1] + self.passScanRange
        for instance in Machine.instances:
            if instance.coordinates[0] > minX and instance.coordinates[0] < maxX:
                if instance.coordinates[1] > minY and instance.coordinates[1] < maxY:
                    if instance.coordinates != self.coordinates:
                        print("Radar picks up heat signatures in the area.")
                    else:
                        print("Nothing on radar.")
            else:
                print("Nothing on radar.")

    def activeScan(self):
        pass



class Weapon:
    def __init__(self, name, minRange, maxRange, heatGen, ammo, damage):
        self.name = name
        self.minRange = minRange
        self.maxRange = maxRange
        self.heatGen = heatGen
        self.ammo = ammo
        self.damage = damage

    def fireWeapon(self):
        pass


#Machine super classes

class StatGun(Machine):
    def __init__(self, name, armor, hull, heat, maxHeat, coordinates, passScanRange, actScanRange, weapon):
        super().__init__(name, armor, hull, heat, maxHeat, coordinates, passScanRange, actScanRange)
        self.weapon = weapon

class MobileUnit(Machine):
    def __init__(self, name, armor, hull, heat, maxHeat, coordinates, passScanRange, actScanRange, maxRange, weaponOne, weaponTwo):
        super().__init__(name, armor, hull, heat, maxHeat, coordinates, passScanRange, actScanRange)
        self.maxRange = maxRange
        self.weaponOne = weaponOne
        self.weaponTwo = weaponTwo

    def moveRobot(self, maxRange):
        radius = self.maxRange
        bearing = input("What is your bearing?")
        if int(bearing) %  90 != 0:
            newX, newY = math.cos(math.radians(int(bearing))) * self.maxRange, math.sin(math.radians(int(bearing))) * self.maxRange
        elif int(bearing) == 0 or int(bearing) == 360:
            newX, newY = self.maxRange, 0
        elif int(bearing) == 90:
            newX, newY = 0, self.maxRange
        elif int(bearing) == 180:
            newX, newY = self.maxRange * (-1), 0
        elif int(bearing) == 270:
            newX, newY = 0, self.maxRange * (-1)

        else:
            updatePlayerCoordinates(newCoordinates = [round(newX), round(newY)])



    def updatePlayerCoordinates(self, newCoordinates):
        print(newCoordinates)
        self.coordinates[0] += newCoordinates[0]
        self.coordinates[1] += newCoordinates[1]
        print(self.coordinates)
