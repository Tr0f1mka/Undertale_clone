import pygame

from src.constants import FPS, WIDTH, HEIGHT
from src.base_classes.scene import Scene
from src.scenes.battle.battle_scene import BattleScene
from src.enemies.sans import Sans, Sans1
from src.base_classes.player import Player

from src.utilities.dj import DJ

class Game():

    def __init__(self) -> None:
        """
        Инициализация игры
        :return: Ничего
        """

        pygame.init()
        pygame.display.set_icon(pygame.image.load("sprites/souls/red_soul.png"))
        pygame.display.set_caption("Undertale(clone)")
        self.dj = DJ()
        self.scenes: dict[str, Scene] = {}
        self.sans = Sans()
        self.player = Player()
        self.current_scene: Scene = BattleScene([self.sans, Sans1()], self.player, self.dj)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()


    def run(self) -> None:
        """
        Тело игры
        :return: Ничего
        """

        running = True

        while running:
            running = self.current_scene.handle_events(pygame.event.get())
            self.current_scene.update()
            self.current_scene.render(self.screen)
            self.clock.tick(FPS)

        pygame.quit()
