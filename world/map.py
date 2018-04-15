"""
A file for associating the map's different colored pixels to different tiles.

Some conventions for choosing the color codes
    - The last digit of the code should be either 0, 2, 4, 6, or 8
      if you look at a numpad (https://i.imgur.com/EyZPJzH.jpg), the numbers correspond to a direction

Pixel color codes and what they represent:
    FF6200 - lava
"""


class Tile:
    def __init__(self):
        self.lava = self.Lava()
        self.grass = self.Grass()
        self.wall = self.Wall()
        self.water1 = self.Water1()

    class Lava:
        # BASE
        # orange lava
        def __init__(self):
            self.code = 'FF6200'

    class Grass:
        # BASE
        # walkable generic green grass
        def __init__(self):
            self.code = '00FF80'

    class Wall:
        # BASE
        # grey castle walls
        def __init__(self):
            self.code = 'E0E0E0'

    class Water1:
        # BASE
        # blue water
        def __init__(self):
            self.code = '009999'
