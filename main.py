import pygame
from pygame.locals import * #import semua constant dari pygame

#variable
LEBAR = 500
TINGGI = 650
FPS = 30

#variabel warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0 , 255 ,0)
BLUE = (0, 0, 255)




pygame.init()#inisialisasi pygame
layar = pygame.display.set_mode((LEBAR, TINGGI ))

pygame.display.set_caption ('FLAPPY BIRD') #setel keterangan dari window
clock = pygame.time.Clock() #create an object to help track time

class burung (pygame.sprite.Sprite): #inheritance
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(RED)
        self.rect  = self.image.get_rect() #pygame object to store rectangular coordinates
        self.rect.x = 50
        self.rect.y = TINGGI // 2 #Means floor division integer result 
        

all_sprites = pygame.sprite.Group()
bird = burung()
all_sprites.add(bird)
#loop game
        
run = True
while run:
    clock.tick(FPS)
    for event  in pygame.event.get(): #mendapatkan event dari queue
        if event.type == QUIT:
            run = False
    all_sprites.draw(layar)
    all_sprites.update()


    pygame.display.flip #perbarui tampilan permukaan ke layar

pygame.quit()
