from Display.dispTypes import *

class EffectInfo():
    def __init__(self):
        self.applied = False
        self.dmg = 0
        self.dmgType = 'none'
        self.itms = []
        self.imgs = []
        self.lines = []

class Hazard():
    def __init__(self):
        self.img = Img('game', '-', 'purple', None)
        self.name = 'hazard'
        self.objType = 'hazard'
        self.hazType = 'none'
        self.solid = False
        self.effectDesc = 'unknown'

        self.effecInfo = EffectInfo()

        self.animated = False
        self.animFrames = [self.img]
        self.animFPS = 1
        self.curFrame = 0
    
    def cycleFrames(self, tick):
        if tick%(60/self.animFPS) == 1:
            if self.curFrame+1 == len(self.animFrames):
                self.curFrame = -1
            self.curFrame += 1
            self.img = self.animFrames[self.curFrame]

    def getShallowInfo(self):
        lines = []
        lines.append(Line('side', self.hazType, 'black', 'grey'))
        lines.append(Line('side', self.name, self.img.color, None))
        lines.append(Line('side', 'effect', 'black', 'grey'))
        lines.append(Line('side', self.effectDesc, 'white', None))

        return lines

    def clearInfo(self):
        self.effectInfo = EffectInfo()
    
    def applyEffect(self):
        pass

    def destruct(self):
        pass

    def update(self, tick):
        self.applyEffect(tick)
        if self.animated:
            self.cycleFrames(tick)
        return self.img
