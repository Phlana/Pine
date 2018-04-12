"""
A file for the different events that can occur
Events bring about changes on screen
"""

from player import Player


class Events:
	class Shop:
		def __init__(self):
			self.item1 = 
			self.item2 = 
			self.item3 = 
	def call_shop():
		# brings up the shop menu

	def call_help():
		# displays help on how to play

	def level_up():

	def call_inventory():
		if len(Player.inv) != 0:
	        # list items in inventory
            for x in range(len(Player.inv)):
	            print(Player.inv[x].name)
	    else:
	        print("Empty")

	def call_stats():
		# displays stats
		if Player.stats.poison: # if poisoned
			print(Player.name, "(Poisoned)")
		else:
			print(Player.name)
		print()
		print()
		print("Level", Player.stats.level)
		print("Experience:", Player.stats.exp, "/", Player.stats.exp_max)
		print()
		print("Health:", Player.stats.hp, "/", Player.stats.hp_max)
		print()
		print("Strength:", Player.stats.strength)
		print("Intellegence:", Player.stats.intellegence)
		print("Defence:", Player.stats.defence)
		print("Speed:", Player.stats.speed)
		print()
		print("Coins:", Player.coins)
		print("Inventory:", len(Player.inv), "/", Player.inv_size)

	def call_map():
		# displays map

	def call_surroundings():
		# displays surroundings

	def call_combat(monster):
		# initializes combat with specified monster

	def call dialogue():
