from src.base_classes.items import Heal
from src.items.weapons.burnt_pan import BurntPan


class Bandage(Heal):
    """
    Пластырь. После снятия становится хилкой
    """

    name = "Пластырь"
    param = 1

    def __call__(self):
        self.player.hp = min(self.player.max_hp, self.player.hp + 10 + 4*int(isinstance(self.player.cur_weapon, BurntPan)))
        self.player.inventory.remove(self)
        if self.player.hp == self.player.max_hp:
            return "Здоровье восполнено до предела"
        else:
            return f"Востановлено {self.param} ОЗ"
