from Display.dispTypes import *
from Item.Consumable.consumable import Consumable

class Coin(Consumable):
    def __init__(self, amount=1):
        super().__init__()
        self.img = Img('game', '.', 'gold', None)
        self.itmType = 'coin'
        self.name = 'coin'
        
        self.amount = amount