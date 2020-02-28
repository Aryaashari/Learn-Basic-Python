import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Arya")

run = True
while run:
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        
pygame.quit()
