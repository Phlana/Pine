"""
A file for storing the map, as well as sub maps such as house interiors, caves, and dungeons
"""


class WorldMap:
    def __init__(self):
        self.maplist = [[0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0]]


    class House_1:
        def __init__(self):
            self.maplist = [[0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0]]
