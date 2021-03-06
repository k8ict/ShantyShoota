import pygame
from sys import exit
from random import randrange
import random
import numpy

#initialize window
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((680,680))
pygame.display.set_caption('Shanty Shootah')
font = pygame.font.Font('font/Pixeltype.ttf', 40)

#ASSETS
#menu assets
menu_bg = pygame.image.load('assets/menu_bg.png').convert()
loss_bg = pygame.image.load('assets/loss_bg.png').convert()
bt_start = pygame.image.load('assets/bt_start.png').convert()
bt_quit = pygame.image.load('assets/bt_quit.png').convert()
bt_retry = pygame.image.load('assets/bt_retry.png').convert()

#icon
game_icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(game_icon)

#game background
sea_surface = pygame.image.load('assets/sea_bg.png').convert()

#fort asset
fort_surface = pygame.image.load('assets/fort.png').convert_alpha()

#ship assets
ship_left_surface = pygame.image.load('assets/ship_left.png').convert_alpha()
ship_top_surface = pygame.image.load('assets/ship_top.png').convert_alpha()
ship_right_surface = pygame.image.load('assets/ship_right.png').convert_alpha()
ship_bot_surface = pygame.image.load('assets/ship_bot.png').convert_alpha()

#sfx
snd_explode = pygame.mixer.Sound('sfx/explosion.mp3')
snd_death = pygame.mixer.Sound('sfx/death.mp3')
snd_miss = pygame.mixer.Sound('sfx/miss.mp3')

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

#synchronisation variables
gamestarted_check = True
onbeat = False
wiggle = True

#spawns random ships
def ship_spawning():
    global ship_left_speed, ship_top_speed, ship_right_speed, ship_bot_speed
    global ship_left_spawned, ship_top_spawned, ship_right_spawned, ship_bot_spawned

    ship_sp = random.randint(0,3)
    if ship_sp == 0:
        if ship_left_spawned == False:
            ship_left_speed += random.randint(3,5)
            ship_left_spawned = True
    if ship_sp == 1:
        if ship_top_spawned == False:
            ship_top_speed += random.randint(3,5)
            ship_top_spawned = True
    if ship_sp == 2:
        if ship_right_spawned == False:
            ship_right_speed += random.randint(3,5)
            ship_right_spawned = True
    if ship_sp == 3:
        if ship_bot_spawned == False:
            ship_bot_speed += random.randint(3,5)
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
            ships_destroyed += 1
            snd_explode.play()
            ship_left_spawned = False
        else:
            snd_miss.play()
    if direction == 1:
        if ship_top_spawned == True:
            ship_top_rect = ship_top_surface.get_rect(center = (340,-32))
            ship_top_speed = 0
            ships_destroyed += 1
            snd_explode.play()
            ship_top_spawned = False
        else:
            snd_miss.play()            
    if direction == 2:
        if ship_right_spawned == True:
            ship_right_rect = ship_right_surface.get_rect(center = (712,340))
            ship_right_speed = 0
            ships_destroyed += 1
            snd_explode.play()
            ship_right_spawned = False
        else:
            snd_miss.play()            
    if direction == 3:
        if ship_bot_spawned == True:
            ship_bot_rect = ship_bot_surface.get_rect(center = (340,712))
            ship_bot_speed = 0
            ships_destroyed += 1
            snd_explode.play()
            ship_bot_spawned = False
        else:
            snd_miss.play()

#collision mechanics
def collision():
    if ((ship_left_rect.colliderect(fort_rect) or ship_top_rect.colliderect(fort_rect)) or (ship_right_rect.colliderect(fort_rect) or ship_bot_rect.colliderect(fort_rect))):
        loss_screen()

#loss screen
def loss_screen():
    
    snd_death.play()
    
    #menu click
    click = False

    #stop music
    pygame.mixer.music.stop()

    #menu buttons rects
    bt_retry_rect = bt_retry.get_rect(midleft = (100,500))
    bt_quit_rect = bt_quit.get_rect(midleft = (380,500))
    score_surface = font.render('Score: '+ str(ships_destroyed), False, 'White')
    score_rect = score_surface.get_rect(center = (340,300))

    while True:
        screen.blit(loss_bg, (0,0))
        screen.blit(bt_retry,bt_retry_rect)
        screen.blit(bt_quit,bt_quit_rect)
        screen.blit(score_surface,score_rect)

        mx, my = pygame.mouse.get_pos()

        if bt_retry_rect.collidepoint((mx, my)):
            if click:
                click = False
                game()
        if bt_quit_rect.collidepoint((mx, my)):
                if click:
                    click = False
                    pygame.quit()
                    exit()

        #inputs
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    main_menu()
        pygame.display.update()
        clock.tick(60)

#main menu
def main_menu():

    #menu click
    click = False

    #stop music if returning to menu from game
    pygame.mixer.music.stop()

    #menu buttons rects
    bt_start_rect = bt_start.get_rect(midleft = (100,400))
    bt_quit_rect = bt_quit.get_rect(midleft = (380,400))

    #start menu music
    menu_loop = pygame.mixer.music.load('music/music_menu.mp3')
    pygame.mixer.music.play(-1)

    while True:
        screen.blit(menu_bg, (0,0))
        screen.blit(bt_start,bt_start_rect)
        screen.blit(bt_quit,bt_quit_rect)

        mx, my = pygame.mouse.get_pos()

        if bt_start_rect.collidepoint((mx, my)):
            if click:
                click = False
                game()
        if bt_quit_rect.collidepoint((mx, my)):
                if click:
                    click = False
                    pygame.quit()
                    exit()

        #inputs
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(60)

#gameloop
def game():
    #ship variables
    global ship_left_speed, ship_top_speed, ship_right_speed, ship_bot_speed
    global ship_left_spawned, ship_top_spawned, ship_right_spawned, ship_bot_spawned
    global ship_left_rect, ship_top_rect, ship_right_rect, ship_bot_rect
    global fort_rect

    #sync variables
    global frame_counter, bullet_count, ships_destroyed, gamestarted_check, onbeat, wiggle

    #music start
    pygame.mixer.music.stop()
    music_loop = pygame.mixer.music.load('music/music_loop.mp3')
    pygame.mixer.music.play(-1)

    #set initial ship and fort position position
    fort_rect = fort_surface.get_rect(center = (340,340))
    ship_left_rect = ship_left_surface.get_rect(center = (-32,342))
    ship_top_rect = ship_top_surface.get_rect(center = (338,-32))
    ship_right_rect = ship_right_surface.get_rect(center = (712,338))
    ship_bot_rect = ship_bot_surface.get_rect(center = (342,712))

    #ship speed reset
    ship_left_spawned = False
    ship_top_spawned = False
    ship_right_spawned = False
    ship_bot_spawned = False
    ship_left_speed = 0
    ship_top_speed = 0
    ship_right_speed = 0
    ship_bot_speed = 0
    
    #set score to 0 every time the game is restarted
    ships_destroyed = 0

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
                if event.key == pygame.K_ESCAPE:
                    main_menu()

        #spawns ships and adds a bullet on beat
        if onbeat == True:
            if bullet_count < 1:
                bullet_count = 1 

            ship_spawning()

            if wiggle == True:
                ship_left_rect.y += 4
                ship_top_rect.x += 4
                ship_right_rect.y -= 4
                ship_bot_rect.x -= 4
                wiggle = False

            else:
                ship_left_rect.y -= 4
                ship_top_rect.x -= 4
                ship_right_rect.y += 4
                ship_bot_rect.x += 4
                wiggle = True

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

        collision()

        #text surfaces for stats
        ships_txt_surface = font.render('Ships destroyed: ' + str(ships_destroyed), False, 'White')
        screen.blit(ships_txt_surface, (20,20))

        onbeat = False

        #update
        pygame.display.update()
        clock.tick(60)
    
main_menu()