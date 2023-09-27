import pygame
import random
pygame.init()

#ชื่อเกม
pygame.display.set_caption("ProjectbeginTest")
#LOGO Game
icon = pygame.image.load("testlearn/logo.png")
pygame.display.set_icon(icon)
#Set ขนาดหน้าจอ
SCREEN_W = 800
SCREEN_H = 600
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
#Set พื้นหลัง
bg = pygame.image.load("testlearn/mapbg.png")
#player setting (Object)
player = pygame.image.load("testlearn/char.png")
player = pygame.transform.scale(player, (50, 50))
#ค่าพื้นฐาน Player
player_rect = player.get_rect()
player_rect.centerx = SCREEN_W // 2
player_rect.centery = SCREEN_H // 2

#BOSS
boss = pygame.image.load("testlearn/boss.png")
boss = pygame.transform.scale(boss, (225, 225))
#ค่าพื้นฐานBoss
boss_rect = boss.get_rect()
boss_rect.centerx = SCREEN_W // 2
boss_rect.centery = 100
#Damage Object
damage = pygame.image.load("testlearn/metreo.png")
damage = pygame.transform.scale(damage, (75, 150))
#ค่าพื้นฐาน Object Damage
damage_rect = damage.get_rect()
damage_rect.x = random.randint(0, SCREEN_W - 32)
damage_rect.y = 0
#Damage Object2
damage2 = pygame.image.load("testlearn/metreo.png")
damage2 = pygame.transform.scale(damage2, (75, 150))
#ค่าพื้นฐาน Object damage2
damage2_rect = damage2.get_rect()
damage2_rect.x = random.randint(0, SCREEN_W - 32)
damage2_rect.y = 0
#MOVEMENT
MOVE = 5
#MOVEMENT METREO FALL
FALL1 = random.randint(7, 12)
FALL2 = random.randint(7, 12)
#Font Game
RED = (255, 0, 0)
font = pygame.font.Font("Font/Coiny.ttf", 30)
#HP System
HP = 100
hp_text = font.render("HP : %i"%HP, True, RED)
hp_rect = hp_text.get_rect()
hp_rect.topleft = (10, 10)
#FPS SETTING
FPS = 30
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if HP == 0:
        running = False
    #ตรวจจับการชนของObject (Player, damage1, damage2)
    if player_rect.colliderect(damage_rect) or player_rect.colliderect(damage2_rect):
        HP -= 20
        hp_text = font.render("HP : %i"%HP, True, RED)
        if player_rect.colliderect(damage_rect) == True:
            damage_rect.x = random.randint(0, SCREEN_W - 32)
            damage_rect.y = 0
        if player_rect.colliderect(damage2_rect) == True:
            damage2_rect.x = random.randint(0, SCREEN_W - 32)
            damage2_rect.y = 0
    #Movement Control
    keys = pygame.key.get_pressed()
    move_list = []
    move_list.append(keys[pygame.K_w])
    move_list.append(keys[pygame.K_s])
    move_list.append(keys[pygame.K_a])
    move_list.append(keys[pygame.K_d])
    if move_list.count(True) >= 2:
        MOVE = 3.5
    else:
        MOVE = 5
    if keys[pygame.K_w] and player_rect.top > 0:
        player_rect.y -= MOVE
    if keys[pygame.K_s] and player_rect.bottom < SCREEN_H:
        player_rect.y += MOVE
    if keys[pygame.K_a] and player_rect.left > 0:
        player_rect.x -= MOVE
    if keys[pygame.K_d] and player_rect.right < SCREEN_W:
        player_rect.x += MOVE
        
    #Ball Object
    if damage_rect.y < SCREEN_H:
        damage_rect.y += FALL1
    else:
        damage_rect.x = random.randint(0, SCREEN_W-32)
        damage_rect.y = 0
    #Ball Object2
    if damage2_rect.y < SCREEN_H:
        damage2_rect.y += FALL2
    else:
        damage2_rect.x = random.randint(0, SCREEN_W-32)
        damage2_rect.y = 0
    
    screen.blit(bg,(0, 0))
    screen.blit(boss, boss_rect)
    screen.blit(player, player_rect)
    screen.blit(damage, damage_rect)
    screen.blit(damage2, damage2_rect)
    screen.blit(hp_text, hp_rect)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
