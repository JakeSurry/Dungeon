from Display.dispTypes import *
from Item.Consumable.consumable import Consumable
from Block.block import Block

class Key(Consumable):
    def __init__(self):
        super().__init__()
        self.img = Img('game', '~', 'gold', None)
        self.itmType = 'key'
        self.range = 1

        self.keyType = 'rusty'
    
    def useItem(self, obj=None):
        self.clearInfo()

        if not issubclass(type(obj), Block):
            return self.useInfo
    
        if obj.blockType == 'chest' and obj.chestType == self.keyType and obj.locked:
            obj.locked = False
            self.useInfo.used = True
            self.useInfo.lines = obj.getShallowInfo()

            return self.useInfo
        