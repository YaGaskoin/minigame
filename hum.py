import pygame

class Human():
	def __init__(self,screen):
		self.screen =  screen
		self.image = pygame.image.load('111.jpg')
		self.rect = self.image.get_rect()
		self.sc_rect = self.screen.get_rect()
		self.rect.centerx = self.sc_rect.centerx
		self.rect.bottom = self.sc_rect.bottom
		self.move_right = False
		self.move_left = False
		self.score = 3
	def blitme(self):
		self.screen.blit(self.image,self.rect)
	def update(self):
		if self.move_right == True and self.rect.centerx < self.sc_rect.right - 50:
			self.rect.centerx +=2
		if self.move_left == True and self.rect.centerx > self.sc_rect.left+50:
			self.rect.centerx -=2
