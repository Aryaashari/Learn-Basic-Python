import pygame
pygame.init()

ukuran = pygame.display.set_mode((500, 500))
pygame.display.set_caption('arya')

x = 50
y = 50
lebar = 60
panjang = 40
vel = 5
lompat = False
lompatan = 10

run = True
while run:
    pygame.time.delay(30)

    for program in pygame.event.get():

        if program.type == pygame.QUIT:
            run = False

    arah = pygame.key.get_pressed()

    if arah[pygame.K_LEFT] and x > vel:
        x -= vel

    if arah[pygame.K_RIGHT] and x < 500 - lebar - vel:
        x += vel

    if not(lompat):
        if arah[pygame.K_UP] and y > vel:
            y -= vel

        if arah[pygame.K_DOWN] and y < 500 - panjang - vel:
            y += vel
        if arah[pygame.K_SPACE]:
            lompat = True
    else:
        if lompatan >= -10:
            neg = 1
            if lompatan < 0:
                neg = -1
            y -= (lompatan ** 2) * 0.3 * neg
            lompatan -= 1
        else:
            lompat= False
            lompatan = 10
            
            

    ukuran.fill((200, 100, 30))
    pygame.draw.rect(ukuran, (50, 100, 0), (x, y, lebar, panjang))
    pygame.display.update()

pygame.quit()
