from Items.item import Item
from Display.dispTypes import *

class Consumable(Item):
    def __init__(self, img, color, bcolor, textcolor, name, itemType, itmRange, amount, held):
        super().__init__(img, color, bcolor, textcolor, name, 'consumable', itemType, itmRange, False, held)
        self.amount = amount

    def getShallowInfo(self):
        lines = []
        lines.append(Line('side', 'consum.', 'black', 'grey'))
        lines.append(Line('side', self.nameWithAmount(), self.textColor, None))
        lines.append(Line('side', 'type', 'black', 'grey'))
        lines.append(Line('side', self.itmType, self.img.color, None))

        return lines
    def nameWithAmount(self):
        return f'{self.name} x{self.amount}'