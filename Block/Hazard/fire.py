from Block.Hazard.basehazard import BaseTrap
from Display.dispTypes import *

class Fire(BaseTrap):
    def __init__(self):
        super().__init__()
        self.img = Img('game', '*', 'red', None)
        self.name = 'fire'

        self.animFrames = [(Img('game', '+', 'red', None)),
                           (Img('game', '*', 'red', None))]
        self.animated = True
        self.animFPS = 2