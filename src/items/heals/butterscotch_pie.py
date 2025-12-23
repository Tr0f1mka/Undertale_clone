from src.base_classes.items import Heal


class ButterscotchPie(Heal):
    name = "Пирог"

    def __call__(self):
        self.player.hp = self.player.max_hp
        self.player.inventory.remove(self)
        return "Здоровье восполнено до предела"
