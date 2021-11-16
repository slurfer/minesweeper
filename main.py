import pygame
from pygame.locals import *
from board import *
import time

WINDOW_WIDTH = 420
WINDOW_HEIGHT = 500 #velikost okna
PLAY_FIELD_HEIGHT = 420 #velikost hrací plochy
PLAY_FIELD_WEIGHT = 420 
BASIC_FONT = None
BASIC_FONT_SIZE = 50
CELL_SIZE = 20 #změnila jsem cell_size

GRID_COLOR = (138, 138, 138)
BG_COLOR = (240, 240, 240)

def main():
    global FPS_CLOCK, DISPLAY_SURFACE, BASIC_FONT, BUTTONS

    pygame.init()
    FPS_CLOCK = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Minesweeper")
    BASIC_FONT = pygame.font.Font('freesansbold.ttf', BASIC_FONT_SIZE)
    DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    board = Board()
    running = True
    draw_game() #test
    while running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
            pygame.display.flip()
        pygame.quit

# grafika
def draw_game():
    DISPLAY_SURFACE.fill(BG_COLOR)
    for x in range(0, WINDOW_WIDTH, CELL_SIZE): 
        pygame.draw.line(DISPLAY_SURFACE, GRID_COLOR, (x, WINDOW_HEIGHT), (x, WINDOW_HEIGHT - PLAY_FIELD_HEIGHT))
    for y in range(WINDOW_HEIGHT - PLAY_FIELD_HEIGHT, WINDOW_HEIGHT, CELL_SIZE): 
        pygame.draw.line(DISPLAY_SURFACE, GRID_COLOR, (0, y), (WINDOW_WIDTH, y))


if __name__ == "__main__":
    main()