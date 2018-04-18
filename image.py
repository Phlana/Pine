"""
file for drawing images to screen
"""

import pyglet
from characters.player import *


def center_anchor(image):
    """
    centers the anchor on images
    """
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2
