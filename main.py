import pygame as pg 
import dungeons
import player
import time
pg.init()

display = pg.display.set_mode((800, 800))
pg.display.set_caption('Dungeon')
pg.display.update()

clock = pg.time.Clock()
room = dungeons.room1()
while True:
	clock.tick(60)
	attack = player.player.get_input(display)
	room = player.player.update_player(room)
	player.player_group.update()
	player.player_group.draw(display)
	pg.display.update()
	if attack:
		time.sleep(.1)
	display.fill((0, 0, 0))
	dungeons.display_dungeon(display, room)

pg.display.quit()
pg.quit()
