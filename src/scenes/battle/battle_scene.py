import pygame

from src.scenes.battle.prepare_stage import PrepareStage
from src.scenes.battle.battle_stage import BattleStage
from src.scenes.battle.action_stage import ActionStage
from src.scenes.battle.inventory_stage import InventoryStage
from src.scenes.battle.escape_stage import EscapeStage
from src.base_classes.scene import Scene
from src.base_classes.stage import Stage

from src.utilities.dj import DJ
from src.entities.button import Button
from src.entities.text import Text
from src.entities.health_bar import HealthBar
from src.base_classes.enemy import Enemy
from src.base_classes.player import Player

from src.constants import COLOR, ACTIONS, WIDTH


class BattleScene(Scene):
    """
    Сцена битвы
    """

    def __init__(self, enemies: list[Enemy], player: Player, dj: DJ) -> None:
        """
        :param enemy: Текущий враг
        :param player: Игрок
        :param dj: Диджей для звуков/темы
        :return: Ничего
        """

        self.enemies = enemies
        self.player = player
        self.all_sprites = pygame.sprite.Group()
        self.set_sprites_enemies()
        self.dj = dj
        self.dj.set_theme(enemies[0].__class__.__name__)
        self.init_buttons()
        self.buttons[0].activate()
        self.stages: list[Stage] = [BattleStage(self.enemies, self.player, self.dj), ActionStage(self.dj), InventoryStage(self.player, self.dj), EscapeStage(self.dj), PrepareStage(self.enemies)]
        self.cur_stage = 4
        self.menu = True
        self.init_stats()


    def set_sprites_enemies(self) -> None:
        """
        Устанавливает координаты спрайтов противников
        :return: Ничего
        """

        parts = len(self.enemies)+1
        for i in range(len(self.enemies)):
            self.enemies[i].cur_sprite.rect.centerx = int(WIDTH/parts*(i+1))
            self.all_sprites.add(self.enemies[i].cur_sprite)
            print(id(self.enemies[i].cur_sprite))


    def init_buttons(self):
        messages = ["БИТВА", "ДЕЙСТВИЕ", "ВЕЩИ", "ПОЩАДА"]
        self.buttons: list[Button] = []
        for i, message in enumerate(messages):
            but = Button(message, COLOR.ORANGE, COLOR.YELLOW, (50+230*i, 530))
            self.buttons.append(but)
            self.all_sprites.add(but)
        self.cur_button = 0


    def init_stats(self):
        nick_name = Text(self.player.name.upper(), 30, COLOR.WHITE, (50, 490))
        if "ё" in self.player.name.lower() or "й" in self.player.name.lower():
            nick_name.rect.y = 487
        self.all_sprites.add(nick_name)
        lv = Text(f"УР {self.player.lv}", 30, COLOR.WHITE, (200, 490))
        self.all_sprites.add(lv)
        oz = Text("оз", 30, COLOR.WHITE, (400, 486))
        self.all_sprites.add(oz)
        self.health_bar = HealthBar(self.player.hp, self.player.max_hp, COLOR.YELLOW, (100, 30), (450, 490))
        self.all_sprites.add(self.health_bar)
        self.hp = Text(f"{self.player.hp} / {self.player.max_hp}", 30, COLOR.WHITE, (575, 490))
        self.all_sprites.add(self.hp)


    def other_events(self, event):
        if self.menu:

            next_but = self.cur_button
            if event.type == pygame.KEYDOWN:

                if event.key in ACTIONS.LEFT:
                    next_but = (next_but - 1) % 4
                    self.dj.play_sound("select")
                    self.change_button(next_but)

                elif event.key in ACTIONS.RIGHT:
                    next_but = (next_but + 1) % 4
                    self.dj.play_sound("select")
                    self.change_button(next_but)

                elif event.key in ACTIONS.ENTER:
                    self.menu = False
                    self.cur_stage = self.cur_button
                    self.stages[self.cur_stage].restart()
                    self.buttons[self.cur_button].deactivate()
                    self.dj.play_sound("select")

        else:
            self.stages[self.cur_stage].other_events(event)


    def change_button(self, next_but: int):
        if self.cur_button != next_but:
            self.buttons[self.cur_button].deactivate()
            self.buttons[next_but].activate()
            self.cur_button = next_but


    def update(self):
        self.stages[self.cur_stage].update()
        self.menu = not(self.stages[self.cur_stage].active)
        if self.menu:
            self.buttons[self.cur_button].activate()
            self.cur_stage = 4
        self.health_bar.redraw(self.player.hp)
        self.hp.image = Text(f"{self.player.hp} / {self.player.max_hp}", 30, COLOR.WHITE).image
        return super().update()


    def render(self, screen):
        screen.fill(COLOR.BLACK)
        self.all_sprites.update()
        self.all_sprites.draw(screen)
        self.stages[self.cur_stage].render(screen)
        pygame.display.flip()
