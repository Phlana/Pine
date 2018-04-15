"""
I want to be able to open up the map image where each pixel with a specific color is a different tile type.
For example the color FF6200 (an orange color) could be used to represent a lava pool where the player cannot traverse.
Thus, the world the game takes place in will open up an image that will be used to play the game.
Color detection would be very specific: the color FF6201 could be used for a slight variation in lava texture but still
appear the same in the image file.

Some conventions for choosing the color codes
    - The last digit of the code should be either 0, 2, 4, 6, or 8
      if you look at a numpad (https://i.imgur.com/EyZPJzH.jpg), the numbers correspond to a direction

    - Any obviously red color will be doors/entrances. The red colors will be found in pairs in the map image.
      These tiles will teleport the player to the other tile in the color pair.
"""

from world.map import *


class Environment:
    def __init__(self):

        # all of the different tiles
        self.tile = Tile()

    def read_pix(self, pix_x, pix_y):
        # reads a color value of a pixel at specified location as RGB
        # returns its equivalent hex code
        # rgb = self.world_map.get_at((pix_x, pix_y))
        # return '%02x%02x%02x' % rgb
        pass

    # def build_world(self):
    #     # building world
    #     for x in range(1, self.image_x+1):
    #         for y in range(1, self.image_y+1):
    #             # hex_color = self.read_pix(x, y)
    #             # now find the tile matching this hex color

