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
                    x = col_index * 34
                    y = row_index * 34
                    screen.blit(self.image_loaded[col], (x,y))
                    self.draw_health(screen, x, y)
    
    def draw_health(self,screen, x, y):
        health_ratio = self.health/100
        rect_image = self.image_loaded[8].get_rect()
        with_image = rect_image.width
        height_image = rect_image.height
        
        pygame.draw.rect(screen, (255, 0, 0), (x, y -10, with_image, 5))
        pygame.draw.rect(screen, (0, 255, 0), (x, y -10, with_image*health_ratio, 5))
                    

class SlimeGreen:
    
    def __init__(self):
        self.image_loaded = {}
        self.health = 150
        self.atack = 2
        self.slimesGreen = []
        
        for image_type, image in image_enmies.items():
            if image_type == 7:
                sheet_image_enemies = pygame.image.load(image["path"]).convert_alpha()
                surface = pygame.Surface((64,64), pygame.SRCALPHA)
                surface.blit(sheet_image_enemies, (0,0), (0,0,64,64))
                self.image_loaded[image_type] = pygame.transform.scale(surface, (image["size"], image["size"]))
                self.rect = self.image_loaded[image_type].get_rect()
     
    
    def draw(self, screen, world):
        for row_index, row in enumerate(world):
            for col_index, col in enumerate(row):
                if col in [7]:
                    x = col_index * 34
                    y = row_index * 34
                    
                    slime = {
                        "rect": pygame.Rect(x,y, 36,36),
                        "health": 150
                    }
                    self.slimesGreen.append(slime)
                    self.rect.topleft = (x,y)
                    screen.blit(self.image_loaded[col], (x,y))
                    self.draw_health(screen, slime)
                    
    def draw_health(self,screen, slime):
        health_ratio = slime["health"]/150
        rect_image = self.image_loaded[7].get_rect()
        with_image = rect_image.width
        height_image = rect_image.height
        x, y = slime['rect'].topleft
        
        pygame.draw.rect(screen, (255, 0, 0), (x+15, y+3, 20, 5))
        pygame.draw.rect(screen, (0, 255, 0), (x+15, y+3, 20*health_ratio, 5))
                    
                    

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
        for row_index, row in enumerate(world):
            for col_index, col in enumerate(row):
                if col in [6]:
                    x = col_index * 34
                    y = row_index * 34
                    screen.blit(self.image_loaded[col], (x,y))
                    self.draw_health(screen, x, y)
    
    def draw_health(self,screen, x, y):
        health_ratio = self.health/100
        rect_image = self.image_loaded[6].get_rect()
        with_image = rect_image.width
        height_image = rect_image.height
        
        pygame.draw.rect(screen, (255, 0, 0), (x, y -10, 20, 5))
        pygame.draw.rect(screen, (0, 255, 0), (x, y -10, 20*health_ratio, 5))
        
    def take_damage(self, amout):
        self.health -= amout
        if self.health <0:
            self.health = 0