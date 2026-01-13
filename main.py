import pygame

#initialization of pygame
pygame.init()

WIDTH = 1000
HEIGHT = 900

screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Rajat's Chess Board")

font = pygame.font.Font('freesansbold.ttf',20)
big_font = pygame.font.Font('freesansbold.ttf',50)
timer = pygame.time.Clock()
fps = 60