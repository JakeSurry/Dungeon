import pygame as pg
import dungeons

def load_images(path):
	image = pg.transform.scale(pg.image.load(path), (40, 40))
	return image
