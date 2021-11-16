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
DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

GRID_COLOR = (138, 138, 138)
BG_COLOR = (240, 240, 240)

def main():
    global FPS_CLOCK, BASIC_FONT, BUTTONS

    pygame.init()
    FPS_CLOCK = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Minesweeper")
    BASIC_FONT = pygame.font.Font('freesansbold.ttf', BASIC_FONT_SIZE)
    board = Board()
    running = True
    grid.draw_game() #test
    while running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
            pygame.display.flip()
        pygame.quit

# grafika
"""def draw_game():
    DISPLAY_SURFACE.fill(BG_COLOR)
    for x in range(0, WINDOW_WIDTH, CELL_SIZE): 
        pygame.draw.line(DISPLAY_SURFACE, GRID_COLOR, (x, WINDOW_HEIGHT), (x, WINDOW_HEIGHT - PLAY_FIELD_HEIGHT))
    for y in range(WINDOW_HEIGHT - PLAY_FIELD_HEIGHT, WINDOW_HEIGHT, CELL_SIZE): 
        pygame.draw.line(DISPLAY_SURFACE, GRID_COLOR, (0, y), (WINDOW_WIDTH, y))"""

spr_empty_grid = pygame.image.load("Sprites/empty.png")
spr_grid = pygame.image.load("Sprites/Grid.png")
spr_grid1 = pygame.image.load("Sprites/grid1.png")
spr_grid2 = pygame.image.load("Sprites/grid2.png")
spr_grid3 = pygame.image.load("Sprites/grid3.png")
spr_grid4 = pygame.image.load("Sprites/grid4.png")
spr_grid5 = pygame.image.load("Sprites/grid5.png")
spr_grid6 = pygame.image.load("Sprites/grid6.png")
spr_grid7 = pygame.image.load("Sprites/grid7.png")
spr_grid8 = pygame.image.load("Sprites/grid8.png")
spr_mine = pygame.image.load("Sprites/mine.png")
spr_mine_clicked = pygame.image.load("Sprites/mineClicked.png")

#DISPLAY_SURFACE.blit(test, (0,0))
class Grid:
    def draw_game(self):
        DISPLAY_SURFACE.fill(BG_COLOR)
        for x in range(0, WINDOW_WIDTH, CELL_SIZE):
            for y in range (WINDOW_HEIGHT - PLAY_FIELD_HEIGHT, WINDOW_HEIGHT, CELL_SIZE):
                DISPLAY_SURFACE.blit(spr_empty_grid, (x,y))

grid = Grid()

if __name__ == "__main__":
    main()