import pygame
from pygame.locals import *
from board import *
from graphic import *
import time

WINDOW_WIDTH = 420
WINDOW_HEIGHT = 500 #velikost okna
PLAY_FIELD_HEIGHT = 420 #velikost hrací plochy
PLAY_FIELD_HEIGHT = 420  
BASIC_FONT = None
BASIC_FONT_SIZE = 50
CELL_SIZE = 20 #změnila jsem cell_size

def main():
    global FPS_CLOCK, DISPLAY_SURFACE, BASIC_FONT, BUTTONS

    pygame.init()
    FPS_CLOCK = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Minesweeper")
    BASIC_FONT = pygame.font.Font('freesansbold.ttf', BASIC_FONT_SIZE)
    DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    board = Board()
    running = True

    while running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
            pygame.display.flip()
        pygame.quit

if __name__ == "__main__":
    main()