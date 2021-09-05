import pygame

pygame.init()

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('THIS IS GOOD SHOPKEEPING')

x = 200 ## player location
y = 200 ## player location

player_img = pygame.image.load('sprites/sprite_test.png') # placeholder?
rect = player_img.get_rect() #creates a boundary box for the character for collision
rect.center = (x,y)

running = True

while running:

    screen.blit(player_img, rect)
    for event in pygame.event.get(): ## quit game
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()