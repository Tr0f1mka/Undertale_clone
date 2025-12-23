from src.base_classes.items import Item
from src.base_classes.items import Weapon, Armor


class Player():

    name: str
    lv: int
    exp: int
    max_hp: int
    hp: int
    gold: int
    speed: int
    base_damage: int = 1
    cur_weapon: Weapon
    cur_armor: Armor
    count_attacks: int
    inventory: list[Item] = []


    # имя, уровень, опыт, золото, здоровье, скорость, оружие, броня, количество атак, инвентарь
    def __init__(self, config: tuple[str, int, int, int, int, int, type[Weapon], type[Armor], int, list[type[Item]]]):
        self.name = config[0]
        self.lv = config[1]
        self.exp = config[2]
        self.gold = config[3]
        self.hp = config[4]
        self.speed = config[5]
        self.cur_weapon = config[6](self)
        self.cur_armor = config[7](self)
        self.count_attacks = config[8]
        self.inventory = [i(self) for i in config[9]]

        self.max_hp = 16+round(83/20*self.lv)
