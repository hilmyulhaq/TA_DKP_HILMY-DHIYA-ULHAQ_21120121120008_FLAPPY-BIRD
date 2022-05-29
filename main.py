from tkinter import END
import pygame
import sys
from pygame.locals import *
from random import *


#variabel layar
LEBAR = 480
TINGGI = 600
FPS = 30
# Variabel game
gravity = 0
pos_list = [[-400,200], [-400, 250], [-220, 450], [-50, 550], [-230, 400]]
score = 0

# VARIABEL WARNA
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORCHID = (191, 62, 255)
BLUE = (0, 0, 255)
CORNSILK = (255,248,220)
RED = (255,48,48)
GREEN = (0,201,87)


pygame.init()
screen = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption('FLAPPY BIRD')
clock = pygame.time.Clock() #menciptakan objek untuk membantu melacak waktu


def buat_pipa():
    y_pos = choice(pos_list)
    pipa1 = Top(y_pos[0])
    pipa2 = Bottom(y_pos[1])
    detection = DetectionPoint(pipa2.rect.x, y_pos[1])
    pipas.add(pipa1)
    pipas.add(pipa2)
    all_sprites.add(pipa1)#menampilkan pipa ke layar
    all_sprites.add(pipa2)
    detect_group.add(detection)
    all_sprites.add(detection)


def tampil_text(text,font_size,font_color,x,y):
    font = pygame.font.SysFont(None, font_size) #font bawaan system
    font_surface = font.render(text, True,font_color )
    screen.blit(font_surface,(x,y))

def layar_game_over():
    screen.fill (BLACK)
    tampil_text("Game Selesai" , 40 , BLUE , LEBAR//2 - 100, TINGGI//4 )
    tampil_text("Score Anda adalah = {}".format(score),25,GREEN ,LEBAR//2-100 ,TINGGI//4 + 50)
    tampil_text("tekan tombol bebas untuk melanjutkan ",25,CORNSILK, LEBAR//2-175,TINGGI//4 + 100)

    pygame.display.flip() #mengupdate surface

    waiting_game_over = True
    while waiting_game_over:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == KEYUP:
                waiting_game_over = False




class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(ORCHID)
        self.rect = self.image.get_rect() 
        self.rect.x = 50
        self.rect.y = TINGGI // 2
    
    def update(self): #method untuk update burung game over
        global game_over
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y > TINGGI:
            game_over = True

   



class Pipa(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 500))
        self.image.fill (RED)
        self.rect = self.image.get_rect()
        self.rect.x = 400
    
    def update(self):
        self.rect.x -= 4
        if self.rect.x < - 20:
            self.kill()

class Top(Pipa):#inheritance
    def __init__(self, y):
        super().__init__()
        self.rect.y = y #posisi y ditaruh di koordinat y

class Bottom(Pipa):#inheritance
    def __init__(self, y):
        super().__init__()
        self.rect.y = y
        

class DetectionPoint(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((20, 120))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y
        self.hit = False

    def update(self):
        self.rect.x -= 4
        if self.rect.x < -20:
            self.kill()#menghapus semua sprite dari semua grup



all_sprites = pygame.sprite.Group()
detect_group = pygame.sprite.Group()
pipas = pygame.sprite.Group()
bird = Bird()


buat_pipa()

all_sprites.add(bird)

# Game loop
game_over = False
run = True
while run:
    if game_over:
        layar_game_over()
        all_sprites = pygame.sprite.Group()
        detect_group = pygame.sprite.Group()
        pipas = pygame.sprite.Group()
        bird = Bird() 

        buat_pipa()

        all_sprites.add(bird)
        score = 0
        game_over = False

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                gravity = 0  
                gravity -= 5


    gravity += 0.25
    bird.rect.y += gravity
    #cek tabrakan dengan detection point
    bird_hit_point = pygame.sprite.spritecollide(bird, detect_group, False)
    if bird_hit_point and not bird_hit_point[0].hit:
        score += 1
        bird_hit_point[0].hit = True
        


    #cek tabrakan bird dengan pipa
    bird_hit_pipa = pygame.sprite.spritecollide(bird, pipas, False)
    if bird_hit_pipa:
        game_over = True

        
    if len(pipas) <= 0:
        buat_pipa()

    
    
    all_sprites.update()
    screen.fill(BLACK) #menghapus jejak gravity    
    all_sprites.draw(screen)
    tampil_text(str(score), 28, WHITE, LEBAR//2,TINGGI//4-100 )
    
    pygame.display.flip()

pygame.quit()    
