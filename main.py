import pygame
from world.world import World
from player.player import Player
from key_press import movePlayer, inventoryKey, collindableEnemies
from enemies.enemies import Skeleton, SlimeGreen, SlimePurple
from player.inventory import HotBar, Inventory
pygame.init()

screen = pygame.display.set_mode((680, 680))
pygame.display.set_caption("Juego")

pygame.font.init()

def main():
    
    clock = pygame.time.Clock()
    running = True
    world = World(680,680)
    player = Player(360,400)
    skeleton = Skeleton()
    slimeGreen = SlimeGreen()
    slimePurple = SlimePurple()
    hotbar = HotBar(screen)
    inventory = Inventory(screen)
    while running:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for slime in slimeGreen.slimesGreen:
                        if slime["rect"].collidepoint(event.pos):
                            collindableEnemies(slime, player)
            inventoryKey(inventory, event)
                
        key = pygame.key.get_pressed()
        movePlayer(key,player, world.collindables)
        
        
        screen.fill("#3e8948")
        world.draw(screen)
        player.draw(screen)
        slimeGreen.draw(screen, world.world)
        slimePurple.draw(screen, world.world)
        skeleton.draw(screen, world.world)
        hotbar.draw()
        inventory.draw()
        
        
    
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    
if __name__ == "__main__":
    main()
