
from Items.item import Item

class Melee(Item):
    def __init__(self, name, textColor, damage, itmRange, aps, held=False, canHold=True, canDrop=True):
        super().__init__('S', 'white', None, textColor, name, 'weapon', 'melee', itmRange, False, held, canHold, canDrop)
        self.damage = damage
        self.range = range
        self.aps = aps