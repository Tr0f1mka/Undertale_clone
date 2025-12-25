from src.base_classes.stage import Stage

from src.entities.text import Text
from src.entities.window import Window
from src.base_classes.enemy import Enemy

from src.constants import COLOR

class PrepareStage(Stage):

    def __init__(self, enemies: list[Enemy]):
        super().__init__()

        window = Window((900, 230), COLOR.WHITE)
        for i in range(len(enemies)):
            window.add(Text(enemies[i].prepare_text, 30, COLOR.WHITE, (10, 10+70*i)))
        window.rect.topleft = (50, 250)
        self.all_sprites.add(window)
