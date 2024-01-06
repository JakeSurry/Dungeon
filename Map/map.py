from Events.events import ev
import pygame as pg

from Block.Chest.rustychest import RustyChest
from Items.Consumable.Key.rustykey import RustyKey
from Items.Consumable.Coin.coin import Coin
from Block.Trap.fire import Fire

level1 = {RustyChest([Coin(3), Coin(6), Coin(1)], True):(10, 10),
          RustyChest([Coin(2)]):(4, 20),
          RustyKey():(20, 2),
          Fire():(20, 20)}

class Map():
    def __init__(self, player, level=level1):
        self.player = player
        self.level = level
        self.blocked = []
        self.getBorders()
        #self.out = out
    
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
            for obj, pos in self.level.items():
                if pos == cpos:
                    lines = obj.getShallowInfo()
                    for line in lines:
                        self.dispLine(line)
                    return

            self.clearWin('side')
    
    def pickUp(self, entity):
        for obj, pos in self.level.items():
            if pos == entity.pos and obj.canHold:
                obj.pickUp()
                entity.pickUp(obj)
                return
            
        self.useItem(entity)
            
    def drop(self, entity):
        obj = entity.equipped
        if obj.canDrop:
            obj.drop()
            entity.drop(obj)
            self.level[obj]=entity.pos

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
        itm = entity.equipped
        useInfo = None
        
        useRange = []
        objInRange = {}
        pos = entity.pos

        for x in range(itm.itmRange*2+1):
            useRange.append((pos[0]-itm.itmRange+x, pos[1]))
        for y in range(itm.itmRange*2+1):
            useRange.append((pos[0], pos[1]-itm.itmRange+y))
        
        for obj, pos in self.level.items():
            if pos in useRange:
                objInRange[obj] = pos

        if entity.usingItem:
            for obj, pos in objInRange.items():
                if pos == entity.cursor.pos:
                    useInfo = itm.useItem(obj)
                    break
            if not useInfo == None:
                if useInfo.used and itm.itmClass == 'consumable':
                    entity.items.remove(itm)
                    entity.equipped = entity.weapons[0]

                for itm in useInfo.itms:
                    self.level[itm[0]] = (itm[1][0]+pos[0], itm[1][1]+pos[1])
                for img in useInfo.imgs:
                    self.dispImg(img[0], img[1])
                for line in useInfo.lines:
                    self.dispLine(line)

        entity.useItem(useRange, objInRange)
        
    def getBlocked(self):
        self.blocked = []
        for obj, pos in self.level.items():
            if obj.solid == True:
                self.blocked.append(pos)
    
    def getBorders(self):
        borders = []
        for x in range(-1, 27, 27):
            for y in range(-1, 27):
                borders.append((x, y))
        for y in range(-1, 27, 27):
            for x in range(0, 26):
                borders.append((x, y))
        self.borders = borders

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
    
    def destruct(self, obj):
        del self.level[obj]

    def update(self, tick):
        self.getBlocked()

        imgs = self.player.update()
        for img in imgs:
            self.dispImg(img[0], img[1])

        for obj, pos in self.level.items():
            img = obj.update(tick)
            self.dispImg(img, pos)