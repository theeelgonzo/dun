import random

# attack module
# accepts meatbag class objects and utilizes attributes for attack

class Meatbag():
    def __init__(self, name, hp, att, dfnd, weapon):
        self.name = name
        self.hp = hp
        self.att = att
        self.dfnd = dfnd
        self.weapon = weapon

class Weapon():
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

def attack(attacker, defender):
    attRoll = random.randrange(1,20) + attacker.att
    defRoll = random.randrange(1,20) + defender.dfnd
    if attRoll >= defRoll:
        damage = random.randrange(1, attacker.weapon.damage)
        defender.hp -= damage
        print(f"{attacker.name} attacks {defender.name} for {damage} points of damage!")
    else:
        print(f"{attacker.name} attacks {defender.name} but misses!")

def powerAttack(attacker, defender):
    attRoll = random.randrange(1,12) + attacker.att
    defRoll = random.randrange(1,20) + defender.dfnd
    if attRoll >+ defRoll:
        damage = attacker.weapon.damage + random.randrange(1, attacker.weapon.damage)
        defender.hp -= damage 
        print(f"{attacker.name} attacks {defender.name} for {damage} points of damage!")
    else:
        print(f"{attacker.name} attacks {defender.name} but misses!")
