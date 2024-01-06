from Item.item import Item

class Weapon(Item):
    def __init__(self):
        super().__init__()
        self.itmClass = 'weapon'

        self.damage = 0
        self.aps = 1