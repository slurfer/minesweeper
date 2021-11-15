import pygame
from pygame.locals import *
import board
import time

WINDOW_WIDTH = 420
WINDOW_HEIGHT = 420

def main():
    global FPS_CLOCK, DISPLAY_SURFACE, BASIC_FONT, BUTTONS

    pygame.init()
    FPS_CLOCK = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Minesweeper")
    while True:
        pygame.display.update