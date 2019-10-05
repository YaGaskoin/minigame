import pygame
from pygame.sprite import Group
from hum import Human
from ball import Ball
import sys
from time import sleep
def check_event(hum):
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					hum.move_right = True
				if event.key == pygame.K_LEFT:
					hum.move_left = True
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					hum.move_right = False
				if event.key == pygame.K_LEFT:
					hum.move_left = False
					
def sc_update(screen,balls,hum):
	screen.fill((255,255,255))
	hum.update()
	hum.blitme()
	balls.update()
	check_ball(balls,hum,screen)
	balls.draw(screen)
	pygame.display.flip()

def check_ball(balls,hum,screen):
	for ball in balls:
		if ball.rect.centery > ball.sc_rect.bottom:
			if hum.score > 0:
				hum.score -=1
				balls.remove(ball)
				ball = Ball(screen)
				balls.add(ball)
			else:
				sleep(1)
				sys.exit()
				
		elif ball.rect.right <= hum.rect.right+50 and ball.rect.left >= hum.rect.left -50 and ball.rect.bottom > hum.rect.top:
			balls.remove(ball)
			ball = Ball(screen)
			balls.add(ball)
def run():
	pygame.init()
	screen=pygame.display.set_mode((1200,800))
	pygame.display.set_caption('FIFA')
	hum = Human(screen)
	ball = Ball(screen)
	balls = Group()
	balls.add(ball)
	
	while True:
		check_event(hum)
		sc_update(screen,balls,hum)
		 
run()
