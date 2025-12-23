import pygame

from src.constants import COLOR


class HealthBar(pygame.sprite.Sprite):

    def __init__(self, hp: int, max_hp: int, color: tuple[int, int, int], size: tuple[int, int], coord: tuple[int, int] | None = None) -> None:
        super().__init__()
        self.cur_hp = hp
        self.size = size
        self.max_hp = max_hp
        self.color = color
        self.image = pygame.Surface(size)
        self.image.fill(COLOR.RED)
        len_hp = int(hp/max_hp*size[0])
        pygame.draw.rect(
            self.image,
            color,
            (0, 0, len_hp, size[1])
        )
        self.rect = self.image.get_rect()
        if coord:
            self.rect.topleft = coord

    def redraw(self, hp: int):
        if hp != self.cur_hp:
            self.image = pygame.Surface(self.size)
            self.image.fill(COLOR.RED)
            len_hp = int(hp/self.max_hp*self.size[0])
            pygame.draw.rect(
                self.image,
                self.color,
                (0, 0, len_hp, self.size[1])
            )
            self.cur_hp = hp
