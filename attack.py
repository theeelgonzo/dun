import random

# attack module
# accepts meatbag class objects and utilizes attributes for attack

class Meatbag():
    def __init__(self, hp, att, dfnd, weapon):
        self.hp = hp
        self.att = att
        self.dfnd = dfnd
        self.weapon = weapon


def attack(attacker, defender):
    
