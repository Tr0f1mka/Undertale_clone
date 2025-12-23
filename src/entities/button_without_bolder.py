import pygame

from src.entities.text import Text


class ButtonWithoutBolder(pygame.sprite.Sprite):

    def __init__(self, message: str, color: tuple[int, int, int], active_color: tuple[int, int, int], coord: tuple[int, int] | None = None):
        super().__init__()

        self.message = message
        self.color = color
        self.active_color = active_color

        self.deactivate()
        self.rect = self.image.get_rect()
        if coord:
            self.rect.topleft = coord

    def deactivate(self):
        self.image = Text(self.message, 30, self.color).image


    def activate(self):
        self.image = Text(self.message, 30, self.active_color).image
