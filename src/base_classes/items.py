from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.base_classes.player import Player
    from src.items.weapons.burnt_pan import BurntPan


"""
Базовые классы предметов инвентаря
"""


class Item():
    """
    Базовый класс предмета
    """

    name: str
    param: int
    player: "Player"

    def __init__(self, player: "Player"):
        self.player = player

    def __call__(self):
        pass


class Heal(Item):
    """
    Базовый класс лечащих предметов
    """

    def __call__(self):
        self.player.hp = min(self.player.max_hp, self.player.hp + self.param + 4*int(isinstance(self.player.cur_weapon, BurntPan)))
        self.player.inventory.remove(self)


class Weapon(Item):
    """
    Базовый класс оружия
    """

    def __call__(self):
        buffer = self.player.cur_weapon
        self.player.cur_weapon = self
        self.player.inventory.remove(self)
        self.player.inventory.append(buffer)


class Armor(Item):
    """
    Базовый класс брони
    """

    def __call__(self):
        buffer = self.player.cur_armor
        self.player.cur_armor = self
        self.player.inventory.remove(self)
        self.player.inventory.append(buffer)
