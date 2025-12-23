from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.base_classes.player import Player


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

    def __init__(self, player: "Player") -> None:
        self.player = player

    def __call__(self) -> str:
        return ""


class Heal(Item):
    """
    Базовый класс лечащих предметов
    """

    def __call__(self) -> str:
        self.player.hp = min(self.player.max_hp, self.player.hp + self.param + 4*int(self.player.cur_weapon.__class__.__name__ == "BurntPan"))
        self.player.inventory.remove(self)
        if self.player.hp == self.player.max_hp:
            return "Здоровье восполнено до предела"
        else:
            return f"Востановлено {self.param} ОЗ"


class Weapon(Item):
    """
    Базовый класс оружия
    """

    def __call__(self):
        buffer = self.player.cur_weapon
        self.player.cur_weapon = self
        self.player.inventory.remove(self)
        self.player.inventory.append(buffer)
        return f"Было экипировано: {self.name}"


class Armor(Item):
    """
    Базовый класс брони
    """

    def __call__(self):
        buffer = self.player.cur_armor
        self.player.cur_armor = self
        self.player.inventory.remove(self)
        self.player.inventory.append(buffer)
        return f"Было экипировано: {self.name}"
