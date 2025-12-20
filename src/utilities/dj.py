import pygame
import os


class DJ():

    def __init__(self) -> None:
        pygame.mixer.init()

        self.themes: dict[str, pygame.mixer.Sound] = {}
        self.sounds: dict[str, pygame.mixer.Sound] = {}

        for i in os.listdir("sounds/themes"):
            theme = pygame.mixer.Sound(os.path.join("sounds/themes", i))
            self.themes[i.split(".")[0]] = theme

        for i in os.listdir("sounds/sounds"):
            sound = pygame.mixer.Sound(os.path.join("sounds/sounds", i))
            self.sounds[i.split(".")[0]] = sound

        self.cur_theme = self.themes["papyrus"]


    def set_theme(self, character: str) -> None:

        self.cur_theme.stop()
        self.cur_theme = self.themes[character.lower()]
        self.cur_theme.play(-1)


    def play_sound(self, type: str) -> None:

        self.sounds[type].play()
