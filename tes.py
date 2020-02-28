import pygame
pygame.init()

layar = pygame.display.set_mode((750, 750))
pygame.display.set_caption('Game')

x = 50
y = 50
lebar = 30
panjang = 30
jalan = 4
lompat = False
lompatan = 5

run = True
while run:
    pygame.time.delay(20)

    for program in pygame.event.get():
        if program.type == pygame.QUIT:
            run = False
    arah = pygame.key.get_pressed()
    if arah[pygame.K_LEFT] and x > jalan:
        x -= jalan
    if arah[pygame.K_RIGHT] and x < 750 - lebar - jalan:
        x += jalan
    if not(lompat):
        if arah[pygame.K_UP] and y > jalan:
            y -= jalan
        if arah[pygame.K_DOWN] and y < 750 - panjang - jalan:
            y += jalan
        if arah[pygame.K_SPACE]:
            lompat = True
    else:
        if lompatan >= -10:
            neg = 1
            if lompatan < 0:
                neg = -1
            y -= (lompatan ** 2)* 0.3 * neg
            lompatan -= 1
        else:
            lompat = False
            lompatan = 10
            
    layar.fill((250,205,103))
    pygame.draw.rect(layar, (200, 100, 0), (x, y, lebar, panjang))
    pygame.display.update()
        

pygame.quit()
