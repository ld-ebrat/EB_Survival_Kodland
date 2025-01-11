import pygame
from constants.image_path import image_path_player

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 500
        self.atack = 10
        
        self.size = image_path_player["size"]
        image_path = pygame.image.load(image_path_player["path"]).convert_alpha()
        surface = pygame.Surface((32,32), pygame.SRCALPHA)
        surface.blit(image_path, (0,0),(0*32,3*32,32,32))
        self.image_player = pygame.transform.scale(surface, (self.size, self.size))
        self.rect = self.image_player.get_rect(topleft=(x,y))
    
    def draw(self,screen):
        screen.blit(self.image_player, (self.x, self.y))
    
    def move(self,moveX, moveY):
        x = moveX
        y = moveY
        self.x += moveX
        self.y += moveY
        self.rect.topleft= (self.x,self.y)
        
    def Atack(self, enemy):
        enemy["health"] -= self.atack
        pass