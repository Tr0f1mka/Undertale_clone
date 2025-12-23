from src.base_classes.enemy import Enemy
from src.base_classes.attack import Attack
from src.entities.picture import Picture

from src.constants import WIDTH, HEIGHT


class Sans(Enemy):
    class Attack0(Attack):

        def create_bullets(self):
            ...



    name = "Санс"
    hp = 100
    max_hp = 100
    sprites = [
        Picture("sprites/enemies/sans.png", (WIDTH//2-110, HEIGHT//5-110))
    ]
    cur_sprite = sprites[0]
    image = "sprites/enemies/sans.png"
    cur_attack = 0
    all_attacks = [Attack0]
    prepare_text = "Санс как всегда улыбается"
    actions = []



class Sans1(Enemy):
    class Attack0(Attack):

        def create_bullets(self):
            ...



    name = "Санс"
    hp = 100
    max_hp = 100
    sprites = [
        Picture("sprites/enemies/sans.png", (WIDTH//2-110, HEIGHT//5-110))
    ]
    cur_sprite = sprites[0]
    image = "sprites/enemies/sans.png"
    cur_attack = 0
    all_attacks = [Attack0]
    prepare_text = "Санс как всегда улыбается"
    actions = []
