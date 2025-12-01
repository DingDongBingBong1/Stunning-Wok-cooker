import pygame
pygame.init()
Width = 720
Height = 720
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
ESurface.set_alpha(150)
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
pygame.mixer.init()

screen = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Window 2")

# Load sound
sound = pygame.mixer.Sound("i'll-take-a-potato-chip...and-eat-it!-made-with-Voicemod.mp3")
sound.set_volume(1.0)

sound.play()
font1 = pygame.font.Font("it´s Scary Now St.ttf", 30)
font2 = pygame.font.Font("NoScary-regular.ttf", 50)
font3 = pygame.font.Font("Scary Brusher.ttf", 50)
font4 = pygame.font.Font("Scary Pumpkin.ttf", 30)
font5 = pygame.font.Font("BloodyTerror-GOW9Z.ttf", 150)
font6 = pygame.font.Font("Youmurdererbb-pwoK.otf", 50)
running = True
screen.fill((0, 0, 0))
screen.blit(font1.render("I'm Going", True, (255, 255, 0)), (1, 50))
screen.blit(font2.render("To Take", True, (255, 255, 0)), (125, 50))
screen.blit(font3.render("a Potato", True, (255, 255, 0)), (250, 50))
screen.blit(font4.render("Chip And...", True, (255, 255, 0)), (420, 55))
screen.blit(font5.render("EAT IT!!!", True, (255, 255, 0)), (40, 150))
screen.blit(font6.render("(Goofy Ahh Chuckle)", True, (255, 255, 0)), (40, 100))

pygame.display.update()

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
