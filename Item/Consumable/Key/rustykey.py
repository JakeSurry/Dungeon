from Item.Consumable.Key.basekey import Key

class RustyKey(Key):
    def __init__(self, amount=1):
        super().__init__()
        self.name = 'r-key'
        self.textColor = 'brown'
        self.keyType = 'rusty'

        self.amount = amount