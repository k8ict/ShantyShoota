import pygame
from sys import exit

#initialize window
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((680,680))
pygame.display.set_caption('Shanty Shootah')
font = pygame.font.Font('font/Pixeltype.ttf', 50)

#assets
sea_surface = pygame.image.load('assets/sea_bg.png').convert()
text_surface = font.render('Score: ', False, 'Black')

fort_surface = pygame.image.load('assets/fort.png').convert_alpha()
fort_rect = fort_surface.get_rect(center = (340,340))

#checks if the game just started
gamestarted_check = True

#main gameloop
while True:
    
    #handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #music
    if gamestarted_check == True:
        pygame.mixer.music.load('music/music_loop.mp3')
        pygame.mixer.music.play(-1)
        gamestarted_check = False
    print(pygame.mixer.music.get_pos())
    screen.blit(sea_surface,(0,0))
    screen.blit(fort_surface,fort_rect)
    #if ship_rect.colliderect(bullet_rect):
    #    print('collision')

    
    #update
    pygame.display.update()
    clock.tick(60)