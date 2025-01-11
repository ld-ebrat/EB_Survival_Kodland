import pygame

def movePlayer(key,player, collindble):
    if key[pygame.K_RIGHT]:
        collindablePlayer(3,0,collindble, player)
    if key[pygame.K_LEFT]:
        collindablePlayer(-3,0,collindble, player)
    if key[pygame.K_UP]:
        collindablePlayer(0,-3,collindble, player)
    if key[pygame.K_DOWN]:
        collindablePlayer(0,3,collindble, player)
    

def collindablePlayer(dx,dy, collindable, player):
    
    temp_rect = player.rect.move(dx, dy)
    for rectt in collindable:
        if temp_rect.colliderect(rectt):
            return
    
    player.move(dx,dy)

def collindableEnemies(collindable, player):
    
    if player.rect.colliderect(collindable["rect"]):
        player.Atack(collindable)
    else:
        print("Aun estoy lejos")
    

def inventoryKey(inventory,key):
    if key.type == pygame.KEYDOWN:
        if key.key == pygame.K_i:
            inventory.visibityInventory = not inventory.visibityInventory

        
    
    