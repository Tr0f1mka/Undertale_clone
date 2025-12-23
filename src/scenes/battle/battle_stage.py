from random import randint
import pygame

from src.base_classes.stage import Stage
from src.entities.window import Window
from src.entities.button_without_bolder import ButtonWithoutBolder
from src.entities.picture import Picture
from src.scenes.battle.attack_marker import Marker
from src.base_classes.enemy import Enemy
from src.base_classes.player import Player
from src.utilities.dj import DJ
from src.items.armors.cowboy_hat import CowboyHat

from src.constants import COLOR, WIDTH, FPS, ACTIONS


class BattleStage(Stage):


    def __init__(self, enemies: list[Enemy], player: Player, dj: DJ):

        super().__init__()
        self.enemies = enemies
        self.player = player
        self.dj = dj


    def init_menu(self):
        self.is_change_substage = True
        self.menu = Window((900, 230), COLOR.WHITE, (50, 250))
        self.buttons: list[ButtonWithoutBolder] = []
        for i in range(len(self.enemies)):
            enemy = ButtonWithoutBolder(self.enemies[i].name, COLOR.WHITE, COLOR.YELLOW, (10, 10+40*i))
            self.menu.add(enemy)
            self.buttons.append(enemy)
        self.cur_button = 0
        self.buttons[0].activate()
        self.all_sprites.add(self.menu)



    def restart(self):
        super().restart()
        self.init_menu()


    def other_events(self, event):
        if self.is_change_substage:
            next_but = self.cur_button
            if event.type == pygame.KEYDOWN:
                if event.key in ACTIONS.UP:
                    next_but = (next_but - 1) % len(self.buttons)
                    self.dj.play_sound("select")
                    self.change_button(next_but)

                if event.key in ACTIONS.DOWN:
                    next_but = (next_but + 1) % len(self.buttons)
                    self.dj.play_sound("select")
                    self.change_button(next_but)

                if event.key in ACTIONS.CANCEL:
                    self.active = False

                if event.key in ACTIONS.ENTER:
                    self.is_change_substage = False
                    self.all_sprites.remove(self.menu)
                    self.init_battle()

        else:
            if event.type == pygame.KEYDOWN:
                if event.key in ACTIONS.ENTER:
                    self.cur_marker.pressed = True


    def change_button(self, next_but: int):
        if self.cur_button != next_but:
            self.buttons[self.cur_button].deactivate()
            self.buttons[next_but].activate()
            self.cur_button = next_but


    def init_battle(self):
        self.battle_field = Window((600, 200), COLOR.WHITE, (WIDTH//2-300, 250))
        picture = Picture("sprites/hud/player_attack.png", (5, 5))
        self.battle_field.add(picture)
        marker = Marker()
        self.battle_field.add(marker)
        self.markers: list[Marker] = [marker]
        self.all_sprites.add(self.battle_field)
        self.cur_marker = self.markers[0]
        self.count_markers = self.player.count_attacks-1
        self.init_timer()


    def init_timer(self):
        self.timer = int(randint(8, 12)/10*FPS)


    def update_battle(self):
        if self.count_markers:
            self.timer -= 1
            if self.timer <= 0:
                marker = Marker()
                self.battle_field.add(marker)
                self.markers.append(marker)
                self.init_timer()
                self.count_markers -= 1


    def calc_damage(self) -> int:
        cur_damage = self.player.cur_weapon.param + self.player.base_damage + 5*int(isinstance(self.player.cur_armor, CowboyHat))
        return int( ( (-(cur_damage) / 34810) * (self.cur_marker.rect.x - 296) ** 2 + 3 * cur_damage) * (randint(95, 105)/100) )


    def update(self):
        super().update()
        if not self.is_change_substage:
            self.update_battle()


    # def __init__(self, enemy: Enemy, player: Player, dj: DJ):

    #     super().__init__()
    #     self.enemy = enemy
    #     self.player = player
    #     self.dj = dj

    #     self.x = -20
    #     self.speedx = 8

    #     self.window = Window((600, 200), COLOR.WHITE)
    #     self.create()
    #     self.window.rect.center = (WIDTH//2, HEIGHT//5*3)
    #     self.all_sprites.add(self.window)

    #     self.timer_after = int(1.5 * FPS)
    #     self.is_attack = 1


    # def restart(self):
    #     super().restart()
    #     self.x = -20
    #     self.create()
    #     self.is_attack = 1
    #     self.timer_after = int(1.5 * FPS)


    # def create(self):
    #     self.window.image = Window((600, 200), COLOR.WHITE).image
    #     self.window.add(Picture("sprites/hud/player_attack.png", (5, 5)))
    #     self.player_marker = Marker()
    #     self.window.add(self.player_marker)


    # def other_events(self, event):
    #     if self.is_attack:
    #         if event.type == pygame.KEYDOWN:
    #             if event.key in ACTIONS.ENTER:
    #                 dmg = self.calc_damage()
    #                 self.enemy.hp -= dmg
    #                 print(self.enemy.hp, self.enemy.max_hp)
    #                 self.show_health_enemy(dmg)
    #                 self.is_attack = 0


    # def update(self):
    #     self.x += self.speedx*self.is_attack
    #     self.player_marker.rect.x = self.x
    #     if self.is_attack and self.x > 400:
    #         self.is_attack = 0

    #     if not self.is_attack:
    #         self.timer_after -= 1
    #         if self.timer_after <= 0:
    #             print(*self.all_sprites)
    #             if "enemy_health_bar" in dir(self):
    #                 self.enemy_health_bar.kill()
    #             print(*self.all_sprites)
    #             self.active = False


    # def show_health_enemy(self, dmg: int) -> None:
    #     self.enemy_health_bar = HealthBar(self.enemy.hp, self.enemy.max_hp, COLOR.GREEN, (150, 30), (425, 200))
    #     self.damage = Text(f"-{dmg}", 30, COLOR.RED, (900, 100))
    #     self.all_sprites.add(self.enemy_health_bar)
