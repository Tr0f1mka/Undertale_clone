from src.base_classes.enemy import Enemy
from src.base_classes.attack import Attack

class Sans(Enemy):
    class Attack0(Attack):

        def create_bullets(self):
            ...



    name = "Санс"
    hp = 100
    image = "sprites/enemies/sans.png"
    cur_attack = 0
    all_attacks = [Attack0]
    prepare_text = "Санс как всегда улыбается"
    actions = []
