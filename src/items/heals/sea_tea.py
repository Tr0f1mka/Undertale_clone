from src.base_classes.items import Heal


class SeaTea(Heal):
    name = "Морской чай"
    param = 10




    def __call__(self):
        self.player.speed += 3
        return super().__call__()
