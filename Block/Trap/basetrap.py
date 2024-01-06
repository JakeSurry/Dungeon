from Block.block import Block

class BaseTrap(Block):
    def __init__(self, img, color, bcolor, name):
        super().__init__(img, color, bcolor, 'trap', name, False)