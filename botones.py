import pygame
from imagenes import BTPLAY
from imagenes import BTSETT
from imagenes import BTQUIT
from imagenes import SALIDA
from imagenes import ROCK
from imagenes import SISSORS
from imagenes import PAPER
from imagenes import LIZZARD
from imagenes import SPOK
from settings import SIZEBOTONP
from settings import SIZEBOTONS
from settings import SIZEBOTONQ
from settings import SIZEBOTONSA
from settings import SIZEBOTONRO
from settings import SIZEBOTONSI
from settings import SIZEBOTONPA
from settings import SIZEBOTONLI
from settings import SIZEBOTONSP


class Boton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        

class PlayBoton(Boton):
    def __init__(self, botonplay, pos_x, pos_y):
        super().__init__()
        self.surface = pygame.Surface(SIZEBOTONP)
        self.rect = self.surface.get_rect()
        self.botonplay = botonplay
        self.pos_x = pos_x
        self.pos_y = pos_y
        

    def draw(self, surface):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        surface.blit(BTPLAY, self.rect)

class SettBoton(Boton):
    def __init__(self, botonplay, pos_x, pos_y):
        super().__init__()
        self.surface = pygame.Surface(SIZEBOTONS)
        self.rect = self.surface.get_rect()
        self.botonplay = botonplay
        self.pos_x = pos_x
        self.pos_y = pos_y
        

    def draw(self, surface):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        surface.blit(BTSETT, self.rect)


class QuitBoton(Boton):
    
    def __init__(self, botonquit, pos_x, pos_y):
        super().__init__()
        self.surface = pygame.Surface(SIZEBOTONQ)
        self.rect = self.surface.get_rect()
        self.botonquit = botonquit
        self.pos_x = pos_x
        self.pos_y = pos_y
        

    def draw(self, surface):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        surface.blit(BTQUIT, self.rect)

class SalidaBoton(Boton):
    def __init__(self, botonquit, pos_x, pos_y):
        super().__init__()
        self.surface = pygame.Surface(SIZEBOTONSA)
        self.rect = self.surface.get_rect()
        self.botonquit = botonquit
        self.pos_x = pos_x
        self.pos_y = pos_y
        

    def draw(self, surface):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        surface.blit(SALIDA, self.rect)

class RockBoton(Boton):
    def __init__(self, botonrock, pos_x, pos_y):
        super().__init__()
        self.surface = pygame.Surface(SIZEBOTONRO)
        self.rect = self.surface.get_rect()
        self.botonrock = botonrock
        self.pos_x = pos_x
        self.pos_y = pos_y
        

    def draw(self, surface):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        surface.blit(ROCK, self.rect)

class SissorsBoton(Boton):
    def __init__(self, botonsissors, pos_x, pos_y):
        super().__init__()
        self.surface = pygame.Surface(SIZEBOTONSI)
        self.rect = self.surface.get_rect()
        self.botonsissors = botonsissors
        self.pos_x = pos_x
        self.pos_y = pos_y
        

    def draw(self, surface):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        surface.blit(SISSORS, self.rect)

class PaperBoton(Boton):
    def __init__(self, botonpaper, pos_x, pos_y):
        super().__init__()
        self.surface = pygame.Surface(SIZEBOTONPA)
        self.rect = self.surface.get_rect()
        self.botonpaper = botonpaper
        self.pos_x = pos_x
        self.pos_y = pos_y
        

    def draw(self, surface):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        surface.blit(PAPER, self.rect)

class LizzardBoton(Boton):
    def __init__(self, botonlizard, pos_x, pos_y):
        super().__init__()
        self.surface = pygame.Surface(SIZEBOTONLI)
        self.rect = self.surface.get_rect()
        self.botonlizard = botonlizard
        self.pos_x = pos_x
        self.pos_y = pos_y
        

    def draw(self, surface):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        surface.blit(LIZZARD, self.rect)

class SpokBoton(Boton):
    def __init__(self, botonspok, pos_x, pos_y):
        super().__init__()
        self.surface = pygame.Surface(SIZEBOTONSP)
        self.rect = self.surface.get_rect()
        self.botonspok = botonspok
        self.pos_x = pos_x
        self.pos_y = pos_y
        

    def draw(self, surface):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        surface.blit(SPOK, self.rect)