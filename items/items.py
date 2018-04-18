"""
A file for all the different items in the game

name: the item's name
value: the item's price in coins when found in shops
You can sell the item for 1/5 the items value to shops

if consumable:
    consume: what happens when item is consumed

if equipment:
    slot: what slot the equipment goes on
    will replace equipped items already in the slot
        0: Head
        1: Body
        2: Legs
        3: Weapon
        4: Accessory 1
        5: Accessory 2


"""

# import TextBased
# import Combat
from characters.player import *
from image import *

# consumables

'''
class :
    def __init__(self):
        self.name =
        self.player = Player()
        self.value =

    def consume(self):
        player.inv_remove(self.name)
'''

# healing


class Herb:  #
    # Consumable that heals 600 health
    def __init__(self):
        self.name = "Herb"
        self.player = Player()
        self.value = 20

    def consume(self):
        self.player.inv_remove(self.name)
        self.player.stats.heal(600)


class SmallHealthPotion:
    # Consumable that heals 1300 health
    def __init__(self):
        self.name = "Small Health Potion"
        self.player = Player()
        self.value = 55

    def consume(self):
        self.player.inv_remove(self.name)
        self.player.stats.heal(1300)


class MediumHealthPotion:
    # Consumable that heals 2100 health
    def __init__(self):
        self.name = "Medium Health Potion"
        self.player = Player()
        self.value = 115

    def consume(self):
        self.player.inv_remove(self.name)
        self.player.stats.heal(2100)


class LargeHealthPotion:
    # Consumable that heals 3300 health
    def __init__(self):
        self.name = "Large Health Potion"
        self.player = Player()
        self.value = 190

    def consume(self):
        self.player.inv_remove(self.name)
        self.player.stats.heal(3300)


# boosts
class StrengthPot:  #
    # Consumable that boosts strength temporarily
    def __init__(self):
        self.name = "Strength Potion"
        self.player = Player()
        self.value = 30

    def consume(self):
        self.player.inv_remove(self.name)
        # self.player.strength += 5 for 3 turns


# other
class Antidote:  #
    # consumable that cure poison
    def __init__(self):
        self.name = "Antidote"
        self.player = Player()
        self.value = 20

    def consume(self):
        self.player.inv_remove(self.name)
        self.player.stats.antidote()


# armor sets
'''
class :  #
    def __init__(self):
        self.name = ""
        self.value = 

        self.strength = 
        self.intelligence = 
        self.defence = 

        self.slot = 0

class :  #
    def __init__(self):
        self.name = ""
        self.value = 

        self.strength = 
        self.intelligence = 
        self.defence = 

        self.slot = 1

class :  #
    def __init__(self):
        self.name = ""
        self.value = 

        self.strength = 
        self.intelligence = 
        self.defence = 

        self.slot = 2
'''


# starter
class ClothHat:  #
    def __init__(self):
        self.name = "Cloth Hat"
        self.value = 5

        self.strength = 0
        self.intelligence = 0
        self.defence = 0

        self.slot = 0


class ClothTop:  #
    def __init__(self):
        self.name = "Cloth Shirt"
        self.value = 5

        self.strength = 0
        self.intelligence = 0
        self.defence = 0

        self.slot = 1


class ClothBot:  #
    def __init__(self):
        self.name = "Cloth Pants"
        self.value = 5

        self.strength = 0
        self.intelligence = 0
        self.defence = 0

        self.slot = 2

# strength class


# warrior armor
class WarriorHat:  #
    def __init__(self):
        self.name = "Warrior Helmet"
        self.value = 70

        self.strength = 25
        self.intelligence = 0
        self.defence = 10

        self.slot = 0


class WarriorTop:  #
    def __init__(self):
        self.name = "Warrior Chainmail"
        self.value = 70

        self.strength = 25
        self.intelligence = 0
        self.defence = 10

        self.slot = 1


class WarriorBot:  #
    def __init__(self):
        self.name = "Warrior Leggings"
        self.value = 70

        self.strength = 25
        self.intelligence = 0
        self.defence = 10

        self.slot = 2


# berserker armor
class BerserkerHat:  #
    def __init__(self):
        self.name = "Berserker Helmet"
        self.value = 120

        self.strength = 45
        self.intelligence = 0
        self.defence = 10
        self.slot = 0


class BerserkerTop:  #
    def __init__(self):
        self.name = "Berserker "
        self.value = 120

        self.strength = 45
        self.intelligence = 0
        self.defence = 10

        self.slot = 1


class BerserkerBot:  #
    def __init__(self):
        self.name = "Berserker "
        self.value = 120

        self.strength = 45
        self.intelligence = 0
        self.defence = 10

        self.slot = 2

# intelligence class


# wizard robes
class WizardHat:  #
    def __init__(self):
        self.name = "Wizard Hat"
        self.value = 40

        self.strength = 0
        self.intelligence = 10
        self.defence = 5

        self.slot = 0


class WizardTop:  #
    def __init__(self):
        self.name = "Wizard Robe Top"
        self.value = 40

        self.strength = 0
        self.intelligence = 10
        self.defence = 5

        self.slot = 1


class WizardBot:  #
    def __init__(self):
        self.name = "Wizard Robe Bottom"
        self.value = 40

        self.strength = 0
        self.intelligence = 10
        self.defence = 5

        self.slot = 2


# arcanist robes
class ArcanistHat:  #
    def __init__(self):
        self.name = "Arcanist Hat"
        self.value = 90

        self.strength = 0
        self.intelligence = 45
        self.defence = 15

        self.slot = 0


class ArcanistTop:  #
    def __init__(self):
        self.name = "Arcanist Robe Top"
        self.value = 90

        self.strength = 0
        self.intelligence = 45
        self.defence = 15

        self.slot = 1


class ArcanistBot:  #
    def __init__(self):
        self.name = "Arcanist Robe Bottom"
        self.value = 90

        self.strength = 0
        self.intelligence = 45
        self.defence = 15

        self.slot = 2

# defence class


# leather armor
class LeatherHat:  #
    def __init__(self):
        self.name = "Leather Cowl"
        self.value = 20

        self.strength = 0
        self.intelligence = 0
        self.defence = 8

        self.slot = 0


class LeatherTop:  #
    def __init__(self):
        self.name = "Leather Tunic"
        self.value = 20

        self.strength = 0
        self.intelligence = 0
        self.defence = 8

        self.slot = 1


class LeatherBot:  #
    def __init__(self):
        self.name = "Leather Chaps"
        self.value = 20

        self.strength = 0
        self.intelligence = 0
        self.defence = 8

        self.slot = 2


# plate armor
class PlateHat:  #
    def __init__(self):
        self.name = "Platehelm"
        self.value = 55

        self.strength = 0
        self.intelligence = 0
        self.defence = 30

        self.slot = 0


class PlateTop:  #
    def __init__(self):
        self.name = "Platebody"
        self.value = 55

        self.strength = 0
        self.intelligence = 0
        self.defence = 30

        self.slot = 1


class PlateBot:  #
    def __init__(self):
        self.name = "Platelegs"
        self.value = 55

        self.strength = 0
        self.intelligence = 0
        self.defence = 30

        self.slot = 2

# mixed class
