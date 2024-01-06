from Display.dispTypes import *
from Items.Consumable.consumable import Consumable

class Coin(Consumable):
    def __init__(self, amount):
        img = Img('game', '.', 'gold', 'none')
        super().__init__('.', 'gold', None, 'white', 'coin', 'coin', 0, amount, False)