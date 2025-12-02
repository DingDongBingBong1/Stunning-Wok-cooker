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
font5 = pygame.font.Font("BloodyTerror-GOW9Z.ttf", 100)
font6 = pygame.font.Font("Youmurdererbb-pwoK.otf", 50)
running = True
screen.fill((0, 0, 0))
screen.blit(font1.render("I'll Take", True, (100, 0, 0)), (1, 50))
screen.blit(font3.render("a Potato", True, (255, 255, 0)), (140, 50))
screen.blit(font4.render("Chip...", True, (255, 0, 203)), (305, 55))
screen.blit(font5.render("AND EAT IT!!!", True, (240, 26, 26)), (15, 150))
screen.blit(font6.render("(Goofy Ahh Chuckle)", True, (201, 80, 24)), (40, 100))

pygame.display.update()

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()


import time

pygame.init()

screen = pygame.display.set_mode((720, 720))

img1 = pygame.image.load("Screenshot 2025-12-02 101145.png")
img2 = pygame.image.load("Screenshot 2025-12-02 103546.png")
img3 = pygame.image.load("Screenshot 2025-12-02 102908.png")

x1 = -200
y1 = 0
speed1 = 4

x2 = 720
y2 = 0
speed2 = 1
image2_active = False

x3 = 0
y3 = 0
image3_active = False
image3_start_time = 0
image3_duration = 1

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x1 += speed1

    if x1 >= 360 and not image3_active and not image2_active:
        image3_active = True
        image3_start_time = time.time()

    if image3_active:
        if time.time() - image3_start_time >= image3_duration:
            image3_active = False
            image2_active = True

    if image2_active:
        x2 -= speed2
        if x2 < -img2.get_width() - 800:  
            image2_active = False
            

    if x1 > 720:
        x1 = -img1.get_width()
        x2 = 720
        image2_active = False
        image3_active = False

    screen.fill((0, 0, 0))
    screen.blit(img1, (x1, y1))

    if image3_active:
        screen.blit(img3, (x3, y3))

    if image2_active:
        screen.blit(img2, (x2, y2))

    pygame.display.update()

pygame.quit()