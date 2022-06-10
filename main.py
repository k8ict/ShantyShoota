import pygame
from sys import exit
from random import randrange
import random

#initialize window
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((680,680))
pygame.display.set_caption('Shanty Shootah')
font = pygame.font.Font('font/Pixeltype.ttf', 40)

#ASSETS
sea_surface = pygame.image.load('assets/sea_bg.png').convert()

#fort
fort_surface = pygame.image.load('assets/fort.png').convert_alpha()
fort_rect = fort_surface.get_rect(center = (340,340))

#ship assets
ship_left_surface = pygame.image.load('assets/ship_left.png').convert_alpha()
ship_top_surface = pygame.image.load('assets/ship_top.png').convert_alpha()
ship_right_surface = pygame.image.load('assets/ship_right.png').convert_alpha()
ship_bot_surface = pygame.image.load('assets/ship_bot.png').convert_alpha()

#ship rects
ship_left_rect = ship_left_surface.get_rect(center = (-32,340))
ship_top_rect = ship_top_surface.get_rect(center = (340,-32))
ship_right_rect = ship_right_surface.get_rect(center = (712,340))
ship_bot_rect = ship_bot_surface.get_rect(center = (340,712))


#sfx
snd_explode = pygame.mixer.Sound('sfx/explosion.mp3')
snd_death = pygame.mixer.Sound('sfx/death.mp3')
music_loop = pygame.mixer.music.load('music/music_loop.mp3')

#synchronisation data for spawning ships
frame_counter = 0

ship_left_speed = 0
ship_top_speed = 0
ship_right_speed = 0
ship_bot_speed = 0

ship_left_spawned = False
ship_top_spawned = False
ship_right_spawned = False
ship_bot_spawned = False

#bullets and stats
bullet_count = 1
ships_destroyed = 0

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
    global bullet_count, ships_destroyed
    bullet_count -= 1
    if direction == 0:
        if ship_left_spawned == True:
            ship_left_rect = ship_left_surface.get_rect(center = (-32,340))
            ship_left_speed = 0
            snd_explode.play()
            ship_left_spawned = False
    if direction == 1:
        if ship_top_spawned == True:
            ship_top_rect = ship_top_surface.get_rect(center = (340,-32))
            ship_top_speed = 0
            snd_explode.play()
            ship_top_spawned = False
    if direction == 2:
        if ship_right_spawned == True:
            ship_right_rect = ship_right_surface.get_rect(center = (712,340))
            ship_right_speed = 0
            snd_explode.play()
            ship_right_spawned = False
    if direction == 3:
        if ship_bot_spawned == True:
            ship_bot_rect = ship_bot_surface.get_rect(center = (340,712))
            ship_bot_speed = 0
            snd_explode.play()
            ship_bot_spawned = False

#synchronisation variables
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
            if bullet_count >= 1:
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
        pygame.mixer.music.play(-1)
        gamestarted_check = False

    #spawns ships and adds a bullet on beat
    
    if onbeat == True:
        if bullet_count < 1:
            bullet_count = 1 
        ship_spawning()
        frame_counter = 0

    #background drawing
    screen.blit(sea_surface,(0,0))
    screen.blit(fort_surface,fort_rect)

    #ships drawing
    screen.blit(ship_left_surface,ship_left_rect)
    screen.blit(ship_top_surface,ship_top_rect)
    screen.blit(ship_right_surface,ship_right_rect)
    screen.blit(ship_bot_surface,ship_bot_rect)
    
    #ship movement
    ship_left_rect.x += ship_left_speed
    ship_top_rect.y += ship_top_speed
    ship_right_rect.x -= ship_right_speed
    ship_bot_rect.y -= ship_bot_speed

    #text surfaces for bullets and stats
    if bullet_count == 1:
        bullet_txt_surface = font.render('Ready to fire!', False, 'White')
    else:
        bullet_txt_surface = font.render('No more ammo', False, 'White')
    ships_txt_surface = font.render('Ships destroyed: ' + str(ships_destroyed), False, 'White')
    screen.blit(bullet_txt_surface, (20,20))
    screen.blit(ships_txt_surface, (20,60))
    #if ship_rect.colliderect(fort_rect):
    #    print('collision')
    print(bullet_count)
    onbeat = False
    #update
    pygame.display.update()
    clock.tick(60)
    