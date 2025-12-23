from src.base_classes.items import Heal


class SeaTea(Heal):
    name = "Морской чай"
    param = 10




    def __call__(self):
        super().__call__()
        self.player.speed += 3
