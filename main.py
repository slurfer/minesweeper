import pygame
from pygame.locals import *
from board import *
import time
import os

WINDOW_WIDTH = 420
WINDOW_HEIGHT = 500 
PLAY_FIELD_HEIGHT = 300 
BASIC_FONT = None
BASIC_FONT_SIZE = 50
CELL_SIZE = 30
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
    graphics
    while running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
            pygame.display.flip()
        graphics.draw_board()
        pygame.quit


class Graphics:
    def __init__(self):
        self.load_sprites()

    def load_sprites(self):
        self.values = {}       
        for file_name in os.listdir("sprites"):
            value = pygame.image.load(r"sprites/" + file_name)
            self.values[file_name.split(".")[0]] = value

    def draw_board(self):
        DISPLAY_SURFACE.fill(BG_COLOR)
        top_left = (CELL_SIZE,WINDOW_HEIGHT - (PLAY_FIELD_HEIGHT + CELL_SIZE))
        for x in range(board.board_width):
            for y in range(board.board_height):
                sprite = self.values["Grid"] #změním, až na ně půjde kliknout
                DISPLAY_SURFACE.blit(sprite, top_left)
                top_left = top_left[0] + CELL_SIZE, top_left[1] 
            top_left = CELL_SIZE, top_left[1] + CELL_SIZE


class Player:
    def __init__(self, name) -> None:
        self.score = 0
        self.name = name
    
    def __str__(self) -> str:
        return f"Score of player {self.name} is {self.score}"
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o):
            return self.score == __o.score
        else:
            False

graphics = Graphics()




if __name__ == "__main__":
    main()