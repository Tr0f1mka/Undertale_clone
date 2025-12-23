import pygame


FPS = 60
WIDTH = 1000
HEIGHT = 600


class COLOR():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    PURPLE = (255, 0, 255)
    LIGHT_BLUE = (0, 255, 255),
    ORANGE = (232,128,47)


class ACTIONS():
    ENTER = (pygame.K_RETURN, pygame.K_z)
    CANCEL = (pygame.K_LSHIFT, pygame.K_RSHIFT, pygame.K_x)
    MENU = (pygame.K_LCTRL, pygame.K_RCTRL, pygame.K_c)
    LEFT = (pygame.K_LEFT, pygame.K_KP4, pygame.K_a)
    UP = (pygame.K_UP, pygame.K_KP8, pygame.K_w)
    RIGHT = (pygame.K_RIGHT, pygame.K_KP6, pygame.K_d)
    DOWN = (pygame.K_DOWN, pygame.K_KP2, pygame.K_s)
    ESCAPE = (pygame.K_ESCAPE,)
