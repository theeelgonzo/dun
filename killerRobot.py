class Robot:
    def __init__(self, name, armor, hull, heat, maxHeat, maxRange, maxScan, power):
        self.name = name
        self.armor = armor
        self.hull = hull
        self.heat = heat
        self.maxHeat = maxHeat
        self.maxRange = maxRange
        self.maxScan = maxScan
        self.power = power

class Weapon:
    def __init__(self, name, typeWeapon, shortRange, medRange, longRange, damage, heatGen, powerDrain):
        self.name = name
        self.typeWeapon = typeWeapon
        self.shortRange = shortRange
        self.medRange = medRange
        self.longRange = longRange
        self.damage = damage
        self.heatGen = heatGen
        self.powerDrain = powerDrain

    def fireWeapon(self):
        print(f"You fired the {self.name} for {self.damage} points of damage.")
