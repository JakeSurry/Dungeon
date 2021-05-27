import tools
import pygame as pg
import time
import enemys

def init_weapons():
	weapons = []
	sword = tools.load_images('assets/sword.png')
	sword_hitbox = sword.get_rect()
	weapons.append([sword, sword_hitbox])
	return weapons

def basic_attack(display, x, y, facing):
	if facing == 'up':
		display.blit(weapons[0][0], (x, y-40, 40, 40))
	elif facing == 'down':
		display.blit(pg.transform.rotate(weapons[0][0], 180), (x, y+40, 40, 40))
	elif facing == 'left':
		display.blit(pg.transform.rotate(weapons[0][0], 90), (x-40, y, 40, 40))
	elif facing == 'right':
		display.blit(pg.transform.rotate(weapons[0][0], 270), (x+40, y, 40, 40))

weapons = init_weapons()