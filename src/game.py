import pygame

from src.constants import FPS, WIDTH, HEIGHT
from src.base_classes.scene import Scene
from src.scenes.battle.battle_scene import BattleScene
from src.enemies.froggit import Froggit
from src.base_classes.player import Player
from src.config import PLAYER_CONFIGS

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
        self.player = Player(PLAYER_CONFIGS[0])
        self.current_scene: Scene = BattleScene([Froggit(), Froggit(), Froggit()], self.player, self.dj)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()


    def run(self) -> None:
        """
        Тело игры
        :return: Ничего
        """

        running = True

        while running:
            self.current_scene.handle_events(pygame.event.get())
            self.current_scene.update()
            self.current_scene.render(self.screen)
            self.clock.tick(FPS)
            running = self.current_scene.active

        pygame.quit()
