import pygame
from pygame.locals import *
from board import *
import time
import os

board = Board()
board.generate_board()
CELL_SIZE = 30
PLAY_FIELD_HEIGHT = board.board_height * CELL_SIZE
WINDOW_HEIGHT = PLAY_FIELD_HEIGHT + CELL_SIZE + 200 #potom změnit 200 
WINDOW_WIDTH = PLAY_FIELD_HEIGHT + 2 * CELL_SIZE
BASIC_FONT = None
BASIC_FONT_SIZE = 50
DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
FPS = 30

time_limit = 10
start_time = time.time()

GRID_COLOR = (138, 138, 138)
BG_COLOR = (240, 240, 240)

def main():
    global FPS_CLOCK, BASIC_FONT, BUTTONS

    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    pygame.display.set_caption("Minesweeper")
    BASIC_FONT = pygame.font.Font('freesansbold.ttf', BASIC_FONT_SIZE)
    board = Board()
    running = True
    graphics
    while running:
        FPS_CLOCK.tick(FPS)
        elapsed_time = time.time() - start_time
        print(time_limit - int(elapsed_time))
        if elapsed_time > time_limit:
            print("GAME OVER")
            quit()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
            pygame.display.flip()
        graphics.draw_board()
        pygame.quit

#def timer():
#    time_limit = 120
#    start_time = time.time()
#    print(start_time)
#    while True:
#        elapsed_time = time.time() - start_time
#        print(time_limit - int(elapsed_time))
#        if elapsed_time > time_limit:
#            print("GAME OVER")
#            quit()

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
        for y in range(board.board_height):
            for x in range(board.board_width):
                sprite = board.board[y][x].value
                if sprite == None: 
                    sprite = 0
                    pass 
                if not sprite == None: 
                    if sprite == 0:
                        sprite = self.values["empty"] #změním, až na ně půjde kliknout
                    if sprite == 1:
                        sprite = self.values["grid1"]
                    if sprite == 2:
                        sprite = self.values["grid2"]
                    if sprite == 3:
                        sprite = self.values["grid3"]
                    if sprite == 4:
                        sprite = self.values["grid4"]
                    if sprite == 5:
                        sprite = self.values["grid5"]
                    if sprite == 6:
                        sprite = self.values["grid6"]
                    if sprite == 7:
                        sprite = self.values["grid7"]
                    if sprite == 8:
                        sprite = self.values["grid8"]      
                        
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
