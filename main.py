import pygame
from pygame.locals import *

def main():
    global FPS_CLOCK, DISPLAY_SURFACE, BASIC_FONT, BUTTONS

    pygame.init()
    FPS_CLOCK = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))