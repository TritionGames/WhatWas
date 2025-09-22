import pygame as pg

class Entity:
    def __init__(self):
        self.rect = pg.FRect(50, 50, 50, 50)
        self.velocity: pg.Vector2 = pg.Vector2(0, 0)
        self.rect_map = []

    def get_collision(self):
        return [rect for rect in self.rect_map if self.rect.colliderect(rect)]

    def update(self, dt):
        self.rect.x += self.velocity.x * dt

        for rect in self.get_collision():
            if self.velocity.x > 0:
                self.rect.right = rect.left
            if self.velocity.x < 0:
                self.rect.left = rect.right

            self.velocity.x = 0

        for rect in self.get_collision():
            if self.velocity.y > 0:
                self.rect.bottom = rect.top
            if self.velocity.v < 0:
                self.rect.top = rect.bottom

            self.velocity.y = 0

        self.rect.y += self.velocity.y * dt