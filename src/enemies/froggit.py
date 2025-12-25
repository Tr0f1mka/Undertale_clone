import pygame
from math import sin, cos

from src.base_classes.enemy import Enemy
from src.base_classes.attack import Attack

from src.constants import WIDTH, HEIGHT, COLOR


class Froggit(Enemy):

    class Avatar(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()

            self.base_image = pygame.Surface((220, 220))
            self.base_image.fill(COLOR.BLACK)
            self.base_image.blit(pygame.image.load("sprites/enemies/froggit_body.png"), (39, 39))
            self.head = pygame.image.load("sprites/enemies/froggit_head.png")
            self.t = 0
            self.render()
            self.rect = self.image.get_rect()
            self.rect.topleft = (WIDTH//2-110, HEIGHT//5-110)

        def render(self):
            self.image = self.base_image.copy()
            self.image.blit(self.head, (25*sin(2*self.t/50)+35, 15*sin(2*self.t/50)*cos(2*self.t/50)+40))

        def update(self):
            self.t += 1
            self.render()



    class Attack0(Attack):

        def __init__(self):
            super().__init__()
            ...

        def create_bullets(self):
            ...



    name = "Фроггит"
    hp = 30
    max_hp = 30
    mercy = 2
    attack = 5
    prepare_text = "Фроггит преграждает вам путь!"


    def __init__(self):
        self.sprite = self.Avatar()
        self.all_attacks = [self.Attack0]
        self.actions = []
