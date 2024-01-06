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
    def __init__(self, img, color, bcolor, textColor, name, itmClass, itmType, itmRange, solid=False, held=False, canHold=True, canDrop=True):
        self.baseImg = Img('game', img, color, bcolor)
        self.img = self.baseImg
        self.name = name
        self.itmClass = itmClass
        self.itmType = itmType
        self.itmRange = itmRange
        self.textColor = textColor
        self.solid = solid
        self.held = held
        self.canHold = canHold
        self.canDrop = canDrop
        
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
        self.img = None
        self.destruct()

    def drop(self):
        self.held = False
        self.img = self.baseImg

    def useItem(self, obj=None):
        return self.useInfo
    
    def clearInfo(self):
        self.useInfo = UseInfo()
    
    def destruct(self):
        pg.event.post(pg.event.Event(ev.DESTRUCT, obj=self))

    def update(self):
        if not self.held:
            return self.img
        return None
    