import pygame

from src.base_classes.stage import Stage
from src.entities.window import Window
from src.base_classes.player import Player

from src.constants import COLOR

class InventoryStage(Stage):

    def __init__(self, player: Player):
        super().__init__()
        window = Window((900, 250), COLOR.BLUE)
        window.rect.topleft = (50, 250)
        self.all_sprites.add(window)


    def other_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                return True
        return False
