from Item.item import Item
from Display.dispTypes import *

class Consumable(Item):
    def __init__(self):
        super().__init__()
        self.amount = 1
        self.itmClass = 'consumable'

    def getShallowInfo(self):
        lines = []
        lines.append(Line('side', 'consum.', 'black', 'grey'))
        lines.append(Line('side', self.nameWithAmount(), self.textColor, None))
        lines.append(Line('side', 'type', 'black', 'grey'))
        lines.append(Line('side', self.itmType, self.img.color, None))

        return lines
    def nameWithAmount(self):
        return f'{self.name} x{self.amount}'