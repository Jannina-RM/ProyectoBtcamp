import pygame
import sys
import random
from settings import *
from imagenes import *
from botones import *
from pathlib import Path
current_path = Path.cwd()
document_path = current_path / "documents"/ "saves.txt"

class Mouse(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, 0, 0, 1, 1)
    def Update(self):
        self.left, self.top = pygame.mouse.get_pos()

class Game:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICONO)
        self.botonrock = RockBoton(Boton, 20, 510)
        self.botonsissors = SissorsBoton(Boton, 90, 510)
        self.botonpaper = PaperBoton(Boton, 160, 510)
        self.botonlizzard = LizzardBoton(Boton, 230, 510)
        self.botonspok = SpokBoton(Boton, 300, 510)
        self.gameover = "G A M E O V E R"
        self.respuesta = " "
        self.game = True
    
    def star(self):
        self.menu()
        self.new()
        
    def new(self):
        self.scoreplayer = 0
        self.scoremaquina = 0
        self.playing = True
        self.rungame()
        

    
    def rungame(self):
        
        while self.game:

            self.events()
            self.update()
            self.draw()
        


    def events(self):

        self.artificialint()
        self.opcionesplayer()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.botonsalida.rect.collidepoint(pos):
                    self.game = False
                elif self.botonrock.rect.collidepoint(pos):
                    sonido = pygame.mixer.Sound(ROCKSD)
                    sonido.set_volume(0.2)
                    sonido.play()
                    if self.botonrock == self.artint:
                        self.respuesta = "Empate"
                    elif self.opcionesp == self.botonrock and self.artint == self.botonsissors or self.artint == self.botonlizzard:
                        self.respuesta = "GANASTE!!"
                        self.scoreplayer += 1
                    else:
                        self.respuesta = "Perdiste.."
                        self.scoremaquina += 1

                elif self.botonsissors.rect.collidepoint(pos):
                    sonido = pygame.mixer.Sound(SISSORSSD)
                    sonido.set_volume(0.1)
                    sonido.play()
                    if self.botonsissors == self.artint:
                        self.respuesta = "Empate"
                    elif self.opcionesp == self.botonsissors and self.artint == self.botonpaper or self.artint == self.botonlizzard:
                        self.respuesta = "GANASTE!!"
                        self.scoreplayer += 1
                    else:
                        self.respuesta = "Perdiste.."
                        self.scoremaquina += 1

                elif self.botonpaper.rect.collidepoint(pos):
                    sonido = pygame.mixer.Sound(PAPERSD)
                    sonido.set_volume(0.3)
                    sonido.play()
                    if self.botonpaper == self.artint:
                        self.respuesta = "Empate"
                    elif self.opcionesp == self.botonpaper and self.artint == self.botonrock or self.artint == self.botonspok:
                        self.respuesta = "GANASTE!!"
                        self.scoreplayer += 1
                    else:
                        self.respuesta = "Perdiste.."
                        self.scoremaquina += 1

                elif self.botonlizzard.rect.collidepoint(pos):
                    sonido = pygame.mixer.Sound(CODYSD)
                    sonido.set_volume(0.2)
                    sonido.play()
                    if self.botonlizzard == self.artint:
                        self.respuesta = "Empate"
                    elif self.opcionesp == self.botonlizzard and self.artint == self.botonspok or self.artint == self.botonpaper:
                        self.respuesta = "GANASTE!!"
                        self.scoreplayer += 1
                    else:
                        self.respuesta = "Perdiste.."
                        self.scoremaquina += 1

                elif self.botonspok.rect.collidepoint(pos):
                    sonido = pygame.mixer.Sound(SPOKSD)
                    sonido.set_volume(0.7)
                    sonido.play()
                    if self.botonspok == self.artint:
                        self.respuesta = "Empate"
                    elif self.opcionesp == self.botonspok and self.artint == self.botonrock or self.artint == self.botonsissors:
                        self.respuesta = "GANASTE!!"
                        self.scoreplayer += 1
                    else:
                        self.respuesta = "Perdiste.."
                        self.scoremaquina += 1
            elif self.scoreplayer >= 20:
                self.playing = False
                
            elif self.scoremaquina >= 20:
                self.playing = False


                
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and not self.playing:
            self.write_score()
            self.new()

    def artificialint(self):
        self.opciones = (self.botonrock, self.botonsissors, self.botonpaper,
        self.botonlizzard, self.botonspok)
        self.artint = random.choice(self.opciones)

    def opcionesplayer(self):
        self.opcionesp = (self.botonrock, self.botonsissors, self.botonpaper,
        self.botonlizzard, self.botonspok)

    def draw_text(self):
        self.display_text(self.respuesta, 48, WHITE, 800//2, 100)
        self.display_text(str(self.scoreplayer), 25, WHITE, 80, 40)
        self.display_text(str(self.scoremaquina), 25, WHITE, 715, 40)
        
        if not self.playing:
            self.display_text(self.gameover, 60, WHITE, 800//2, 600//2)
            self.display_text("Presiona ESPACIO para reiniciar", 40, WHITE, 800//2, 400)
            
    def display_text(self, text, size, color, pos_x, pos_y):
        font = pygame.font.Font("freesansbold.ttf", size)
        text = font.render(text, True, color)
        rect = text.get_rect()
        rect.midtop = (pos_x, pos_y)
        self.screen.blit(text, rect)

    def menu(self):
        
        self.botonplay = PlayBoton(Boton, 40,380)
        self.botonsett = SettBoton(Boton, 40,455)
        self.botonquit = QuitBoton(Boton, 65, 530)
        self.screen.blit(BACKGROUND, (0, 0))
        self.screen.blit(CODYM, (300, 50))
        self.botonplay.draw(self.screen)
        self.botonsett.draw(self.screen)
        self.botonquit.draw(self.screen)
        self.screen.blit(TITULOM, (10, 10))

        pygame.display.flip()

        self.wait()

    def wait(self):
        wait = True
        pygame.mixer.init()
        pygame.mixer.music.load("music/musicamenu.wav")
        pygame.mixer.music.play(-1, 0, 0)
        pygame.mixer.music.set_volume(0.1)
        while wait:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    wait = False
                    self.rungame = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.botonquit.rect.collidepoint(pos):
                        wait = False
                        self.rungame = False
                        pygame.quit()
                        sys.exit()
                    if self.botonplay.rect.collidepoint(pos):
                        wait = False
                        pygame.mixer.init()
                        pygame.mixer.music.load(MUSICGAME)
                        pygame.mixer.music.play(-1, 0, 0)
                        pygame.mixer.music.set_volume(0.1)

    def draw(self):
        self.scores()
        self.botonsalida = SalidaBoton(Boton, 730, 530)
        self.botonrock = RockBoton(Boton, 20, 510)
        self.botonsissors = SissorsBoton(Boton, 90, 510)
        self.botonpaper = PaperBoton(Boton, 160, 510)
        self.botonlizzard = LizzardBoton(Boton, 230, 510)
        self.botonspok = SpokBoton(Boton, 300, 510)
        self.fuentescore = pygame.font.Font("freesansbold.ttf", 18)
        self.textoplayer = self.fuentescore.render("PLAYER SCORE", True, WHITE)
        self.textoai = self.fuentescore.render("A.I. SCORE", True, WHITE)
        self.screen.blit(BG_GAME, (0, 0))
        self.screen.blit(VS, (330, 200))
        self.botonsalida.draw(self.screen)
        self.botonrock.draw(self.screen)
        self.botonsissors.draw(self.screen)
        self.botonpaper.draw(self.screen)
        self.botonlizzard.draw(self.screen)
        self.botonspok.draw(self.screen)
        pygame.draw.rect(self.screen, BLACK, self.scorep)
        pygame.draw.rect(self.screen, BLACK, self.scoreai)
        self.screen.blit(self.textoplayer, (15, 10))
        self.screen.blit(self.textoai, (667, 10))
        self.draw_text()
        pygame.display.update()
        pygame.display.flip()

    def update(self):
        if self.playing:
            pass
            
            
            
        
    def scores(self):
        
        self.scorep = pygame.Rect(10, 10, 150, 60)
        self.scoreai = pygame.Rect(640, 10, 150, 60)

    def write_score(self):
        with open(document_path, "a") as file:
            file.write("Player score: " + str(self.scoreplayer) + "\n")
    
    def stop(self):
        self.playing = False
    