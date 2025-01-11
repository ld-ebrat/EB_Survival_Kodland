import pygame
from constants.image_path import image_path_nature, image_house

from .draw_world import draw_World

world1 = [
    [2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,3,0,2,3,2,1,2,2,2,2,2,2,0,0,0,2,2,2],
    [2,2,0,2,2,2,2,1,1,0,0,0,0,0,7,0,0,6,0,2],
    [2,0,2,8,2,2,2,2,1,1,2,2,2,2,2,2,0,0,0,2],
    [2,2,2,2,2,2,3,2,2,1,1,2,2,2,2,2,2,0,0,2],
    [2,0,2,2,3,2,2,2,2,2,1,2,2,2,2,2,2,6,2,2],
    [2,2,0,2,2,2,2,2,1,1,1,1,1,2,2,4,2,2,2,2],
    [2,2,0,2,2,2,2,1,1,0,0,0,1,1,2,4,2,2,3,2],
    [2,2,2,2,0,2,2,1,0,5,0,0,0,1,2,2,3,2,4,2],
    [2,2,2,2,2,1,1,1,0,0,0,0,0,1,1,1,1,2,2,1],
    [2,2,2,2,2,1,2,1,0,0,0,0,0,1,2,2,1,1,1,1],
    [2,2,2,1,1,1,2,1,1,0,0,0,1,1,2,2,2,2,2,2],
    [2,1,1,1,2,2,2,2,1,1,1,1,1,0,0,2,2,2,2,2],
    [1,1,2,0,2,2,0,2,2,2,1,2,2,2,0,2,2,0,2,2],
    [1,2,2,0,0,0,2,3,2,1,1,2,3,2,0,2,2,2,2,2],
    [2,2,2,0,7,0,2,2,2,1,2,2,2,2,0,0,0,2,2,0],
    [2,2,0,2,0,6,2,2,2,1,1,2,2,2,0,0,6,0,2,2],
    [2,2,0,2,2,2,2,2,2,2,1,1,2,2,6,3,0,8,2,2],
    [2,2,2,2,3,2,2,2,3,2,2,1,1,2,2,2,2,2,2,2],
    [2,2,2,0,0,0,2,2,2,2,2,2,1,2,2,2,2,2,3,2],
]

cell_size = 34
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.images_loaded = {}
        self.collindables = []
        self.collindablesEnmies = []
        self.world = world1
        
        for image_type, image in image_path_nature.items():
            if image_type == 3:
                sheet_image_rock = pygame.image.load(image["path"]).convert_alpha()
                surface = pygame.Surface((16,16), pygame.SRCALPHA)
                surface.blit(sheet_image_rock, (0,0),(2*16,2*16,16,16))
                self.images_loaded[image_type] = pygame.transform.scale(surface, (image["size"],image["size"]))
            else:
                self.image_loaded = pygame.image.load(image["path"]).convert_alpha()
                self.images_loaded[image_type] = pygame.transform.scale(self.image_loaded, (image["size"],image["size"]))
        
        self.house = pygame.image.load(image_house["path"]).convert_alpha()
        self.images_loaded[5] = pygame.transform.scale(self.house, (image_house["size"],image_house["size"]))
        self.load_collindable()
            
        
    def load_collindable(self):
        for row_index, row in enumerate(world1):
            for col_index, col in enumerate(row):
                x = col_index*cell_size
                y = row_index*cell_size
                if col in [2, 3, 5]:
                    if col in [5]:
                        rect = pygame.Rect(x, y, image_house["size"], image_house["size"]) 
                        self.collindables.append(rect)
                    else:
                        rect = pygame.Rect(x, y, cell_size, cell_size) 
                        self.collindables.append(rect)
 
    def draw(self,screen):
        draw_World(screen, world1, cell_size, self.images_loaded)
        
    
        
        