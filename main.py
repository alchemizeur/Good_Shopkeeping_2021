import pygame

pygame.init()

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('THIS IS GOOD SHOPKEEPING')

running = True

while running:
    for event in pygame.event.get(): ## quit game
        if event.type == pygame.QUIT:
            running = False

pygame.quit()