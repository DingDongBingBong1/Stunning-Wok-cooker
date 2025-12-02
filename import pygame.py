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
img2 = pygame.image.load("Screenshot 2025-12-02 102908.png")
img3 = pygame.image.load("Screenshot 2025-12-02 103546.png")

# Image 1 (left -> right)
x1 = -img1.get_width()
y1 = 0
speed1 = 7
image1_active = True

# Image 2 (appears for a few seconds)
x2 = 0
y2 = 0
image2_active = False
image2_start_time = 0
image2_duration = 0.7 # seconds

# Image 3 (moves right -> left)
x3 = 100  # start at right edge
y3 = 0
speed3 = 7
image3_active = False

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move Image 1
    if image1_active:
        x1 += speed1
        if x1 >= 360:
            image1_active = False
            image2_active = True
            image2_start_time = time.time()  # start timer

    # Show Image 2 for a few seconds
    if image2_active:
        if time.time() - image2_start_time >= image2_duration:
            image2_active = False
            image3_active = True
            x3 = 720  # reset Image 3 position at right edge

    # Move Image 3 (right -> left)
    if image3_active:
        x3 -= speed3
        if x3 + img3.get_width() < 0:
            image3_active = False

    # Draw everything
    screen.fill((0, 0, 0))
    if image1_active:
        screen.blit(img1, (x1, y1))
    if image2_active:
        screen.blit(img2, (x2, y2))
    if image3_active:
        screen.blit(img3, (x3, y3))

    pygame.display.update()

pygame.quit()