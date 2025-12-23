from src.base_classes.items import Heal


class LegendaryHero(Heal):
    name = "Легендарный герой"
    param = 40




    def __call__(self):
        super().__call__()
        self.player.base_damage += 4
