import pygame
pygame.init()
Width = 900
Height = 900
screen = pygame.display.set_mode((Width, Height))
ASurface = pygame.Surface((Width,5))
ASurface.fill((100,0,0))
ASurface.set_alpha(100)
BSurface = pygame.Surface((Width,5))
BSurface.fill((100,100,0))
BSurface.set_alpha(100)
CSurface = pygame.Surface((Width,5))
CSurface.fill((100, 100, 100))
CSurface.set_alpha(200)
DSurface = pygame.Surface((10,Height))
DSurface.fill((200, 100, 100))
DSurface.set_alpha(130)
ESurface = pygame.Surface((10,Height))
ESurface.fill((200, 200, 100))
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
    screen.blit(ESurface,((x*20)+10,0))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()