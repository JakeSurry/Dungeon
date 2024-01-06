from Display.dispTypes import *
import pygame as pg
from Events.events import ev

class Block():
    def __init__(self, img, color, bcolor, blockType, name, solid=True):
        self.img = Img('game', img, color, bcolor)
        self.blockType = blockType
        self.solid = solid
        self.name = name

    def destruct(self):
        pg.event.post(pg.event.Event(ev.DESTRUCT, obj=self))