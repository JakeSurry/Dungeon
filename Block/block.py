from Display.dispTypes import *
import pygame as pg
from Events.events import ev

class Block():
    def __init__(self, img, color, bcolor, blockType, name, solid=True):
        self.img = Img('game', img, color, bcolor)
        self.blockType = blockType
        self.solid = solid
        self.name = name

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
        lines.append(Line('side', self.blockType, 'black', 'grey'))
        lines.append(Line('side', self.name, self.img.color, None))

        return lines

    def destruct(self):
        pg.event.post(pg.event.Event(ev.DESTRUCT, obj=self))

    def update(self, tick):
        if self.animated:
            self.cycleFrames(tick)
        return self.img