from Events.events import ev
import pygame as pg

from Block.Chest.rustychest import RustyChest
from Item.Consumable.Key.rustykey import RustyKey
from Item.Consumable.Coin.coin import Coin
from Hazard.Lasting.fire import Fire
from Block.block import Block
from Item.item import Item

level1 = {
        (10, 10):[RustyChest([Coin(3), Coin(6), Coin(1)], True)],
        (4, 20): [RustyChest([RustyKey()])],
        #(20, 2): [RustyKey()],
        (20, 20):[Fire()],
        (15, 15):[Block()],
        (11, 12):[Item()]
        }


class Map():
    def __init__(self, player, level=level1):
        self.player = player
        self.level = level
        self.blocked = []
        self.initObjPositions()
        self.getBorders()
        #self.out = out
    
    def getBorders(self):
        borders = []
        for x in range(-1, 27, 27):
            for y in range(-1, 27):
                borders.append((x, y))
        for y in range(-1, 27, 27):
            for x in range(0, 26):
                borders.append((x, y))
        self.borders = borders
    
    def initObjPositions(self):
        self.objPositions = {}
        for pos, objects in self.level.items():
            for obj in objects:
                self.objPositions[obj] = pos

    def onKey(self, key):
        mods = pg.key.get_mods()
        self.lastPressedKey = key
        match key:
            case pg.K_d if mods & pg.KMOD_SHIFT:
                self.drop(self.player)
            case pg.K_w:
                self.playerMove((0, -1))
            case pg.K_a:
                self.playerMove((-1, 0))
            case pg.K_s:
                self.playerMove((0, 1))
            case pg.K_d:
                self.playerMove((1, 0))
            case pg.K_i:
                self.player.outInventory()
            case pg.K_c:
                self.player.toggleCursor()
            case pg.K_v:
                self.view(self.player.cursor.pos)
            case pg.K_e:
                self.pickUp(self.player)
        #self.player.onKey(key)

    def view(self, cpos):
        if self.player.cursor.active:
            self.player.showingInv = False

            objects = self.getObjects(cpos)

            for obj in objects:
                lines = obj.getShallowInfo()
                for line in lines:
                    self.dispLine(line)

            self.clearWin('side')
    
    def pickUp(self, entity):
        objects = self.getObjects(entity.pos)
        for obj in objects:
            if obj.canHold:
                obj.pickUp()
                entity.pickUp(obj)
                self.rmFromLevel(obj)
                return

        self.useItem(entity)
            
    def drop(self, entity):
        obj = entity.equipped
        if obj.canDrop:
            obj.drop()
            entity.drop(obj)

            self.addToLevel(entity.pos, obj)

    def move(self, curPos, deltaPos, collision, limit=[]):
        newPos = (curPos[0]+deltaPos[0], curPos[1]+deltaPos[1])
        if collision and newPos in self.blocked:
            return curPos
        if newPos in self.borders:
            return curPos
        if not limit == [] and not newPos in limit:
            return curPos
        return newPos
    
    def playerMove(self, dir):
        if self.player.cursor.active:
            self.player.cursor.pos = self.move(self.player.cursor.pos, dir, self.player.cursor.collision, self.player.cursor.limit)
        else:
            self.player.pos = self.move(self.player.pos, dir, self.player.collision)

    def useItem(self, entity):
        useInfo = None
        
        useRange = entity.equipped.getUseRange(entity.pos)

        #TODO Don't like this, change objInRange to match same structure as level (key=pos, value=obj)
        objInRange = {}
        for tile in useRange:
            if tile in self.level.keys():
                for obj in self.level[tile]:
                    objInRange[obj] = tile

        if entity.usingItem:
            for obj, pos in objInRange.items():
                if pos == entity.cursor.pos:
                    useInfo = entity.equipped.useItem(obj)
                    break
        if not useInfo == None:
            self.interpUseInfo(useInfo, entity)

        entity.useItem(useRange, objInRange)
    
    def interpUseInfo(self, useInfo, entity):
        if useInfo.used and entity.equipped.itmClass == 'consumable':
            rmItem = entity.equipped.consumeItem()
            if rmItem:
                entity.items.remove(entity.equipped)
                entity.equipped = entity.weapons[0]

        for itm in useInfo.itms:
            self.addToLevel((itm[1][0]+entity.pos[0], itm[1][1]+entity.pos[1]), itm[0])
        for img in useInfo.imgs:
            self.dispImg(img[0], img[1])
        for line in useInfo.lines:
            self.dispLine(line)

    def getBlocked(self):
        self.blocked = []
        for pos, objects in self.level.items():
            for obj in objects:
                if obj.solid == True:
                    self.blocked.append(pos)
                    break

    def addToLevel(self, pos, obj):
        if pos in self.level.keys():
            self.level[pos].append(obj)
        else:
            self.level[pos] = [obj]
        self.objPositions[obj] = pos
    
    def rmFromLevel(self, obj):
        pos = self.objPositions[obj]
        self.level[pos].remove(obj)
        del self.objPositions[obj]

        if self.level[pos] == []:
            del self.level[pos]
    
    def getObjects(self, pos):
        objects = []
        if pos in self.level.keys():
            objects += self.level[pos]

        return objects

    def dispImg(self, img, pos):
        if img == None:
            return
        pg.event.post(pg.event.Event(ev.DRAWCHAR, win=img.win, char=img.img, pos=pos, color=img.color, backgroundColor=img.bcolor))
    
    def dispLine(self, line):
        if line == None:
            return
        pg.event.post(pg.event.Event(ev.DRAWLINE, win=line.win, strg=line.string, color=line.color, backgroundColor=line.bcolor))
    
    def clearWin(self, win):
        pg.event.post(pg.event.Event(ev.CLEARWIN, win=win))

    def update(self, tick):
        self.getBlocked()
        self.applyEffects(self.player)

        imgs = self.player.update()
        for img in imgs:
            self.dispImg(img[0], img[1])

        for obj in self.getObjects(self.player.pos):
            if obj.objType == 'hazard':
                obj.applyEffects(self.player)

        for pos, objects in self.level.items():
            for obj in objects:
                img = obj.update(tick)
                self.dispImg(img, pos)
        
