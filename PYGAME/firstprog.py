import pygame,sys,os

from pygame.locals import  *

red =(255,0,0)

pygame.init()

window=pygame.display.set_mode((600,1000))

pygame.display.set_caption("This is First gaming progra")

screen=pygame.display.get_surface()

screen.fill(red)

pygame.display.set_caption('Divakar Pal')

pygame.display.flip()

while True:
	print("First pygame program")
	pass