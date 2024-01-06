from Block.Chest.basechest import Chest

class RustyChest(Chest):
    def __init__(self, items=[], locked=False):
        super().__init__('rusty', 'rusty chest', items, locked)