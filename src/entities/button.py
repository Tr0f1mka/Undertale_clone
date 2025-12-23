import pygame

from src.entities.text import Text
from src.entities.window import Window


class Button(pygame.sprite.Sprite):

    def __init__(self, message: str, color: tuple[int], active_color: tuple[int], coord: tuple[int]):
        pygame.sprite.Sprite.__init__(self)

        self.message = message
        self.color = color
        self.active_color = active_color
        self.coord = coord

        self.deactivate()
        self.rect = self.image.get_rect()
        self.rect.topleft = coord


    def deactivate(self):
        self.image = Window((210, 50), self.color)
        self.image = self.image.image
        text = Text(self.message, 30, self.color)
        self.image.blit(text.image, ((210-text.image.get_width())//2, (50-text.image.get_height())//2))


    def activate(self):
        self.image = Window((210, 50), self.active_color)
        self.image = self.image.image
        text = Text(self.message, 30, self.active_color)
        self.image.blit(text.image, ((210-text.image.get_width())//2, (50-text.image.get_height())//2))
