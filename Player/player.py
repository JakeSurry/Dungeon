import pygame as pg
from Events.events import ev
from Display.dispTypes import *
from Player.cursor import Cursor
from Items.Weapon.Melee.hands import Hands

class Player():
    def __init__(self):
        self.pos = (0, 0)
        self.img = Img('game', '@', 'green', None) 
        self.health = 3

        self.cursor = Cursor()

        self.weapons = [Hands()]
        self.items = [] 

        self.equipped = self.weapons[0]
        self.showingInv = False

        self.selectedObj = None
        self.rangeTiles = []
        self.rangeImg = Img('game', ' ', 'white', 'blue')
        self.usingItem = False

        self.collision = True
    
    def drawInfo(self, inf, color='white', backgroundColor=None):
        pg.event.post(pg.event.Event(ev.DRAWLINE, win='side', strg=inf, color=color, backgroundColor=backgroundColor))

    def toggleCursor(self):
        if self.usingItem:
            self.usingItem = False
            self.cursor.limit = []
        self.cursor.active = not self.cursor.active
        self.cursor.pos = self.pos
    
    def toggleUsingItem(self):
        self.usingItem = not self.usingItem

    def outInventory(self):
        if self.cursor.active:
            self.toggleCursor()

        if self.showingInv:
            self.cycleEquipped()
        self.showingInv = True

        self.drawInfo('weapons', 'black', 'grey')
        for weapon in self.weapons:
            if weapon == self.equipped:
                self.drawInfo(weapon.name, 'white', 'red')
            else:
                self.drawInfo(weapon.name)
        self.drawInfo(' ')
        self.drawInfo('consum.', 'black', 'grey') 
        for item in self.items:
            if item == self.equipped:
                self.drawInfo(item.nameWithAmount(), 'white', 'red')
            else:
                self.drawInfo(item.nameWithAmount())

    def cycleEquipped(self, found=False):
        for weapon in self.weapons:
            if found:
                self.equipped = weapon
                return
            if weapon == self.equipped:
                found = True

        for item in self.items:
            if found:
                self.equipped = item
                return
            if item == self.equipped:
                found = True

        self.cycleEquipped(found)
    
    def pickUp(self, obj):
        match obj.itmClass:
            case 'consumable':
                for itm in self.items:
                    if itm.itmType == obj.itmType:
                        itm.amount += obj.amount
                        self.outInventory()
                        return

                self.items.append(obj)

            case 'weapon':
                self.weapons.append(obj)
        
        self.outInventory()
    
    def drop(self, obj):
        if obj.itmClass == 'consumable':
            self.items.remove(obj)
        else:
            self.weapons.remove(obj)
        self.equipped = self.weapons[0]
        self.outInventory()

    def useItem(self, useRange, objInRange):
        self.rangeTiles = useRange

        self.toggleUsingItem()
        self.cursor.active = self.usingItem

        self.cursor.pos = self.pos

        if self.usingItem:
            self.cursor.limit = useRange
        else:
            self.cursor.limit = []

    def onKey(self, key):
        if not key == pg.K_h:
            self.usingItem = False

    def update(self):
        imgs = []
        if self.usingItem:
            for tile in self.rangeTiles:
                imgs.append((self.rangeImg, tile))
        if self.cursor.active:
            imgs.append((self.cursor.img, self.cursor.pos))
        imgs.append((self.img, self.pos))
        return imgs
        
        

            