import pygame


class Picture(pygame.sprite.Sprite):

    def __init__(self, image: str, coord: tuple[int, int]):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = coord
