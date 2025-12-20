import pygame

from src.constants import COLOR

class Scene():

    def __init__(self):
        self.all_sprites = pygame.sprite.Group()

    def handle_events(self, events: list[pygame.event.Event]) -> bool:
        """
        Обрабатывает события
        :param events: Список событий
        :return: Продолжаем цикл или нет
        """

        for e in events:
            if e.type == pygame.QUIT:
                return False
            if e.type == pygame.KEYDOWN:
                print(e.key, e.mod)
                if e.key == pygame.K_ESCAPE:
                    return False
            self.other_events(e)

        return True

    def other_events(self, event: pygame.event.Event):
        pass

    def update(self) -> None:
        pass

    def render(self, screen: pygame.Surface) -> None:
        pass
