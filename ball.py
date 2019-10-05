import pygame
from pygame.sprite import Sprite
from random import randint

class Ball(Sprite):
	def __init__(self,screen):
		super(Ball,self).__init__()
		self.screen = screen
		self.sc_rect = self.screen.get_rect()
		self.image = pygame.image.load('this.png')
		self.rect = self.image.get_rect()
		self.speed = 3
		self.rect.top = self.sc_rect.top
		self.rect.centerx = randint(50,1150)
		self.y = float(self.rect.y)
	def blitme(self):
		self.screen.blit(self.image,self.rect)
	def update(self):
		self.y += 1.7
		self.rect.y = self.y
		
	
