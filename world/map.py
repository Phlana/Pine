"""
A file for associating the map's different colored pixels to different tiles.

Some conventions for choosing the color codes
    - The last digit of the code should be either 0, 2, 4, 6, or 8
      if you look at a numpad (https://i.imgur.com/EyZPJzH.jpg), the numbers correspond to a direction

Pixel color codes and what they represent:
    FF6200 - lava


"""


class Lava:
    def __init__(self):
        self.code = 'FF6200'
