import pygame


class Window(pygame.sprite.Sprite):
    """
    Окно(для меню, диалогов и прочего)
    """

    def __init__(self, size: tuple[int, int], color: tuple[int, int, int], coord: tuple[int, int] | None = None):
        super().__init__()

        self.size = size
        self.color = color
        self.children = pygame.sprite.Group()  # список спрайтов

        # Базовое изображение
        self.base_image = pygame.Surface(size)
        pygame.draw.rect(self.base_image, color, (0, 0, size[0], size[1]), 5)

        self.image = self.base_image.copy()
        self.rect = self.image.get_rect()
        if coord:
            self.rect.topleft = coord


    def add(self, sprite: pygame.sprite.Sprite):
        """
        Добавить спрайт (координаты из sprite.rect)
        :param sprite: Добавление спрайта
        :return: Ничего
        """

        self.children.add(sprite)


    def remove(self, sprite: pygame.sprite.Sprite):
        """
        Удалить спрайт
        :param sprite: Удаление спрайта
        :return: Ничего
        """

        self.children.remove(sprite)


    def _update_image(self):
        """Обновить изображение окна со всеми спрайтами"""
        self.image = self.base_image.copy()
        for sprite in self.children:
            if hasattr(sprite, 'image'):
                self.image.blit(sprite.image, sprite.rect.topleft)

    def update(self):
        """Обновить все компоненты"""
        self.children.update()
        self.render()

    def render(self):
        self.image = self.base_image.copy()
        self.children.draw(self.image)
