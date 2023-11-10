# define base classes

class Machine:
    def __init__(self, name, armor, hull, heat, maxHeat, coordinates):
        self.name = name
        self.armor = armor
        self.hull = hull
        self.heat = heat
        self.maxHeat = maxHeat
        self.coordinates = coordinates

    def setPlayerCoordinates(self, x,y):
        if self.coordinates == []:
            self.coordinates.append(x)
            self.coordinates.append(y)
        else:
            x = self.coordinates[0]
            y = self.coordinates[1]



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
    def __init__(self, name, armor, hull, heat, maxHeat, coordinates, weapon):
        super().__init__(name, armor, hull, heat, maxHeat, coordinates)
        self.weapon = weapon

class MobileUnit(Machine):
    def __init__(self, name, armor, hull, heat, maxHeat, coordinates, maxRange, weaponOne, weaponTwo):
        super().__init__(name, armor, hull, heat, maxHeat, coordinates)
        self.maxRange = maxRange
        self.weaponOne = weaponOne
        self.weaponTwo = weaponTwo

    def moveRobot(self, self.maxRange):
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
            pass

        updatePlayerCoordinates(newCoordinates = [round(newX), round(newY)])

    def updatePlayerCoordinates(newCoordinates):
        print(newCoordinates)
        self.coordinates[0] += newCoordinates[0]
        self.coordinates[1] += newCoordinates[1]
        print(self.coordinates)
