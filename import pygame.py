import pygame
pygame.init()
Width = 1280
Height = 720
screen = pygame.display.set_mode((Width, Height))
redSurface = pygame.Surface((Width,10))
redSurface.fill((255,0,0))
redSurface.set_alpha(100)
blueSurface = pygame.Surface((Width,5))
blueSurface.fill((255, 184, 61))
blueSurface.set_alpha(200)
greenSurface = pygame.Surface((10,Height))
greenSurface.fill((86, 232, 205))
greenSurface.set_alpha(130)
screen.fill((227, 163, 159))
running = True
i = 0
for i in range(Height):
    screen.blit(redSurface,(0,i*60))
    screen.blit(blueSurface,(0,(i*60)+30))
for x in range(Width):
    screen.blit(greenSurface,(x*40,0))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()