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
import player

class Items:

	# consumables

	'''
	class :
		def __init__(self):
			self.name = 
			self.value = 

		def consume(self):
			Player.inv_remove(self.name)
	'''

	# healing

	class herb: #
		# Consumable that heals 600 health
		def __init__(self):
			self.name = "Herb"
			self.value = 20

		def consume(self):
			Player.inv_remove(self.name)
			Player.stats.heal(600)

	class smallhealthpotion:
		# Consumable that heals 1300 health
		def __init__(self):
			self.name = "Small Health Potion"
			self.value = 55

		def consume(self):
			Player.inv_remove(self.name)
			Player.stats.heal(1300)

	class mediumhealthpotion:
		# Consumable that heals 2100 health
		def __init__(self):
			self.name = "Medium Health Potion"
			self.value = 115

		def consume(self):
			Player.inv_remove(self.name)
			Player.stats.heal(2100)

	class largehealthpotion:
		# Consumable that heals 3300 health
		def __init__(self):
			self.name = "Large Health Potion"
			self.value = 190

		def consume(self):
			Player.inv_remove(self.name)
			Player.stats.heal(3300)

	# boosts

	class strengthpot: #
		# Consumable that boosts strength temporarily
		def __init__(self):
			self.name = "Strength Potion"
			self.value = 0

		def consume(self):
			Player.inv_remove(self.name)
			# Player.strength += 5 for 3 turns

	# other

	class antidote: #
		# consumable that cure poison
		def __init__(self):
			self.name = "Antidote"
			self.value = 0

		def consume(self):
			Player.inv_remove(self.name)
			Player.stats.antidote()



	# armor sets

	'''
	class : #
		def __init__(self):
			self.name = ""
			self.value = 

			self.strength = 
			self.intellegence = 
			self.defence = 

			self.slot = 0

	class : #
		def __init__(self):
			self.name = ""
			self.value = 

			self.strength = 
			self.intellegence = 
			self.defence = 

			self.slot = 1

	class : #
		def __init__(self):
			self.name = ""
			self.value = 

			self.strength = 
			self.intellegence = 
			self.defence = 

			self.slot = 2
	'''

	# starter

	class clothhat: #
		def __init__(self):
			self.name = "Cloth Hat"
			self.value = 5

			self.strength = 0
			self.intellegence = 0
			self.defence = 0

			self.slot = 0

	class clothtop: #
		def __init__(self):
			self.name = "Cloth Shirt"
			self.value = 5

			self.strength = 0
			self.intellegence = 0
			self.defence = 0

			self.slot = 1

	class clothbot: #
		def __init__(self):
			self.name = "Cloth Pants"
			self.value = 5

			self.strength = 0
			self.intellegence = 0
			self.defence = 0

			self.slot = 2

	# strength class

	# warrior armor

	class warriorhat: #
		def __init__(self):
			self.name = "Warrior Helmet"
			self.value = 70

			self.strength = 25
			self.intellegence = 0
			self.defence = 10

			self.slot = 0

	class warriortop: #
		def __init__(self):
			self.name = "Warrior Chainmail"
			self.value = 70

			self.strength = 25
			self.intellegence = 0
			self.defence = 10

			self.slot = 1

	class warriorbot: #
		def __init__(self):
			self.name = "Warrior Leggings"
			self.value = 70

			self.strength = 25
			self.intellegence = 0
			self.defence = 10

			self.slot = 2

	# berserker armor

	class berserkerhat: #
		def __init__(self):
			self.name = "Berserker Helmet"
			self.value = 120

			self.strength = 45
			self.intellegence = 0
			self.defence = 10
			self.slot = 0

	class berserkertop: #
		def __init__(self):
			self.name = "Berserker "
			self.value = 120

			self.strength = 45
			self.intellegence = 0
			self.defence = 10

			self.slot = 1

	class berserkerbot: #
		def __init__(self):
			self.name = "Berserker "
			self.value = 120

			self.strength = 45
			self.intellegence = 0
			self.defence = 10

			self.slot = 2

	# intellegence class

	# wizard robes

	class wizardhat: #
		def __init__(self):
			self.name = "Wizard Hat"
			self.value = 40

			self.strength = 0
			self.intellegence = 10
			self.defence = 5

			self.slot = 0

	class wizardtop: #
		def __init__(self):
			self.name = "Wizard Robe Top"
			self.value = 40

			self.strength = 0
			self.intellegence = 10
			self.defence = 5

			self.slot = 1

	class wizardbot: #
		def __init__(self):
			self.name = "Wizard Robe Bottom"
			self.value = 40

			self.strength = 0
			self.intellegence = 10
			self.defence = 5

			self.slot = 2

	# arcanist robes

	class arcanisthat: #
		def __init__(self):
			self.name = "Arcanist Hat"
			self.value = 90

			self.strength = 0
			self.intellegence = 45
			self.defence = 15

			self.slot = 0

	class arcanisttop: #
		def __init__(self):
			self.name = "Arcanist Robe Top"
			self.value = 90

			self.strength = 0
			self.intellegence = 45
			self.defence = 15

			self.slot = 1

	class arcanistbot: #
		def __init__(self):
			self.name = "Arcanist Robe Bottom"
			self.value = 90

			self.strength = 0
			self.intellegence = 45
			self.defence = 15

			self.slot = 2

	# defence class

	# leather armor

	class leatherhat: #
		def __init__(self):
			self.name = "Leather Cowl"
			self.value = 20

			self.strength = 0
			self.intellegence = 0
			self.defence = 8

			self.slot = 0

	class leathertop: #
		def __init__(self):
			self.name = "Leather Tunic"
			self.value = 20

			self.strength = 0
			self.intellegence = 0
			self.defence = 8

			self.slot = 1

	class leatherbot: #
		def __init__(self):
			self.name = "Leather Chaps"
			self.value = 20

			self.strength = 0
			self.intellegence = 0
			self.defence = 8

			self.slot = 2

	# plate armor

	class platehat #
		def __init__(self):
			self.name = "Platehelm"
			self.value = 55

			self.strength = 0
			self.intellegence = 0
			self.defence = 30

			self.slot = 0

	class platetop: #
		def __init__(self):
			self.name = "Platebody"
			self.value = 55

			self.strength = 0
			self.intellegence = 0
			self.defence = 30

			self.slot = 1

	class platebot: #
		def __init__(self):
			self.name = "Platelegs"
			self.value = 55

			self.strength = 0
			self.intellegence = 0
			self.defence = 30

			self.slot = 2

	# mixed class