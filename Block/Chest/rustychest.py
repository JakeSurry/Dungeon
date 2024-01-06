from Block.Chest.basechest import Chest

class RustyChest(Chest):
    def __init__(self, items=[], locked=False):
        super().__init__()
        self.chestType = 'rusty'
        self.name = 'rusty chest'
        self.items = items
        self.locked = locked