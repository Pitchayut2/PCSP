import pygame
pygame.init()
#เซตหน้าจอ
SCREEN_WIDTH = 800
SCREEN_HIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
#ชื่อเกม
pygame.display.set_caption("Testwalk")
#LOGO Game
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)
#พื้นหลัง
bg = pygame.image.load("mapbg.png")
#ตัวละคร
load_player = pygame.image.load("char.png")
#ขนาดตัวละคร
load_player = pygame.transform.scale(load_player, (60, 60))
#ค่าต่างๆของตัวละคร
load_player_rect = load_player.get_rect()
#เซตให้ตัวละครอยู่กลางจอ
load_player_rect.centerx = SCREEN_WIDTH // 2
load_player_rect.centery = SCREEN_HIGHT // 2
#ค่าการเคลื่อนที่ตัวละคร
MOVE = 3
#FPS SETTING
FPS = 30
clock = pygame.time.Clock()

run = True
while run:
    pygame.time.delay(12)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and load_player_rect.left > 0:
        load_player_rect.x -= MOVE
    if keys[pygame.K_d] and load_player_rect.right < SCREEN_WIDTH:
        load_player_rect.x += MOVE 
    if keys[pygame.K_w] and load_player_rect.top > 0:
        load_player_rect.y -= MOVE
    if keys[pygame.K_s] and load_player_rect.bottom < SCREEN_HIGHT:
        load_player_rect += MOVE
    move = 3
    screen.blit(bg,(0, 0))
    screen.blit(load_player, (load_player_rect.centerx, load_player_rect.centery))
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()