import sys
import pygame as pg

from Events.events import ev

from Display.output import Output
from Player.player import Player
from Map.map import Map

clock = pg.time.Clock()

out = Output()
player = Player()
level = Map(player)  

run = True
animCounter = 0
while run:
    for event in pg.event.get():
        match event.type:
            case pg.QUIT:
                run = False
            case pg.KEYDOWN:
                level.onKey(event.key)            
            case ev.DRAWCHAR:
                out.draw(event.win, event.char, event.pos, event.color, event.backgroundColor)
            case ev.DRAWLINE:
                out.drawLine(event.win, event.strg, event.color, event.backgroundColor)
            case ev.CLEARWIN:
                out.clearWin(event.win)
            case ev.VIEW:
                level.view()
            case ev.DESTRUCT:
                level.rmFromLevel(event.obj)

    animCounter += 1

    out.update()
    level.update(animCounter)

    if animCounter == 60:
        animCounter = 0

    #DEBUGGING
    #out.draw('bottom', f'ups:{int(clock.get_fps())}', (30, 8), 'black', 'grey')
    #END DEBUGGING

    clock.tick(60)

pg.quit()