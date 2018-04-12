"""
A file for the combat game logic
"""

import textbased
import monsters
import items
import player

class combat_turn:

	def __init__(self, monster: Monsters):
		# the number of turns elapsed
		self.turn_num = 0

		# the total exp and coins from each monster
		# self.exp_pool = # sum of each monster's exp value
		# self.coins = # sum of each monster's coin value

		# win: 0 for defeat, 1 for victory
		self.win = 0

	def next_turn(self): #
		if Player.stats.faint:
			# Player has lost the battle
			self.win = 0
			self.end_combat()

		if Player.stats.poison > 0:
			Player.stats.hp = Player.stats.hp - Player.stats.hp_max*0.06
			Player.stats.poison -= 1


		self.turn_num += 1

	def end_combat(): #
		if self.win:
			# get loot
			# increase stats/level
			Player.stats.exp_up(self.exp_pool)
		else:
			# send to revival zone

class spells:
	# list of spells
	def __init__(self):
		print("spells")