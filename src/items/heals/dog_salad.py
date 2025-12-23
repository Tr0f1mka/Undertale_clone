from random import choice

from src.base_classes.items import Heal


class DogSalad(Heal):
    name = "Собачий салат"
    param = choice([2, 10, 30])
