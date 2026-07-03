import pygame
import os

pygame.font.init()

WIDTH = 900
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

BORDER = pygame.Rect(WIDTH//2 - 5,0,10, HEIGHT)

HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont("comicsans", 100)

FPS = 60
VEL = 5

BULLET_VEL = 7
MAX_BULLETS1 = 3
MAX_BULLETS2 = 1

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

RED_SPACESHIP_IMAGE = pygame.image.load("spaceship_red.png")
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),270)


