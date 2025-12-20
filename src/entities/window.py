import pygame


class Window(pygame.sprite.Sprite):

    def __init__(self, size: tuple[int, int], color: tuple[int, int, int]):
        super().__init__()

        self.image = pygame.Surface(size)
        pygame.draw.rect(
            self.image,
            color,
            (0, 0, self.image.get_width(), self.image.get_height()),
            5
        )
        self.rect = self.image.get_rect()
