import pygame as pg
import modules.entities

class Player(modules.entities.Entity):
    def __init__(self):
        super().__init__()
        self.rect = pg.FRect(50, 50, 50, 50)

    def listen(self, dt):
        self.velocity.xy = (0, 0)

        if pg.key.get_pressed()[pg.K_d]:
            self.velocity.x = 200

        if pg.key.get_pressed()[pg.K_a]:
            self.velocity.x = -200

        if pg.key.get_pressed()[pg.K_s]:
            self.velocity.y = 200

        if pg.key.get_pressed()[pg.K_w]:
            self.velocity.y = -200

    def render(self, display):
        pg.draw.rect(display, (0, 0, 0), self.rect)