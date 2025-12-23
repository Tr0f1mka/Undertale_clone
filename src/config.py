from src.items.weapons.ballet_shoes import BalletShoes
from src.items.weapons.burnt_pan import BurntPan
from src.items.weapons.empty_gun import EmptyGun
from src.items.weapons.real_knife import RealKnife
from src.items.weapons.stick import Stick
from src.items.weapons.torn_notebook import TornNotebook
from src.items.weapons.tough_glove import ToughGlove
from src.items.weapons.toy_knife import ToyKnife
from src.items.weapons.worn_dagger import WornDagger

from src.items.armors.cloudy_glasses import CloudyGlasses
from src.items.armors.cowboy_hat import CowboyHat
from src.items.armors.faded_ribbon import FadedRibbon
from src.items.armors.locket import Locket
from src.items.armors.manly_bandanna import ManlyBandanna
from src.items.armors.old_tutu import OldTutu
from src.items.armors.stained_apron import StainedApron

from src.items.heals.abandoned_quiche import AbandonedQuiche
from src.items.heals.astronaut_food import AstronautFood
from src.items.heals.bandage import Bandage
from src.items.heals.bisicle import Bisicle
from src.items.heals.butterscotch_pie import ButterscotchPie
from src.items.heals.cinnamon_bunny import CinnamonBunny
from src.items.heals.crab_apple import CrabApple
from src.items.heals.dog_salad import DogSalad
from src.items.heals.glamburger import Glamburger
from src.items.heals.hot_dog import HotDog, HotCat
from src.items.heals.hush_puppy import HushPuppy
from src.items.heals.instant_noodles import InstantNoodles
from src.items.heals.junk_food import JunkFood
from src.items.heals.legendary_hero import LegendaryHero
from src.items.heals.monster_candy import MonsterCandy
from src.items.heals.nice_cream import NiceCream
from src.items.heals.potato_chisps import PotatoChisps
from src.items.heals.sea_tea import SeaTea
from src.items.heals.snowman_piece import SnowmanPiece
from src.items.heals.spider_cider import SpiderCider
from src.items.heals.spider_donut import SpiderDonut
from src.items.heals.starfait import Starfait
from src.items.heals.steak_in_the_shape_of_mettatons_face import SteakInTheShapeOfMettatons
from src.items.heals.temmie_flakes import TemmieFlakes


# Буферные массивы(защита от ругани mypy)
WEAPONS = [BalletShoes, BurntPan, EmptyGun, RealKnife, Stick, TornNotebook,ToughGlove, ToyKnife, WornDagger]
ARMORS  = [CloudyGlasses, CowboyHat, FadedRibbon, Locket, ManlyBandanna, OldTutu, StainedApron]
HEALS   = [AbandonedQuiche, AstronautFood, Bandage, Bisicle, ButterscotchPie, CinnamonBunny, CrabApple, DogSalad,
           Glamburger, HotDog, HotCat, HushPuppy, InstantNoodles, JunkFood, LegendaryHero, MonsterCandy, NiceCream,
           PotatoChisps, SeaTea, SnowmanPiece, SpiderCider, SpiderDonut, Starfait, SteakInTheShapeOfMettatons, TemmieFlakes]


# имя, уровень, опыт, золото, здоровье, скорость, оружие, броня, количество атак, инвентарь
PLAYER_CONFIGS = [
    (
        "Обычный",
        12,
        31,
        150,
        34,
        6,
        Stick,
        ManlyBandanna,
        1,
        [MonsterCandy, ButterscotchPie, RealKnife, Bisicle,
        SteakInTheShapeOfMettatons, CowboyHat, SnowmanPiece]
    ),
    (
        "Азаза",
        1,
        0,
        150,
        4,
        6,
        Stick,
        ManlyBandanna,
        1,
        []
    )


]
