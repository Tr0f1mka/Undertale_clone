import pygame

from src.base_classes.stage import Stage
from src.entities.window import Window
from src.entities.button_without_bolder import ButtonWithoutBolder
from src.base_classes.player import Player
from src.utilities.dj import DJ

from src.constants import COLOR, ACTIONS


class InventoryStage(Stage):

    def __init__(self, player: Player, dj: DJ):
        super().__init__()
        self.player = player
        self.dj = dj


    def restart(self):
        super().restart()
        self.window = Window((900, 230), COLOR.WHITE, (50, 250))
        self.all_sprites.add(self.window)
        self.buttons: list[list[list[ButtonWithoutBolder]]] = [[[], []], [[], []]]
        for i in range(len(self.player.inventory)):
            button = ButtonWithoutBolder(self.player.inventory[i].name, COLOR.WHITE, COLOR.YELLOW, (10 + ((i // 2) % 2) * 440, 10 + (i % 2) * 100))
            self.buttons[i//4][i%2].append(button)

        self.cur_button = 0
        self.buttons[0][0][0].activate()
        self.cur_part_list = 0
        for i in self.buttons[0]:
            self.window.add(i)



# ┌                       ┐
# │ ┌       ┐  ┌       ┐  │
# │ │ [] [] │  │ [] [] │  │
# │ │ [] [] │  │ [] [] │  │
# │ └       ┘  └       ┘  │
# └                       ┘

    def other_events(self, event):
        next_but = self.cur_button
        if event.type == pygame.KEYDOWN:
            if event.key in ACTIONS.LEFT:
                next_but = (next_but - 2) % 8
                self.dj.play_sound("select")
                self.change_button(next_but)
            if event.key in ACTIONS.RIGHT:
                next_but = (next_but + 2) % 8
                self.dj.play_sound("select")
                self.change_button(next_but)
            if event.key in ACTIONS.UP:
                next_but = (next_but - 1) % 8
                self.dj.play_sound("select")
                self.change_button(next_but)
            if event.key in ACTIONS.DOWN:
                next_but = (next_but + 1) % 8
                self.dj.play_sound("select")
                self.change_button(next_but)


            if event.key in ACTIONS.CANCEL:
                self.active = False
                self.dj.play_sound("select")


    def change_button(self, next_but: int) -> None:
        if self.cur_button != next_but:
            self.buttons[next_but//4][next_but%2][next_but%4//2].activate()
            self.buttons[self.cur_button//4][self.cur_button%2][self.cur_button%4//2].deactivate()
            if self.cur_part_list != next_but//4:
                for i in self.buttons[self.cur_part_list]:
                    self.window.remove(i)
                for i in self.buttons[next_but//4]:
                    self.window.add(i)
                self.cur_part_list = next_but//4
            self.cur_button = next_but
