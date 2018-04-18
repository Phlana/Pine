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
        # Bright Green
        # walkable generic green grass
        def __init__(self):
            self.code = '00FF80'

    class Hedge:
        # BASE
        # Dark Green
        # not walkable hedge
        def __init__(self):
            self.code = '00C040'

    # generic tree
    class TreeTL:
        # top left
        def __init__(self):
            self.code = '007000'

    class TreeTR:
        # top right
        def __init__(self):
            self.code = '007100'

    class TreeBL:
        # bottom left
        def __init__(self):
            self.code = '007200'

    class TreeBR:
        # bottom right
        def __init__(self):
            self.code = '007300'

    class Wall:
        # BASE
        # light grey
        # grey castle walls
        def __init__(self):
            self.code = 'E0E0E0'

    class Water1:
        # BASE
        # dirty aqua blue
        # blue water
        def __init__(self):
            self.code = '00A0A0'

    class FountainWater:
        # BASE
        # pale blue
        # fountain water
        def __init__(self):
            self.code = '8080F0'

