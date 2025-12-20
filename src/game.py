import pygame

from src.constants import FPS, WIDTH, HEIGHT, ENEMIES
from src.base_classes.scene import Scene
from src.scenes.battle.battle_scene import BattleScene
from src.enemies.sans import Sans
from src.base_classes.player import Player

from src.utilities.dj import DJ

class Game():

    def __init__(self) -> None:
        """
        Инициализация игры
        :return: Ничего
        """

        pygame.init()
        pygame.display.set_icon(pygame.image.load("sprites/red_heart.png"))
        pygame.display.set_caption("Undertale(clone)")
        self.scenes: dict[str, Scene] = {}
        self.sans = Sans()
        self.current_scene: Scene = BattleScene(self.sans, Player())
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.dj = DJ()


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
