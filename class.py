# define base classes

class Machine:
    def __init__(self, name, armor, hull, heat, maxHeat):
        self.name = name
        self.armor = armor
        self.hull = hull
        self.heat = heat
        self.maxHeat = maxHeat


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
    def __init__(self, name, armor, hull, heat, maxHeat, weapon):
        super().__init__(name, armor, hull, heat, maxHeat)
        self.weapon = weapon

class MobileUnit(Machine):
    def __init__(self, name, armor, hull, heat, maxHeat, weaponOne, weaponTwo):
        super().__init__(name, armor, hull, heat, maxHeat)
        self.weaponOne = weaponOne
        self.weaponTwo = weaponTwo

