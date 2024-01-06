import pygame as pg
from Display.colors import Colors as c

SCALE = 28

class Output():
    def __init__(self):
        pg.init()
        pg.font.init()

        self.mainWin = pg.display.set_mode((36*SCALE, 36*SCALE))
        self.font = pg.font.Font("Assets\Font\square.ttf", SCALE)

        self.initSideWin()
        self.initBottomWin()
        self.initGameWin()
        self.initBorders()

        pg.display.set_caption('Tiles')
        pg.display.flip()

    def initSideWin(self):
        self.sideWin = pg.Surface((9*SCALE, 26*SCALE))
        self.sideQueue = []
        self.sideChange = True
    
    def initBottomWin(self):
        self.bottomWin = pg.Surface((36*SCALE, 9*SCALE))
        self.bottomQueue = []
        self.bottomChange = True

    def initGameWin(self):
        self.gameWin = pg.Surface((26*SCALE, 26*SCALE))
        self.gameChange = True

    def initBorders(self):
        pole = self.ascii('|')
        for i in range(26):
            self.mainWin.blit(pole, (26*SCALE, i*SCALE))

        dash = self.ascii('-')
        for i in range(36):
            self.mainWin.blit(dash, (i*SCALE, 26*SCALE))

    def ascii(self, string, textColor=c['white'], backgroundColor=None):
        return self.font.render(string, False, textColor, backgroundColor)

    def draw(self, win, char, pos, textColor=c['white'], backgroundColor=None):
        char = self.ascii(char, textColor, backgroundColor)
        pos = (pos[0]*SCALE, pos[1]*SCALE)
        match win:
            case 'game':              
                self.gameWin.blit(char, pos)
                self.gameChange = True
            case 'side':
                self.sideWin.blit(char, pos)
                self.sideChange = True
            case 'bottom':
                self.bottomWin.blit(char, pos)
                self.bottomChange = True

    def drawLine(self, win, strg, textColor=c['white'], backgroundColor=None):
        match win:
            case 'side':
                self.sideQueue.append(self.ascii(strg, textColor, backgroundColor))
                self.sideChange = True
            case 'bottom':
                self.bottomQueue.append(self.ascii(strg, textColor, backgroundColor))
                self.bottomChange = True

    def updateSideWin(self):
        if not self.sideChange:
            return
        
        for i, line in enumerate(self.sideQueue):
            self.sideWin.blit(line, (0, i*SCALE))
        self.mainWin.blit(self.sideWin, (27*SCALE, 0))
        self.clearWin('side')
        self.sideQueue = []

        self.sideChange = False

    def updateBottomWin(self):
        if not self.bottomChange:
            return

        for i, line in enumerate(self.bottomQueue):
            self.bottomWin.blit(line, (0, i*SCALE))
        self.mainWin.blit(self.bottomWin, (0, 27*SCALE))
        self.clearWin('bottom')
        self.bottomQueue = []

        self.bottomChange = False

    def updateGameWin(self):
        if not self.gameChange:
            return
        
        self.mainWin.blit(self.gameWin, (0, 0))
        self.clearWin('game')

        self.gameChange = False

    def clearWin(self, win):
        match win:
            case 'game':
                self.gameWin.fill((0, 0, 0))
                self.gameChange = True
            case 'side':
                self.sideWin.fill((0, 0, 0))
                self.sideChange = True
            case 'bottom':
                self.bottomWin.fill((0, 0, 0))
                self.bottomChange = True

    def update(self):
        
        self.updateSideWin()
        self.updateBottomWin()
        self.updateGameWin()

        pg.display.update()

    