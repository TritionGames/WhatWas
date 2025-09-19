import pygame as pg

class Buttons:
    def __init__(self, rect: pg.Rect | tuple[float, float, float, float], text_surface: str):
        self.rect: pg.Rect = rect if isinstance(rect, pg.Rect) else pg.Rect(*rect)
        self.origin: tuple[int, int] = self.rect.topleft
        self.hover: bool = False
            
        self.text_surface: pg.Surface = text_surface
        
    def render(self, display: pg.Surface):
        display.blit(self.text_surface, self.rect.topleft)

    def update(self):
        self.hover = False

        if not self.rect.collidepoint(pg.mouse.get_pos()):
            return False
        
        self.hover = True

        if pg.mouse.get_just_released()[0]:
            return True