from src.base_classes.attack import Attack

class Enemy():
    name: str
    hp: int
    image: str
    cur_attack: int
    all_attacks: list[Attack]
    prepare_text: str
    actions: list
