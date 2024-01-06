from Items.Consumable.consumable import Consumable
from Block.block import Block

class Key(Consumable):
    def __init__(self, name, textColor, keyType, amount, held=False, canDrop=True):
        super().__init__('K', 'gold', None, textColor, name, 'key', 1, amount, held)
        self.keyType = keyType
    
    def useItem(self, obj=None):
        self.clearInfo()

        if not issubclass(type(obj), Block):
            return self.useInfo
    
        if obj.blockType == 'chest' and obj.chestType == self.keyType:
            obj.locked = False
            self.useInfo.used = True
            self.useInfo.lines = obj.getShallowInfo()

            return self.useInfo
        