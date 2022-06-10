import pygame
from sys import exit

#initialize window
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((680,680))
pygame.display.set_caption('Shanty Shootah')
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My Game', False, 'Black')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft = (600,300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))

while True:

    #handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(50,50))

    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surface,snail_rect)
    screen.blit(player_surface,player_rect)

    if player_rect.colliderect(snail_rect):
        print('collision')

    
    #update
    pygame.display.update()
    clock.tick(60)