import os
import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RAGE_BAR
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.obstacles.obstacle import Obstacle

class Rage(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.IMAGEM_RAGE = []
        for i in range(5):
            img = RAGE_BAR.subsurface((i * 32, 0), (32,32))
            img = pygame.transform.scale(img, (32*20, 32*7))
            self.IMAGEM_RAGE.append(img)
        self.index_lista = 0
        self.image = self.IMAGEM_RAGE[self.index_lista]
        self.rect = self.image.get_rect()
        self.start_time = 0
        self.duration = 6
    
    def update(self, score):
        user_input = pygame.key.get_pressed()
        if score %100 == 0:
            self.index_lista += 1
        if self.index_lista >= 4:
            self.index_lista = 4
        if self.index_lista >= 4 and user_input[pygame.K_f]:   
            self.index_lista = 0
        if score == 1:
            self.index_lista = 0
        self.image = self.IMAGEM_RAGE[int(self.index_lista)]

    
    def draw(self, screen):
        screen.blit(self.image, (180, 450))
