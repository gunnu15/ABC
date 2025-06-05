import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
screen.fill((255, 255, 255))
GREEEN = (0, 255, 0)
pygame.display.set_caption('Adding Images and background image')
pygame.draw.circle(window, GREEN, (300, 300), 50)
pygame.draw.circle(window, GREEN, (300, 300), 50, 3)
pygame.display.update()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()