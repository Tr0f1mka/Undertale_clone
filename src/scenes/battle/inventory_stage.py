import pygame

from src.base_classes.stage import Stage
from src.entities.window import Window
from src.entities.text import Text
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
        self.inventory_not_is_empty = True
        self.is_changed = False

        if self.player.inventory:
            self.buttons: list[list[list[ButtonWithoutBolder]]] = [[[], []], [[], []]]
            for i in range(len(self.player.inventory)):
                button = ButtonWithoutBolder(self.player.inventory[i].name, COLOR.WHITE, COLOR.YELLOW, (10 + ((i // 2) % 2) * 440, 10 + (i % 2) * 100))
                self.buttons[i//4][i%2].append(button)

            self.cur_button = 0
            self.buttons[0][0][0].activate()
            self.cur_part_list = 0
            self.show_num_list = Text("СТРАНИЦА 1", 35, COLOR.WHITE, (660, 185))
            self.window.add(self.show_num_list)
            for i in self.buttons[0]:
                self.window.add(i)

        else:
            self.window.add(Text("Ваш инвентарь пуст", 30, COLOR.WHITE, (10, 10)))
            self.inventory_not_is_empty = False



# ┌                       ┐
# │ ┌       ┐  ┌       ┐  │
# │ │ [] [] │  │ [] [] │  │
# │ │ [] [] │  │ [] [] │  │
# │ └       ┘  └       ┘  │
# └                       ┘

    def other_events(self, event):

        if self.is_changed:
            if event.type == pygame.KEYDOWN:
                if event.key in ACTIONS.ENTER:
                    self.active = False
                    self.dj.play_sound("select")

        if not self.is_changed:
            if self.inventory_not_is_empty:
                if event.type == pygame.KEYDOWN:
                    if event.key in ACTIONS.LEFT:
                        self.select_button(-2)
                    if event.key in ACTIONS.RIGHT:
                        self.select_button(+2)
                    if event.key in ACTIONS.UP:
                        self.select_button(-1)
                    if event.key in ACTIONS.DOWN:
                        self.select_button(+1)
                    if event.key in ACTIONS.ENTER:
                        for i in self.buttons[self.cur_part_list]:
                            self.window.remove(i)
                        self.window.remove(self.show_num_list)

                        message = self.player.inventory[self.cur_button]()
                        self.window.add(Text(message, 30, COLOR.WHITE, (10, 10)))
                        self.is_changed = True
                        self.dj.play_sound("select")

        if event.type == pygame.KEYDOWN:
            if event.key in ACTIONS.CANCEL:
                self.active = False
                self.dj.play_sound("select")


    def calc_button(self, shift):

        # 1 - переключение на соседнюю кнопку(перемещение по вертикали)
        if abs(shift) == 1:
            return (self.cur_button+shift)%len(self.player.inventory)
        # 2 - перемещение по горизонтали
        if not(len(self.player.inventory)%2):
            return (self.cur_button+shift)%len(self.player.inventory)
        else:
            column = self.cur_button//2
            row = self.cur_button%2
            column += shift//2
            if column*2 + row >= len(self.player.inventory):
                column = 0
            if column*2+row < 0:
                column = (len(self.player.inventory)-1)//2
                if row:
                    column -= 1
            return column*2+row


    def select_button(self, shift: int) -> None:
        next_but = self.calc_button(shift)
        self.dj.play_sound("select")
        self.change_button(next_but)


    def change_button(self, next_but: int) -> None:
        if self.cur_button != next_but:
            print(next_but, next_but//4, next_but%2, next_but%4//2)
            self.buttons[next_but//4][next_but%2][next_but%4//2].activate()
            self.buttons[self.cur_button//4][self.cur_button%2][self.cur_button%4//2].deactivate()
            if self.cur_part_list != next_but//4:
                for i in self.buttons[self.cur_part_list]:
                    self.window.remove(i)
                for i in self.buttons[next_but//4]:
                    self.window.add(i)
                self.cur_part_list = next_but//4
                self.show_num_list.image = Text(f"СТРАНИЦА {self.cur_part_list+1}", 35, COLOR.WHITE).image
            self.cur_button = next_but
