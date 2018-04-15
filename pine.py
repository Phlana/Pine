"""
Main file for the game logic
"""

from items.items import *
from characters.player import *
from world.environment import *


class Game:
    def __init__(self):
        # environment initialization
        self.environment = Environment()

        self.player = Player()
        self.player.request_name()
        # self.herb = Herb()
        # self.smallhealthpot = SmallHealthPotion()
        # self.mediumhealthpot = MediumHealthPotion()
        # self.largehealthpot = LargeHealthPotion()
        # self.strengthpot = StrengthPot()
        # self.antidote = Antidote()


if __name__ == "__main__":
    game = Game()

    # testing
    game.player.inv_add(Herb())
    game.player.inv_remove("Herb")

    if game.player.stats.poison:  # if poisoned
        print(game.player.name, "(Poisoned)")
    else:
        print(game.player.name)
    print()
    print()
    print("Level", game.player.stats.level)
    print("Experience:", game.player.stats.exp, "/", game.player.stats.exp_max)
    print()
    print("Health:", game.player.stats.hp, "/", game.player.stats.hp_max)
    print()
    print("Strength:", game.player.stats.strength)
    print("Intelligence:", game.player.stats.intelligence)
    print("Defence:", game.player.stats.defence)
    print("Speed:", game.player.stats.speed)
    print()
    print("Coins:", game.player.coins)
    print("Inventory:", len(game.player.inv), "/", game.player.inv_size)

    # window testing
    # while True:
    #     key = pygame.key.get_pressed()
    #     if key[K_ESCAPE]:
    #         break
    #     continue
