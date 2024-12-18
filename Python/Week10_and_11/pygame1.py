import pygame, sys
from pygame.locals import *
import time
import random

pygame.init()

FPS = 60
FramesPerSec = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Pygame 1")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pygame1_player.png")
        self.surf = pygame.Surface((50,50))
        self.rect = self.surf.get_rect(center = (250, 450))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)        

class Win(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pygame1_win.png")
        self.surf = pygame.Surface((50,50))
        self.rect = self.surf.get_rect(center = (100, 50))

    def move(self):
        self.rect.move_ip(5,0)
        if (self.rect.left > 450):
            self.rect.left = 0


class Lose(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pygame1_lose.png")
        self.surf = pygame.Surface((50,50))
        self.rect = self.surf.get_rect(center = (400, 150))

    def move(self):
        self.rect.move_ip(-5,0)
        if (self.rect.left <= 0):
            self.rect.left = 500


P1 = Player()
win = Win()
lose = Lose()

win_group = pygame.sprite.Group()
win_group.add(win)

lose_group = pygame.sprite.Group()
lose_group.add(lose)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(win)
all_sprites.add(lose)

while True:

    for event in pygame.event.get():  
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    DISPLAYSURF.fill(WHITE)

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    DISPLAYSURF.blit(P1.image, P1.rect)
    P1.move()
    

    if pygame.sprite.spritecollideany(P1, win_group):
        DISPLAYSURF.fill(GREEN)
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    if pygame.sprite.spritecollideany(P1, lose_group):
        DISPLAYSURF.fill(RED)
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    

    pygame.display.update()
    FramesPerSec.tick(FPS)

