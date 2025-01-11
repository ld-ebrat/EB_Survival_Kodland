import pygame
from constants.image_path import image_path_hotbar

class Inventory:
    def __init__(self, screen):
        self.screen = screen
        self.visibityInventory = False
        
        self.image = pygame.image.load(image_path_hotbar["path"]).convert_alpha()
        surface = pygame.Surface(((48,48)), pygame.SRCALPHA)
        surface.blit(self.image, (0,0), (48,48*2,48,48))
        
        self.image = pygame.transform.scale(surface, (48,48))
    
    def draw(self):
        
        if self.visibityInventory:
            backgound = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
            backgound.fill((0,0,0,128))
            self.screen.blit(backgound, (0,0))
        
            font = pygame.font.SysFont("Arial", 30)
            font_render = font.render("Inventory", True, (255,255,255))
            self.screen.blit(font_render, (self.screen.get_width()/2 - font_render.get_rect().width/2, 10))
            for i in range(5):
                for j in range(5):
                    hotbarY = (self.screen.get_height()/2 - (5*48)) + (j*48)
                    hotbarX = ((self.screen.get_width() - (5*48))/2) + (i*48)
                    self.screen.blit(self.image, (hotbarX,hotbarY))
                
                
                
                
        
    
    

class InventoryItem:
    def __init__(self):
        pass

class HotBar:
    def __init__(self, screen):
        self.screen = screen
        
        self.image = pygame.image.load(image_path_hotbar["path"]).convert_alpha()
        surface = pygame.Surface(((48,48)), pygame.SRCALPHA)
        surface.blit(self.image, (0,0), (48,48*2,48,48))
        
        self.image = pygame.transform.scale(surface, (48,48))
    
    def draw(self):
        
        for i in range(5):
            hotbarY = self.screen.get_height() - 48 - 5
            hotbarX = ((self.screen.get_width() - (5*48))/2) + (i*48)
            self.screen.blit(self.image, (hotbarX,hotbarY))