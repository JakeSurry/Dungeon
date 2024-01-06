from Display.dispTypes import *

class Cursor():
    def __init__(self):
        self.active = False
        self.img = Img('game', ' ', 'grey', 'grey')
        self.collision = False
        self.pos = (0, 0)
        self.limit = []