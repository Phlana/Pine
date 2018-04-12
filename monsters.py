"""
A file for all the different monsters that can be fought.

tier: a value assigned to each monster so you wont face extremely hard monsters from the start.

exp: the amount of experience you will gain from defeating this monster
coins: the amount of coins rewarded to player for defeating this monster

unique: unique loot from a monster
chance: the chance the unique loot will drop from the monster

class :
	def __init__(self):
		self.tier = 

		self.hp_max = 
		self.hp = self.hp_max

		self.strength = 
		self.intellegence = 
		self.defence = 
		self.speed = 

		self.exp = 
		self.coins = 

		self.unique = 
		self.chance = 
"""

import items

class Monsters:
	def __init__(self): #
		self

	class goblin: #
		def __init__(self):
			# standard basic monster
			self.tier = 0

			self.hp_max = 900
			self.hp = self.hp_max

			self.strength = 5
			self.intellegence = 0
			self.defence = 7
			self.speed = 100

			self.exp = 50
			self.coins = 

			self.unique = 
			self.chance = 

	class zombie: #
		# high hp but low defence monster
		def __init__(self):
			self.tier = 

			self.hp_max = 1400
			self.hp = self.hp_max

			self.strength = 3
			self.intellegence = 0
			self.defence = 1
			self.speed = 70

			self.exp = 80
			self.coins = 

			self.unique = 
			self.chance = 

	class slime: #
		# slimes have a special ability to spawn 1-3 baby_slime upon death
		def __init__(self):
			self.tier = 

			self.hp_max = 800
			self.hp = self.hp_max

			self.strength = 
			self.intellegence = 
			self.defence = 
			self.speed = 85

			self.exp = 
			self.coins = 

			self.unique = 
			self.chance = 

	class baby_slime: #
		def __init__(self):
			self.tier = 

			self.hp_max = 200
			self.hp = self.hp_max

			self.strength = 
			self.intellegence = 
			self.defence = 
			self.speed = 125

			self.exp = 
			self.coins = 

			self.unique = 
			self.chance = 

	class bat: #
		def __init__(self):
			self.tier = 

			self.hp_max = 100
			self.hp = self.hp_max

			self.strength = 
			self.intellegence = 
			self.defence = 
			self.speed = 160

			self.exp = 
			self.coins = 

			self.unique = 
			self.chance = 

