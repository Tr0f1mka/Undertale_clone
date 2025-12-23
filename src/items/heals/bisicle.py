from src.base_classes.items import Heal


class Bisicle(Heal):
    name = "Дваскимо"
    param = 11



    def __call__(self):
        super().__call__()
        self.player.inventory.append(Unisicle(self.player))


class Unisicle(Heal):
    name = "Односкимо"
    param = 11
