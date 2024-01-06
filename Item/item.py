from Display.dispTypes import *
import pygame as pg
from Events.events import ev

class UseInfo():
    def __init__(self):
        self.used = False
        self.itms = []
        self.imgs = []
        self.lines = []

class Item():
    def __init__(self):
        self.img = Img('game', '?', 'purple', None)
        self.name = 'item'
        self.itmClass = 'none'
        self.itmType = 'none'
        self.range = 0
        self.textColor = 'white'
        self.solid = False
        self.held = False
        self.canHold = True
        self.canDrop = True
        
        self.useInfo = UseInfo()
    
    def getShallowInfo(self):
        lines = []
        lines.append(Line('side', self.itmClass, 'black', 'grey'))
        lines.append(Line('side', self.name, self.textColor, None))
        lines.append(Line('side', 'type', 'black', 'grey'))
        lines.append(Line('side', self.itmType, self.img.color, None))

        return lines

    def pickUp(self):
        self.held = True

    def drop(self):
        self.held = False

    def useItem(self, obj=None):
        return self.useInfo
    
    def getUseRange(self, originPos):
        useRange = []
        for x in range(self.range*2+1):
            useRange.append((originPos[0]-self.range+x, originPos[1]))
        for y in range(self.range*2+1):
            useRange.append((originPos[0], originPos[1]-self.range+y))

        return useRange

    def clearInfo(self):
        self.useInfo = UseInfo()
    
    def rmFromLevel(self):
        pg.event.post(pg.event.Event(ev.DESTRUCT, obj=self))

    def consumeItem(self):
        self.amount -= 1
        rmItem = False
        if self.amount == 0:
            rmItem = True

        return rmItem

    def update(self, tick):
        if not self.held:
            return self.img
        return None
    