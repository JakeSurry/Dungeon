from Block.Trap.basetrap import BaseTrap
from Display.dispTypes import *

class Fire(BaseTrap):
    def __init__(self):
        super().__init__('*', 'red', None, 'fire')

        self.animFrames.append(Img('game', '+', 'red', None))
        
        self.animated = True
        self.animFPS = 3