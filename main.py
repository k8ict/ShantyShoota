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
ship_left_rect = ship_left_surface.get_rect(center = (-16,340))
ship_top_rect = ship_top_surface.get_rect(center = (340,-16))
ship_right_rect = ship_right_surface.get_rect(center = (696,340))
ship_bot_rect = ship_bot_surface.get_rect(center = (340,696))

#synchronisation frames for spawning ships
frame_counter = 0
#handles player shooting
#def player_shooting():
    #fdadngadg

ship_left_speed = 0
ship_top_speed = 0
ship_right_speed = 0
ship_bot_speed = 0

ship_left_spawned = False
ship_top_spawned = False
ship_right_spawned = False
ship_bot_spawned = False

#spawns random ships
def ship_spawning():
    global ship_left_speed, ship_top_speed, ship_right_speed, ship_bot_speed
    global ship_left_spawned, ship_top_spawned, ship_right_spawned, ship_bot_spawned

    ship_sp = random.randint(0,3)
    if ship_sp == 0:
        if ship_left_spawned == False:
            ship_left_speed += random.randint(2,4)
            ship_left_spawned = True
    if ship_sp == 1:
        if ship_top_spawned == False:
            ship_top_speed += random.randint(2,4)
            ship_top_spawned = True
    if ship_sp == 2:
        if ship_right_spawned == False:
            ship_right_speed += random.randint(2,4)
            ship_right_spawned = True
    if ship_sp == 3:
        if ship_bot_spawned == False:
            ship_bot_speed += random.randint(2,4)
            ship_bot_spawned = True

#shooting mechanics
def shooting(direction):
    global ship_left_rect, ship_top_rect, ship_right_rect, ship_bot_rect
    global ship_left_speed, ship_top_speed, ship_right_speed, ship_bot_speed
    global ship_left_spawned, ship_top_spawned, ship_right_spawned, ship_bot_spawned

    if direction == 0:
        ship_left_rect = ship_left_surface.get_rect(center = (-16,340))
        ship_left_speed = 0
        ship_left_spawned = False
    if direction == 1:
        ship_top_rect = ship_top_surface.get_rect(center = (340,-16))
        ship_top_speed = 0
        ship_top_spawned = False
    if direction == 2:
        ship_right_rect = ship_right_surface.get_rect(center = (696,340))
        ship_right_speed = 0
        ship_right_spawned = False
    if direction == 3:
        ship_bot_rect = ship_bot_surface.get_rect(center = (340,696))
        ship_bot_speed = 0
        ship_bot_spawned = False

#checks if the game just started
gamestarted_check = True
onbeat = False
#main gameloop
while True:

    #detects if the music is on beat
    frame_counter += 1
    if frame_counter % 30 == 0:
        onbeat = True
    
    #handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                 shooting(0)
            if event.key == pygame.K_UP: 
                shooting(1)
            if event.key == pygame.K_RIGHT: 
                shooting(2)
            if event.key == pygame.K_DOWN: 
                shooting(3)


    #music
    if gamestarted_check == True:
        pygame.mixer.music.load('music/music_menu.mp3')
        pygame.mixer.music.play(-1)
        gamestarted_check = False

    #spawns ships on beat
    if onbeat == True: 
        ship_spawning()
        frame_counter = 0

    screen.blit(sea_surface,(0,0))
    screen.blit(fort_surface,fort_rect)

    screen.blit(ship_left_surface,ship_left_rect)
    screen.blit(ship_top_surface,ship_top_rect)
    screen.blit(ship_right_surface,ship_right_rect)
    screen.blit(ship_bot_surface,ship_bot_rect)

    ship_left_rect.x += ship_left_speed
    ship_top_rect.y += ship_top_speed
    ship_right_rect.x -= ship_right_speed
    ship_bot_rect.y -= ship_bot_speed

    #if ship_rect.colliderect(fort_rect):
    #    print('collision')

    onbeat = False
    #update
    pygame.display.update()
    clock.tick(60)
    