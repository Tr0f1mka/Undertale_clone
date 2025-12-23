from src.base_classes.items import Item
from src.base_classes.items import Weapon, Armor


class Player():

    name: str = "Игрок"
    lv: int = 1
    exp: int = 0
    max_hp: int = 16+round(83/20*lv)
    hp: int = max_hp
    speed: int = 6
    base_damage: int = 1
    cur_weapon: Weapon
    cur_armor: Armor
    count_attacks: int = 1
    inventory: list[Item] = []
