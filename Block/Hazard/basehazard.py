from Block.block import Block

class BaseTrap(Block):
    def __init__(self):
        super().__init__()
        self.blockType = 'hazard'
        self.solid = False