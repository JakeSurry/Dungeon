from Items.Consumable.Key.basekey import Key

class RustyKey(Key):
    def __init__(self, amount=1):
        super().__init__('rusty key', 'brown', 'rusty', amount)