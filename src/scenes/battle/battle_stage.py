from random import randint
import pygame

from src.base_classes.stage import Stage
from src.entities.window import Window
from src.entities.picture import Picture
from src.base_classes.enemy import Enemy
from src.base_classes.player import Player

from src.constants import COLOR, WIDTH, HEIGHT

class BattleStage(Stage):

    def __init__(self, enemy: Enemy, player: Player):
        super().__init__()
        self.enemy = enemy
        self.player = player
        self.x = -20
        self.speedx = 8
        self.window = Window((600, 200), COLOR.WHITE)
        self.create()
        self.window.rect.center = (WIDTH//2, HEIGHT//5*3)
        self.all_sprites.add(self.window)

    def restart(self):
        self.x = -20
        self.create()

    def create(self):
        self.window.image = Window((600, 200), COLOR.WHITE).image
        picture = Picture("sprites/hud/player_attack.png", (5, 5))
        self.window.image.blit(picture.image, (5, 5))
        player = pygame.Surface((8, 200))
        player.fill(COLOR.WHITE)
        self.window.image.blit(player, (self.x, 0))


    def other_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.enemy.hp -= self.calc_damage()
                print(self.enemy.hp)
                return True
        return False


    def calc_damage(self):
        return int(((-self.player.cur_weapon.damage/34810)*(self.x+4-300)**2+3*self.player.cur_weapon.damage)*(randint(95, 105)/100))


    def update(self):
        self.x += self.speedx
        self.create()
