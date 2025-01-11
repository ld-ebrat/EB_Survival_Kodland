import pygame
from constants.image_path import image_enmies

class SlimePurple:
    
    def __init__(self):
        self.image_loaded = {}
        self.health = 100
        self.atack = 3
        
        for image_type, image in image_enmies.items():
            if image_type == 8:
                sheet_image_enemies = pygame.image.load(image["path"]).convert_alpha()
                surface = pygame.Surface((32,32), pygame.SRCALPHA)
                surface.blit(sheet_image_enemies, (0,0), (0,0,32,32))
                self.image_loaded[image_type] = pygame.transform.scale(surface, (image["size"], image["size"]))
     
    
    def draw(self, screen, world):
        for row_index, row in enumerate(world):
            for col_index, col in enumerate(row):
                if col in [8]:
                    x = col_index * 36
                    y = row_index * 36
                    screen.blit(self.image_loaded[col], (x,y))
                    

class SlimeGreen:
    
    def __init__(self):
        self.image_loaded = {}
        self.health = 150
        self.atack = 2
        
        for image_type, image in image_enmies.items():
            if image_type == 7:
                sheet_image_enemies = pygame.image.load(image["path"]).convert_alpha()
                surface = pygame.Surface((64,64), pygame.SRCALPHA)
                surface.blit(sheet_image_enemies, (0,0), (0,0,64,64))
                self.image_loaded[image_type] = pygame.transform.scale(surface, (image["size"], image["size"]))
     
    
    def draw(self, screen, world):
        for row_index, row in enumerate(world):
            for col_index, col in enumerate(row):
                if col in [7]:
                    x = col_index * 36
                    y = row_index * 36
                    screen.blit(self.image_loaded[col], (x,y))
                    
                    

class Skeleton:
    
    def __init__(self):
        self.image_loaded = {}
        self.health = 200
        self.atack = 5
        
        for image_type, image in image_enmies.items():
            if image_type == 6:
                sheet_image_enemies = pygame.image.load(image["path"]).convert_alpha()
                surface = pygame.Surface((32,32), pygame.SRCALPHA)
                surface.blit(sheet_image_enemies, (0,0), (0,0,32,32))
                self.image_loaded[image_type] = pygame.transform.scale(surface, (image["size"], image["size"]))
     
    
    def draw(self, screen, world):
        for i in range(1,5):
            print(i, "multiplico por 8 =", i*8)
        for row_index, row in enumerate(world):
            for col_index, col in enumerate(row):
                if col in [6]:
                    x = col_index * 36
                    y = row_index * 36
                    screen.blit(self.image_loaded[col], (x,y))
    
    def draw_health(self,screen):
        health_ratio = self.health/100
        pygame.draw.rect(screen, (255, 0, 0))