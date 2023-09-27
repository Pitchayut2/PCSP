import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("TEST")
icon = pygame.image.load("testlearn/logo.png")
pygame.display.set_icon(icon)
bg = pygame.image.load("testlearn/mapbg.png")
load_player = pygame.image.load("testlearn/char.png")
player = pygame.transform.scale(load_player, (85, 120))
x = 250
y = 350
move = 5
run = True

while run:
    pygame.time.delay(12)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= move
    if keys[pygame.K_RIGHT] and x < 800-85:
        x += move
    if keys[pygame.K_UP] and y > 0:
        y -= move
    if keys[pygame.K_DOWN] and y < 600-85:
        y += move
    screen.blit(bg,(0,0))
    screen.blit(player, (x,y))
    pygame.display.update()

pygame.quit()