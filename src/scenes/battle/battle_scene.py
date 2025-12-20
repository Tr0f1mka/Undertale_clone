import pygame

from src.scenes.battle.prepare_stage import PrepareStage
from src.scenes.battle.battle_stage import BattleStage
from src.scenes.battle.action_stage import ActionStage
from src.scenes.battle.inventory_stage import InventoryStage
from src.scenes.battle.escape_stage import EscapeStage
from src.base_classes.scene import Scene
from src.base_classes.stage import Stage

from src.utilities.dj import DJ
from src.entities.picture import Picture
from src.entities.button import Button
from src.base_classes.enemy import Enemy
from src.base_classes.player import Player

from src.constants import COLOR, WIDTH, HEIGHT


class BattleScene(Scene):

    def __init__(self, enemy: Enemy, player: Player):

        self.enemy = enemy
        self.player = player
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(Picture(self.enemy.image, (WIDTH//2-110, HEIGHT//5-110)))
        self.dj = DJ()
        self.dj.set_theme(enemy.__class__.__name__)
        self.init_buttons()
        self.buttons[0].activate()
        self.stages: list[Stage] = [BattleStage(self.enemy, self.player), ActionStage(), InventoryStage(self.player), EscapeStage(), PrepareStage(self.enemy.prepare_text)]
        self.cur_stage = 4
        self.menu = True


    def init_buttons(self):
        messages = ["БИТВА", "ДЕЙСТВИЕ", "ВЕЩИ", "ПОЩАДА"]
        self.buttons: list[Button] = []
        for i, message in enumerate(messages):
            but = Button(message, COLOR.ORANGE, COLOR.YELLOW, (50+230*i, 530))
            self.buttons.append(but)
            self.all_sprites.add(but)
        self.cur_button = 0


    def other_events(self, event):
        if self.menu:
            next_but = self.cur_button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    next_but -= 1
                    if next_but < 0:
                        next_but = 0
                    self.dj.play_sound("select")
                    self.change_button(next_but)
                elif event.key == pygame.K_RIGHT:
                    next_but += 1
                    if next_but > 3:
                        next_but = 3
                    self.dj.play_sound("select")
                    self.change_button(next_but)
                elif event.key == pygame.K_RETURN:
                    self.menu = False
                    self.cur_stage = self.cur_button
                    self.stages[self.cur_stage].restart()
                    self.buttons[self.cur_button].deactivate()
                    self.dj.play_sound("select")

        else:
            self.menu = self.stages[self.cur_stage].other_events(event)
            if self.menu:
                self.buttons[self.cur_button].activate()
                self.cur_stage = 4


    def change_button(self, next_but: int):
        if self.cur_button != next_but:
            self.buttons[self.cur_button].deactivate()
            self.buttons[next_but].activate()
            self.cur_button = next_but


    def update(self):
        self.stages[self.cur_stage].update()
        return super().update()


    def render(self, screen):
        screen.fill(COLOR.BLACK)
        self.all_sprites.update()
        self.all_sprites.draw(screen)
        self.stages[self.cur_stage].render(screen)
        pygame.display.flip()
