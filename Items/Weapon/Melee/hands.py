from Items.Weapon.Melee.basemelee import Melee
from Block.block import Block
from Display.dispTypes import *

class Hands(Melee):
    def __init__(self):
        super().__init__('hands', 'white', 1, 1, 1, True, True, False)
    
    def useItem(self, obj=None):
        self.clearInfo()

        lines = []
        if issubclass(type(obj), Block) and obj.blockType == 'chest' and not obj.locked:
            self.useInfo.itms = obj.open()
            self.useInfo.used = True
        else:
            lines.append(Line('bottom', f'you punched the {obj.name}.', 'white', None))
            lines.append(Line('bottom', 'that hurt...', 'red', None))
            lines.append(Line('bottom', '...that was stupid', 'white', None))

        self.useInfo.lines = lines
        return self.useInfo