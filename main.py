import pygame
from pygame.locals import *
from board import *
import time
import os

CELL_SIZE = 30
PLAY_FIELD_HEIGHT = board.board_height * CELL_SIZE
WINDOW_HEIGHT = PLAY_FIELD_HEIGHT + CELL_SIZE + 210 # don't change 210
WINDOW_WIDTH = PLAY_FIELD_HEIGHT + 2 * CELL_SIZE
BASIC_FONT = None
BASIC_FONT_SIZE = 50
DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
FPS = 30

time_limit = 10
start_time = time.time()

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
        """elapsed_time = time.time() - start_time
        print(time_limit - int(elapsed_time))
        if elapsed_time > time_limit:
            print("GAME OVER")
            quit()"""
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
            pygame.display.flip()
            if(event.type == pygame.MOUSEBUTTONDOWN):
                tiles = pygame.mouse.get_pos()
                graphics.handle_click(tiles)    
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
        self.game_ended = False

    def load_sprites(self):
        self.values = {}       
        for file_name in os.listdir("sprites"):
            value = pygame.image.load(r"sprites/" + file_name)
            self.values[file_name.split(".")[0]] = value

    def click(self, yx):
        y, x = yx
        if y >= 200 and y <= 800:
            if x >= 30 and x <= 630:
                board.board[y // CELL_SIZE - 7][x // CELL_SIZE - 1].was_clicked = True 
                """if board.board[y // CELL_SIZE - 7][x // CELL_SIZE - 1].value is 0:
                    board.board[y // CELL_SIZE - 7][x // CELL_SIZE - 1] = cell"""
                self.draw_board()      
                if board.board[y // CELL_SIZE - 7][x // CELL_SIZE - 1].value == None:
                    self.game_ended = True
                    self.draw_board()
                    self.end_screen()
                
        else:
            return None


    def draw_board(self):
        DISPLAY_SURFACE.fill(BG_COLOR)
        top_left = (CELL_SIZE,WINDOW_HEIGHT - (PLAY_FIELD_HEIGHT + CELL_SIZE))
        for y in range(board.board_height):
            for x in range(board.board_width):
                if board.board[y][x].was_clicked is True:
                    sprite = board.board[y][x].value
                    if sprite == None: 
                        sprite = self.values["mine"]
                        DISPLAY_SURFACE.blit(sprite, top_left)                   
                    if not sprite == None: 
                        if sprite == 0:
                            sprite = self.values["empty"] 
                        elif sprite == 1:
                            sprite = self.values["grid1"]
                        elif sprite == 2:
                            sprite = self.values["grid2"]
                        elif sprite == 3:
                            sprite = self.values["grid3"]
                        elif sprite == 4:
                            sprite = self.values["grid4"]
                        elif sprite == 5:
                            sprite = self.values["grid5"]
                        elif sprite == 6:
                            sprite = self.values["grid6"]
                        elif sprite == 7:
                            sprite = self.values["grid7"]
                        elif sprite == 8:
                            sprite = self.values["grid8"]   
                        DISPLAY_SURFACE.blit(sprite, top_left)
                else:
                    sprite = self.values["Grid"]
                    DISPLAY_SURFACE.blit(sprite, top_left)
                    
                if self.game_ended == True:
                    if board.board[y][x].value == None:
                        DISPLAY_SURFACE.blit(self.values["mine"], top_left)
                top_left = top_left[0] + CELL_SIZE, top_left[1]
            top_left = CELL_SIZE, top_left[1] + CELL_SIZE


    def handle_click(self, tiles):
        yx = tiles[1] , tiles[0] 
        self.click(yx)

    def end_screen(self):
        
        msg_surface = BASIC_FONT.render('idk', True, BG_COLOR)
        msg_rect = msg_surface.get_rect()
        msg_rect.topleft = (WINDOW_WIDTH - 200, WINDOW_HEIGHT - 30)
        DISPLAY_SURFACE.blit(msg_surface, msg_rect)



    #def game_ended():


"""class Player:
    def __init__(self, name) -> None:
        self.score = 0
        self.name = name
    
    def __str__(self) -> str:
        return f"Score of player {self.name} is {self.score}"
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o):
            return self.score == __o.score
        else:
            False"""

graphics = Graphics()




if __name__ == "__main__":
    main()
