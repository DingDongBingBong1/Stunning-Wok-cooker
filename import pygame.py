import pygame
pygame.init()
Width = 900
Height = 900
screen = pygame.display.set_mode((Width, Height))
ASurface = pygame.Surface((Width,5))
ASurface.fill(((43,125,125)))
ASurface.set_alpha(100)
BSurface = pygame.Surface((Width,5))
BSurface.fill(((64,217,144)))
BSurface.set_alpha(100)
CSurface = pygame.Surface((Width,5))
CSurface.fill(((14,43,52)))
CSurface.set_alpha(200)
DSurface = pygame.Surface((10,Height))
DSurface.fill(((137,237,247)))
DSurface.set_alpha(130)
ESurface = pygame.Surface((10,Height))
ESurface.fill(((6,37,73)))
ESurface.set_alpha(130)
screen.fill((255, 255, 255))
running = True
i = 0
for i in range(Height):
    screen.blit(ASurface,(0,(i*20)+5))
    screen.blit(CSurface,(0,(i*20)+15))
    screen.blit(BSurface,(0,(i*20)+30))
for x in range(Width):
    screen.blit(DSurface,((x*20)+5,0))
    screen.blit(ESurface,((x*20)+9,0))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()


pygame.init()
screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Window 2")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 255))
    pygame.display.flip()

pygame.quit()
