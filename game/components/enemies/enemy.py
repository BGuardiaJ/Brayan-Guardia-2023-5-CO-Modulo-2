import pygame
import random

from pygame.sprite import  Sprite
from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_3, SCREEN_HEIGHT, SCREEN_WIDTH


class Enemy(Sprite):
    ENEMY_WIDTH = 40
    ENEMY_HEIGHT= 60
    ENEMY_WIDTH_E3 = 80
    ENEMY_HEIGHT_E3 = 100
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
    Y_POS = 20
    SPEED_X_E1 = 3
    SPEED_Y_E1 = 3
    MOV_X = {0: 'left', 1: 'right'}
    ENEMIES = [ENEMY_1, ENEMY_2, ENEMY_3]
    
    def __init__(self):
        self.choose_enemies = random.choice(self.ENEMIES)
        self.image = pygame.transform.scale(self.choose_enemies, (self.ENEMY_WIDTH, self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS_LIST[random.randint(0, 10)]
        self.rect.y = self.Y_POS
        self.movement_x = self.MOV_X[random.randint(0, 1)]
        self.move_x_for = random.randint(30, 100)
        self.index = 0
        
        if self.choose_enemies == ENEMY_1:
            self.speed_x = self.SPEED_X_E1
            self.speed_y = self.SPEED_Y_E1
            self.choose_enemies = random.choice(self.ENEMIES)
            
        elif self.choose_enemies == ENEMY_2:   
            self.speed_x = random.randint(3, 8)
            self.speed_y = random.randint(3, 8)
            self.choose_enemies = random.choice(self.ENEMIES)
        
        elif self.choose_enemies == ENEMY_3:
            self.image = pygame.transform.scale(self.choose_enemies,(self.ENEMY_WIDTH_E3, self.ENEMY_HEIGHT_E3))    
            self.speed_x = random.randint(2, 5)
            self.speed_y = random.randint(2, 2)
            self.choose_enemies = random.choice(self.ENEMIES)
        
        
    def update(self, ships):
        self.rect.y += self.speed_y
        
        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
            self.change_movement_x()
        else:
            self.rect.x += self.speed_x
            self.change_movement_x()
        
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)
            
      
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x , self.rect.y))
        #if self.choose_enemies == ENEMY_1 or self.choose_enemies == ENEMY_2:
        #    screen.blit(self.image, (self.rect.x , self.rect.y))
             
             
        #elif self.choose_enemies == ENEMY_3:
        #    screen.blit(self.image, (self.rect.x , self.rect.y))
        #    screen.blit(self.image, (self.rect.x+200 , self.rect.y-100))
        #    screen.blit(self.image, (self.rect.x+400 , self.rect.y-100))
             
     
    def change_movement_x(self):
      self.index += 1
      if   (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.ENEMY_WIDTH):
          self.movement_x = 'left'
          self.index = 0
      elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10) :
          self.movement_x = 'right'
          self.index = 0
          
          
    
