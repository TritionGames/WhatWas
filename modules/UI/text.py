import pygame as pg

class Text:
    def __init__(self, pos: tuple[int, int], font: pg.Font, text: str = "Text", color: tuple[int, int, int] = (0, 0, 0)):
        self.pos: tuple[int, int, int] = pos
        self.text: tuple[int, int, int] = text
        self.color: tuple[int, int, int] = color
        self.font: pg.Font = font
        self.surface: pg.Surface = self.font.render(self.text, False, self.color)

    def render(self, display: pg.Surface):
        display.blit(self.surface, self.pos)