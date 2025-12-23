import pygame

from src.entities.text import Text


class ButtonWithoutBolder(pygame.sprite.Sprite):

    def __init__(self, message: str, color: tuple[int, int, int], active_color: tuple[int, int, int], coord: tuple[int, int] | None = None):
        super().__init__()

        self.deactive = Text(message, 30, color).image
        self.active = Text(message, 30, active_color).image

        self.deactivate()
        self.rect = self.image.get_rect()
        if coord:
            self.rect.topleft = coord

    def deactivate(self):
        self.image = self.deactive


    def activate(self):
        self.image = self.active
