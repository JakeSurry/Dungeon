from Hazard.Lasting.baselasting import Lasting
from Display.dispTypes import *

class Fire(Lasting):
    def __init__(self):
        super().__init__()
        self.img = Img('game', '*', 'red', None)
        self.name = 'fire'
        self.dmg = 1
        self.dmgType = 'fire'

        self.animFrames = [(Img('game', '+', 'red', None)),
                           (Img('game', '*', 'red', None))]
        self.animated = True
        self.animFPS = 2

    def applyEffect(self, obj=None):
        self.clearInfo()
        if not obj == None and obj.canTakeDamage:
            self.effecInfo.applied = True
            obj.takeDamage(self.dmg, self.dmgType)
        
        return self.effectInfo
            