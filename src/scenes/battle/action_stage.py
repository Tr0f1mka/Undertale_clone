import pygame

from src.base_classes.stage import Stage
from src.entities.window import Window
from src.utilities.dj import DJ

from src.constants import COLOR, ACTIONS


class ActionStage(Stage):

    def __init__(self, dj: DJ):
        super().__init__()
        self.dj = dj
        window = Window((900, 230), COLOR.YELLOW)
        window.rect.topleft = (50, 250)
        self.all_sprites.add(window)


    def other_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in ACTIONS.DOWN:
                self.active = False
                self.dj.play_sound("select")
