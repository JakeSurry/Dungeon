from Display.dispTypes import *
from Block.block import Block

class Chest(Block):
    def __init__(self, chestType, name, items=[], locked=False):
        super().__init__('C', 'brown', None, 'chest', name, True)
        self.chestType = chestType
        self.items = items
        self.locked = locked
        self.getStatus()
        self.solid = True
    
    def getShallowInfo(self):
        lines = []
        lines.append(Line('side', 'object', 'black', 'grey'))
        lines.append(Line('side', 'chest', self.img.color, None))
        lines.append(Line('side', 'type', 'black', 'grey'))
        lines.append(Line('side', self.chestType, 'white', None))
        lines.append(Line('side', 'status', 'black', 'grey'))
        self.getStatus()
        lines.append(Line('side', self.status, self.c, None))
        lines.append(Line('side', 'items', 'black', 'grey'))
        if self.locked:
            lines.append(Line('side', 'unknown', 'red', None))
        else:
            if not self.items:
                lines.append(Line('side', 'empty', 'white', None))
                return lines

            for itm in self.items:
                lines.append(Line('side', itm.nameWithAmount(), 'white', None))

        return lines

    def getStatus(self):
        if self.locked:
            self.status = 'locked'
            self.c = 'red'
        else:
            self.status = 'unlocked'
            self.c = 'green'

    def open(self):
        spiral = ((0, 0), (1, 0), (0, -1), (-1, 0), (0, 1))
        itms = []
        for i, itm in enumerate(self.items):
            itms.append((itm, spiral[i]))
        
        self.destruct()
        return itms
            
    def update(self):
        return self.img