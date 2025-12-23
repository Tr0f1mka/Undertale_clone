import pygame

from src.constants import ACTIONS

class Scene():

    def __init__(self):
        self.all_sprites = pygame.sprite.Group()

    def handle_events(self, events: list[pygame.event.Event]) -> bool:
        """
        Обрабатывает события
        :param events: Список событий
        :return: Продолжаем цикл или нет
        """

        for event in events:
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key in ACTIONS.ESCAPE:
                    return False
            self.other_events(event)

        return True

    def other_events(self, event: pygame.event.Event):
        pass

    def update(self) -> None:
        pass

    def render(self, screen: pygame.Surface) -> None:
        pass
