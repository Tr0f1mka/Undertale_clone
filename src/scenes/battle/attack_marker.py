import pygame

from src.constants import COLOR


class Marker(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # Создаем изображение с поддержкой альфа-канала
        self.original_image = pygame.Surface((8, 200), pygame.SRCALPHA)
        self.original_image.fill(COLOR.WHITE)

        # Копия для работы
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.topleft = (-20, 0)

        # Параметры затухания
        self.alpha = 255  # Полностью непрозрачный
        self.fade_speed = 15  # Скорость затухания

        # Флаг затухания
        self.is_fading = False
        self.pressed = False


    def update(self) -> None:
        """
        Обновление спрайта
        :return: Ничего
        """

        if self.is_fading:
            if self.alpha > 0:
                # Уменьшаем альфа-канал
                self.alpha = max(0, self.alpha - self.fade_speed)

                # Создаем новое изображение с прозрачностью
                self.image = self.original_image.copy()
                self.image.set_alpha(self.alpha)

                # Если полностью затух, удаляем
                if self.alpha <= 0:
                    self.kill()

        else:
            if self.pressed:
                self.is_fading = True
                return

            self.rect.x += 8
            if self.rect.x > 400:
                self.is_fading = True
