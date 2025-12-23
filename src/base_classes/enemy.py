from src.base_classes.attack import Attack
from src.entities.picture import Picture

class Enemy():
    name: str
    hp: int = 1
    max_hp: int
    cur_sprite: Picture
    sprites: list[Picture] = []
    cur_attack: int
    all_attacks: list[type[Attack]]
    prepare_text: str
    actions: list
