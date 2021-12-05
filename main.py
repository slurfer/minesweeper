import pygame
from pygame.locals import *
from board import *
import time
import os

board = Board()
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
PLAYER = (51, 51, 51)
PLAYER_NOT_ON_TURN =  (115, 115, 115)

def main():
    global FPS_CLOCK, BASIC_FONT, BUTTONS
    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    DISPLAY_SURFACE.fill(BG_COLOR)
    pygame.display.set_caption("Minesweeper")
    BASIC_FONT = pygame.font.Font('freesansbold.ttf', BASIC_FONT_SIZE)
    running = True
    player.timestamp()
    player.turn()
    graphics.draw_board()
    while running:
        FPS_CLOCK.tick(FPS)
        player.subtract_time()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
            pygame.display.flip()
            if(event.type == pygame.MOUSEBUTTONDOWN):
                tiles = pygame.mouse.get_pos()
                graphics.handle_click(tiles)   


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
                if self.game_ended is True:   
                    if 750 >= y >= 700:
                        if 150 >= x >= 30:
                            raise ValueError ("Game quit")
                    if 810 >= y >= 760:
                        if 271 >= x >= 30:
                            self.game_ended = False
                            self.reset_board()                
                if not self.game_ended is True:
                    print(player.player_1)
                    if board.get_tile(x // CELL_SIZE - 1, y // CELL_SIZE - 7).was_clicked is False:
                        player.switch_players()
                    board.click(x // CELL_SIZE - 1, y // CELL_SIZE - 7)
                    self.draw_board()
                    if board.get_tile(x // CELL_SIZE - 1, y // CELL_SIZE - 7).value == None:
                        self.game_ended = True
                        self.draw_board()
                        self.end_screen()
                    else:
                        return None
            else:
                return None


    def draw_board(self):
        top_left = (CELL_SIZE,WINDOW_HEIGHT - (PLAY_FIELD_HEIGHT + CELL_SIZE))
        for y in range(board.board_height):
            for x in range(board.board_width):
                if board.get_tile(x, y).was_clicked is True:
                    sprite = board.get_tile(x, y).value
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
                    if board.get_tile(x, y).value == None:
                        DISPLAY_SURFACE.blit(self.values["mine"], top_left)
                top_left = top_left[0] + CELL_SIZE, top_left[1]
            top_left = CELL_SIZE, top_left[1] + CELL_SIZE


    def handle_click(self, pixels):
        yx = pixels[1] , pixels[0] 
        self.click(yx)

    def end_screen(self):
        DISPLAY_SURFACE.blit(self.values["background"], (0,0))
        msg_surface = BASIC_FONT.render("quit", True, BG_COLOR)
        msg_rect = msg_surface.get_rect()
        msg_rect.topleft = (30, 700)
        DISPLAY_SURFACE.blit(msg_surface, msg_rect)
        msg_surface = BASIC_FONT.render("new game", True, BG_COLOR)
        msg_rect = msg_surface.get_rect()
        msg_rect.topleft = (30, 760)
        DISPLAY_SURFACE.blit(msg_surface, msg_rect)
        if player.player_1 == True:
            msg_surface = BASIC_FONT.render("Player 1 has won", True, BG_COLOR)
            msg_rect = msg_surface.get_rect()
            msg_rect.topleft = (121, 395)
            DISPLAY_SURFACE.blit(msg_surface, msg_rect)
        else:
            msg_surface = BASIC_FONT.render("Player 2 has won", True, BG_COLOR)
            msg_rect = msg_surface.get_rect()
            msg_rect.topleft = (121, 395)
            DISPLAY_SURFACE.blit(msg_surface, msg_rect)

    def reset_board(self):
        board.reset()
        DISPLAY_SURFACE.fill(BG_COLOR)
        player.player_1 = True
        player.player_2 = False
        player.turn()
        self.draw_board()      

class Player:
    def __init__(self):
        self.player_1 = True
        self.player_2 = False
        self.player_1_remaining_time = 30
        self.player_2_remaining_time = 30
        self.timestamp()

    def turn(self):
        if self.player_1 == True:            
            msg_surface = BASIC_FONT.render("Player 1", True, PLAYER)
            msg_rect = msg_surface.get_rect()
            msg_rect.topleft = (30, 30)
            DISPLAY_SURFACE.blit(msg_surface, msg_rect)
            msg_surface = BASIC_FONT.render("Player 2", True, PLAYER_NOT_ON_TURN)
            msg_rect = msg_surface.get_rect()
            msg_rect.topleft = (432, 30)
            DISPLAY_SURFACE.blit(msg_surface, msg_rect)
        if self.player_2 == True:
            msg_surface = BASIC_FONT.render("Player 2", True, PLAYER)
            msg_rect = msg_surface.get_rect()
            msg_rect.topleft = (432, 30)
            DISPLAY_SURFACE.blit(msg_surface, msg_rect)
            msg_surface = BASIC_FONT.render("Player 1", True, PLAYER_NOT_ON_TURN)
            msg_rect = msg_surface.get_rect()
            msg_rect.topleft = (30, 30)
            DISPLAY_SURFACE.blit(msg_surface, msg_rect)

    def display_time(self):
        self.subtract_time()
        if self.player_1 == True:
            msg_surface = pygame.Rect(30, 95, 60, 54)
            pygame.draw.rect(DISPLAY_SURFACE, BG_COLOR, msg_surface)
            msg_surface = BASIC_FONT.render(str(int(self.player_1_remaining_time)), True, PLAYER)
            msg_rect = msg_surface.get_rect()
            msg_rect.topleft = (30, 95)
            DISPLAY_SURFACE.blit(msg_surface, msg_rect)
            self.timestamp()       
        elif self.player_2 == True:
            msg_surface = pygame.Rect(570, 95, 60, 54)
            pygame.draw.rect(DISPLAY_SURFACE, BG_COLOR, msg_surface)
            msg_surface = BASIC_FONT.render(str(int(self.player_2_remaining_time)), True, PLAYER)
            msg_rect = msg_surface.get_rect()
            msg_rect.topleft = (570, 95)
            DISPLAY_SURFACE.blit(msg_surface, msg_rect)
            self.timestamp()      

    def timestamp(self):
        self.timestampvalue = time.time()
    
    def switch_players(self):
        if self.player_1 == True:
            self.subtract_time()
            self.display_time()
            print(f'Player 1: {self.player_1_remaining_time}')
            self.player_1 = False
            self.player_2 = True
            self.turn()
        elif self.player_2 == True:
            self.subtract_time()
            self.display_time()
            print(f'Player 2: {self.player_2_remaining_time}')
            self.timestamp()
            self.player_2 = False
            self.player_1 = True
            self.turn()
    
    def subtract_time(self):
        if self.player_1 == True:
            self.player_1_remaining_time -= time.time()-self.timestampvalue
            self.timestamp()
            return self.player_1_remaining_time
        else:
            self.player_2_remaining_time -= time.time()-self.timestampvalue
            self.timestamp()
            return self.player_2_remaining_time

player = Player()
graphics = Graphics()




if __name__ == "__main__":
    main()