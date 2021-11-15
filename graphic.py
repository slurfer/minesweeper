import pygame
from pygame.locals import *

WINDOW_WIDTH = 420
WINDOW_HEIGHT = 600 
PLAY_FIELD_HEIGHT = 420 
BASIC_FONT = None
BASIC_FONT_SIZE = 50
CELL_SIZE = 10
DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
GRID_COLOR = (138, 138, 138)
BG_COLOR = (240, 240, 240)




def draw_game():
    DISPLAY_SURFACE.fill(BG_COLOR)
    for x in range(0, WINDOW_WIDTH, CELL_SIZE): 
        pygame.draw.line(DISPLAY_SURFACE, GRID_COLOR, (x, WINDOW_HEIGHT), (x, WINDOW_HEIGHT - PLAY_FIELD_HEIGHT))
    for y in range(WINDOW_HEIGHT - PLAY_FIELD_HEIGHT, WINDOW_HEIGHT, CELL_SIZE): 
        pygame.draw.line(DISPLAY_SURFACE, GRID_COLOR, (0, y), (WINDOW_WIDTH, y))
