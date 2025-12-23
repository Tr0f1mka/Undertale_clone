from src.base_classes.scene import Scene


class Stage(Scene):

    active: bool = False

    def restart(self):
        self.active = True
        self.all_sprites.empty()

    def render(self, screen):
        self.all_sprites.update()
        self.all_sprites.draw(screen)
