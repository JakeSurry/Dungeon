import pygame as pg
import dungeons
import tools
import attacks
import time
pg.init()

class Player(pg.sprite.Sprite):
	def __init__(self, image, pos):
		super().__init__()
		self.image = image
		self.ori_image = image
		self.rect = self.image.get_rect()
		self.rect.x = pos[0]
		self.rect.y = pos[1]
		self.angle = 0
		self.facing = 'up'
	def get_input(self, display):
		movement = None
		attack = False
		pressed_keys = pg.key.get_pressed()
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.display.quit()
				pg.quit()
			if event.type == pg.MOUSEBUTTONDOWN:
				attacks.basic_attack(display, self.rect.x, self.rect.y, self.facing)
				attack = True
		if pressed_keys[pg.K_a]:
			movement = 'left'
		elif pressed_keys[pg.K_d]:
			movement = 'right'
		elif pressed_keys[pg.K_w]:
			movement = 'up'
		elif pressed_keys[pg.K_s]:
			movement = 'down'
		self.movement = movement
		return attack
	def collision(self, room):
		collision_list, room = collision_test(self.rect, self.movement, room)
		for block in collision_list:
			if self.movement == 'left':
				self.rect.left = block.right
			elif self.movement == 'right':
				self.rect.right = block.left
			elif self.movement == 'up':
				self.rect.top = block.bottom
			elif self.movement == 'down':
				self.rect.bottom = block.top
		return room
	def update_player(self, room):
		if self.movement == 'left':
			self.rect.x -= 5
			self.angle = 90
			self.facing = 'left'
		elif self.movement == 'right':
			self.rect.x += 5
			self.angle = 270
			self.facing = 'right'
		elif self.movement == 'up':
			self.rect.y -= 5
			self.angle = 0
			self.facing = 'up'
		elif self.movement == 'down':
			self.rect.y += 5
			self.angle = 180
			self.facing = 'down'
		self.image = pg.transform.rotate(self.ori_image, self.angle)
		room = self.collision(room)
		return room

def collision_test(thing, movement, room):
	collision_list = []
	blocks = dungeons.blocks(room)
	for block in blocks:
		if thing.colliderect(block[1]):
			try:
				if block[0][0] == 2:
					room = swap_rooms(block[0][1], movement)
			except TypeError:
				collision_list.append(block[1])
	return collision_list, room

def init_player():
	player_image = tools.load_images('assets/player.test.png')
	player = Player(player_image, [200, 200])
	player_group = pg.sprite.Group()
	player_group.add(player)
	return player_group, player

def swap_rooms(room, movement):
	if movement == 'left':
		player.rect.x = 720
		player.rect.y = 380
	elif movement == 'right':
		player.rect.x = 40
		player.rect.y = 380
	elif movement == 'up':
		player.rect.x = 380
		player.rect.y = 760
	elif movement == 'down':
		player.rect.x = 380
		player.rect.y = 40
	if room == 1:
		room = dungeons.room1()
	elif room == 2:
		room = dungeons.room2()
	return room

player_group, player = init_player()
