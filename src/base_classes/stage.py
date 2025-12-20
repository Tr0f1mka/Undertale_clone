from src.base_classes.scene import Scene


class Stage(Scene):

    def restart(self):
        pass

    def render(self, screen):
        self.all_sprites.update()
        self.all_sprites.draw(screen)
