import pygame as pg

class ev(): 
    DRAWCHAR = pg.event.custom_type() #Call to print something to some window 
    DRAWLINE = pg.event.custom_type() #Call to queue a line to some window
    CLEARWIN = pg.event.custom_type() #Call to clear some window
    VIEW     = pg.event.custom_type() #Call to view whatever is under cursor
    DESTRUCT = pg.event.custom_type() #Call to delete an object from level