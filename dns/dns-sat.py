import pygame
import os.path

pygame.init()

white = (255, 255, 255,)

X = 800
Y = 700



while True:
    display_surface = pygame.display.set_mode((X, Y))
    image = pygame.image.load('yee')
    display_surface.fill(white)
    display_surface.blit(image, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        pygame.display.update()