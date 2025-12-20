import pygame

from src.base_classes.item import Item
from src.base_classes.weapon import Weapon


class Player():

    name: str = "Игрок"
    lv: int = 1
    exp: int = 0
    max_hp: int = 16+round(83/20*lv)
    hp: int = max_hp
    speed: int = 6
    cur_weapon: Weapon = Weapon()
    inventory: list[Item] = []
