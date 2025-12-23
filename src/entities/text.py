import pygame


class Text(pygame.sprite.Sprite):

    def __init__(self, message: str, size: int, color: tuple[int, int, int], coord: tuple[int, int] | None = None):
        pygame.sprite.Sprite.__init__(self)

        self.font = pygame.font.Font("fonts/Monocraft.otf", size)
        self.image = self.font.render(message, True, color)
        self.rect = self.image.get_rect()
        if coord:
            self.rect.topleft = coord
