from src.base_classes.items import Heal


class ButterscotchPie(Heal):
    name = "Ирисково-коричный пирог"

    def __call__(self):
        self.player.hp = self.player.max_hp
