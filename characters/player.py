"""
A file for the Player information
"""

# import events


class Player:

    def __init__(self):
        self.name = ""
        self.stats = self.Stats()

        # coins is the amount of coins you have
        self.coins = 0

        # inv is what you carry
        # inv_size is how many items you can carry
        self.inv = list()
        self.inv_size = 20

    class Stats:
        # Player stats
        def __init__(self):
            # hp_max is the maximum hitpoints you can have
            # hp is the amount of hitpoints you have currently
            self.hp_max = 1000
            self.hp = self.hp_max

            # strength adds one point of damage done by melee weapons per value of strength
            self.strength = 0
            # intelligence adds one point of damage done by magic weapons per value of intelligence
            self.intelligence = 0
            # defence removes one point of damage taken per value of defence
            self.defence = 0
            # speed dictates order of attacking in combat
            self.speed = 100

            # exp is your experience
            # exp_max is your experience needed to level up
            # level is your combat level
            self.exp = 0
            self.exp_max = 100
            self.level = 1

            # value for poison is amount of turns until poison wears off
            # deals percent health damage until self.poison = 0
            self.poison = 0

            # status
            self.faint = 0

    def request_name(self):
        print("Enter name: ")
        self.name = input().strip()

    def str_up(self, strength: int):
        self.stats.strength += strength

    def str_down(self, strength: int):
        self.stats.strength -= strength

    def int_up(self, intelligence: int):
        self.stats.intelligence += intelligence

    def int_down(self, intelligence: int):
        self.stats.intelligence -= intelligence

    def def_up(self, defence: int):
        self.stats.defence += defence

    def def_down(self, defence: int):
        self.stats.defence -= defence

    def spd_up(self, speed: int):
        self.stats.speed += speed

    def spd_down(self, speed: int):
        self.stats.speed -= speed

    def poison(self, duration: int):
        # Player has been poisoned
        # poison duration stacks with subsequent poisons
        self.stats.poison += duration

    def antidote(self):
        # removes poison
        self.stats.poison = 0

    def damage(self, hp: int):
        self.stats.hp -= hp
        if self.stats.hp < 1:
            # Player has been knocked out
            self.stats.faint = 1

    def heal(self, hp: int):
        self.stats.hp += hp
        # set health back down to max
        if self.stats.hp > self.stats.hp_max:
            self.stats.hp = self.stats.hp_max

    # def level_up(self):
    #   self.level += 1
    #   events.level_up()

    def exp_up(self, exp: int):
        self.stats.exp += exp
        if self.stats.exp > self.stats.exp_max:
            # Events.level_up()
            self.stats.level += 1
            # remaining experience after level up
            self.stats.exp = self.stats.exp - self.stats.exp_max
            self.stats.exp_max = self.stats.exp_max * 1.6

    def inv_add(self, item):  #
        if len(self.inv) == self.inv_size:
            # inv full
            print("Inventory full")
        else:
            self.inv.append(item)
            # keep inventory sorted
            self.inv.sort()

    def inv_remove(self, item):  # Items are in a class: need to make it remove with matching Item.name
        for index, thing in enumerate(self.inv):
            if thing.name == item:
                del self.inv[index]
                return
        raise IndexError

    def inv_increase(self, size: int):
        self.inv_size += size

    def coins_get(self, amount: int):
        self.coins += amount

    def coins_remove(self, amount: int):  #
        if self.coins < amount:
            # not enough coins
            print("Not enough coins")
        else:
            self.coins -= amount
