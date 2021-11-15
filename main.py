import pygame
from pygame.locals import *

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
DISPLAY_WIDTH = WINDOW_WIDTH #display width/height bude asi to pole s minama
DISPLAY_HEIGHT = WINDOW_HEIGHT - 100 #potom změnit až tam budou ty stats
CELL_SIZE: 10
assert DISPLAY_WIDTH % CELL_SIZE == 0, 'Window width must be a multiple of cell size.'
assert DISPLAY_HEIGHT % CELL_SIZE == 0, 'Window height must be a multiple of cell size.'

BG_COLOR = (215, 215, 215)
GRID_COLOR = (181, 181, 181)
BASIC_FONT = pygame.font.Font('freesansbold.ttf', 8)

def main():
    global FPS_CLOCK, DISPLAY_SURFACE, BUTTONS

    pygame.init()
    FPS_CLOCK = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))