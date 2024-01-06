from Display.dispTypes import *
from Item.Weapon.weapon import Weapon

class Melee(Weapon):
    def __init__(self):
        super().__init__()
        self.img = Img('game', '/', 'white', None)
        self.itmType = 'melee'
        self.range = 1
