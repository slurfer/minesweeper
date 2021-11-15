import pygame
from pygame.locals import *


GRID_COLOR = (138, 138, 138)
BG_COLOR = (240, 240, 240)




def draw_game():
    DISPLAY_SURFACE.fill(BG_COLOR)
    for x in range(0, WINDOW_WIDTH, CELL_SIZE): 
        pygame.draw.line(DISPLAY_SURFACE, GRID_COLOR, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE): 
        pygame.draw.line(DISPLAY_SURFACE, GRID_COLOR, (0, y), (WINDOW_WIDTH, y))
