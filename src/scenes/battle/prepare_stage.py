import pygame

from src.base_classes.stage import Stage

from src.entities.text import Text
from src.entities.window import Window

from src.constants import COLOR, WIDTH, HEIGHT

class PrepareStage(Stage):

    def __init__(self, message: str):
        super().__init__()
        window = Window((900, 250), COLOR.WHITE)
        text = Text(message, 20, COLOR.WHITE)
        window.image.blit(text.image, (10, 10))
        window.rect.topleft = (50, 250)
        self.all_sprites.add(window)
