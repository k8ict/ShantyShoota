import pygame
from sys import exit
from random import randrange
import random

#initialize window
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((680,680))
pygame.display.set_caption('Shanty Shootah')
font = pygame.font.Font('font/Pixeltype.ttf', 50)

#ASSETS
sea_surface = pygame.image.load('assets/sea_bg.png').convert()
text_surface = font.render('Score: ', False, 'Black')

#fort
fort_surface = pygame.image.load('assets/fort.png').convert_alpha()
fort_rect = fort_surface.get_rect(center = (340,340))

#ship assets
ship_left_surface = pygame.image.load('assets/ship_left.png').convert_alpha()
ship_top_surface = pygame.image.load('assets/ship_top.png').convert_alpha()
ship_right_surface = pygame.image.load('assets/ship_right.png').convert_alpha()
ship_bot_surface = pygame.image.load('assets/ship_bot.png').convert_alpha()

#ship rects
ship_left_rect = ship_left_surface.get_rect(center = (0,340))
ship_top_rect = ship_top_surface.get_rect(center = (340,0))
ship_right_rect = ship_right_surface.get_rect(center = (680,340))
ship_bot_rect = ship_bot_surface.get_rect(center = (340,680))

#ship speeds global
ship_left_speed = 0
ship_top_speed = 0
ship_right_speed = 0
ship_bot_speed = 0

#handles player shooting
#def player_shooting():
    #fdadngadg

#spawns random ships
def ship_spawning():
    ship_sp = random.randint(0,1,2,3)
    if ship_sp == 0:
        ship_left_speed = random.randint(1,2)
    if ship_sp == 1:
        ship_top_speed = random.randint(1,2)
    if ship_sp == 2:
        ship_right_speed = random.randint(1,2)
    if ship_sp == 3:
        ship_bot_speed = random.randint(1,2)


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

    pygame.mixer.music.get_pos()
    screen.blit(sea_surface,(0,0))
    screen.blit(fort_surface,fort_rect)

    screen.blit(ship_left_surface,ship_left_rect)
    screen.blit(ship_top_surface,ship_top_rect)
    screen.blit(ship_right_surface,ship_right_rect)
    screen.blit(ship_bot_surface,ship_bot_rect)

    #ship movement
    ship_left_rect.x += ship_left_speed
    ship_top_rect.y += ship_top_speed
    ship_right_rect.x -= ship_right_speed
    ship_bot_rect.y -= ship_bot_speed
    #if ship_rect.colliderect(bullet_rect):
    #    print('collision')

    #update
    pygame.display.update()
    clock.tick(60)
    