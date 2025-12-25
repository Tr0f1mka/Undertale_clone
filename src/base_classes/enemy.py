import pygame

from src.base_classes.attack import Attack


class Enemy():
    name: str
    hp: int = 1
    max_hp: int
    mercy: int
    sprite: pygame.sprite.Sprite
    attack: int
    all_attacks: list[type[Attack]]
    prepare_text: str
    actions: list
