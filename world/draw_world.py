import pygame
def draw_World(screen, world, cell_size, images_loaded):
    
    layer = 0
    
    while layer <= 5:
        
        for row_index, row in enumerate(world):
            for col_index, col in enumerate(row):
                x = col_index*cell_size
                y = row_index*cell_size
                
                if col != layer:
                    continue
                
                if col == 1:
                    screen.blit(images_loaded[col], (x+10,y+10))
                else:
                    if col == 3:
                        screen.blit(images_loaded[col], (x+10,y+10))
                    else: 
                        if col == 4:
                            screen.blit(images_loaded[col], (x+10,y+10))
                        if col == 5:
                            screen.blit(images_loaded[col], (x,y))
                        else:
                            screen.blit(images_loaded[col], (x,y))
        
        layer+=1