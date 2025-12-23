from src.base_classes.items import Heal


class Bisicle(Heal):
    name = "Дваскимо"
    param = 11



    def __call__(self):
        self.player.inventory.append(Unisicle(self.player))
        return super().__call__()


class Unisicle(Heal):
    name = "Односкимо"
    param = 11
