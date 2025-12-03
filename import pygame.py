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


import pygame, time

pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()

# -------------------------------------------------------
# Load Images
# -------------------------------------------------------
img1 = pygame.image.load("Screenshot 2025-12-02 101145.png")
img2 = pygame.image.load("Screenshot 2025-12-02 102908.png")
img3 = pygame.image.load("Screenshot 2025-12-02 103546.png")

# -------------------------------------------------------
# Load Fog + flatten it
# -------------------------------------------------------
raw_fog = pygame.image.load("Fog.png")

FLAT_HEIGHT = 80
FLAT_WIDTH = 4000   # Must be wider than the screen for smooth overlap

fog1 = pygame.transform.scale(raw_fog, (FLAT_WIDTH, FLAT_HEIGHT))
fog2 = pygame.transform.scale(raw_fog, (FLAT_WIDTH, FLAT_HEIGHT))

# These are used for top and bottom (copies)
fog_top1 = fog1
fog_top2 = fog2

fog_bottom1 = fog1
fog_bottom2 = fog2

# -------------------------------------------------------
# Fog Positions + Speed
# -------------------------------------------------------
fog_speed = 500

# Bottom fog pair
fog_bottom_x1 = 0
fog_bottom_x2 = FLAT_WIDTH
fog_bottom_y = 720 - FLAT_HEIGHT

# Top fog pair
fog_top_x1 = 0
fog_top_x2 = FLAT_WIDTH-380
fog_top_y = 0

# -------------------------------------------------------
# Main Animation Settings
# -------------------------------------------------------
state = "image1"

x1 = -500
x3 = 0

speed = 5
image2_start = 0
image2_duration = 0.8

running = True
while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -------------------------------------------------------
    # Fog Scroll Logic (top + bottom)
    # -------------------------------------------------------

    # Bottom fog scrolling
    fog_bottom_x1 -= fog_speed
    fog_bottom_x2 -= fog_speed

    # Loop bottom fog chunks
    if fog_bottom_x1 + FLAT_WIDTH < 0:
        fog_bottom_x1 = fog_bottom_x2 + FLAT_WIDTH
    if fog_bottom_x2 + FLAT_WIDTH < 0:
        fog_bottom_x2 = fog_bottom_x1 + FLAT_WIDTH

    # Top fog scrolling
    fog_top_x1 -= fog_speed
    fog_top_x2 -= fog_speed

    # Loop top fog chunks
    if fog_top_x1 + FLAT_WIDTH < 0:
        fog_top_x1 = fog_top_x2 + FLAT_WIDTH
    if fog_top_x2 + FLAT_WIDTH < 0:
        fog_top_x2 = fog_top_x1 + FLAT_WIDTH

    # -------------------------------------------------------
    # Main Animation State Machine
    # -------------------------------------------------------
    if state == "image1":
        x1 += speed
        if x1 >= 200:
            state = "image2"
            image2_start = time.time()

    elif state == "image2":
        if time.time() - image2_start >= image2_duration:
            state = "image3"

    elif state == "image3":
        x3 -= speed
        if x3 + img3.get_width() < -400:
            state = "done"

    # -------------------------------------------------------
    # Draw Everything
    # -------------------------------------------------------
    screen.fill((0, 0, 0))

    # Main images
    if state == "image1":
        screen.blit(img1, (x1, 0))
    elif state == "image2":
        screen.blit(img2, (0, 0))
    elif state == "image3":
        screen.blit(img3, (x3, 0))

    # Fog: draw two strips on top + two on bottom
    screen.blit(fog_top1, (fog_top_x1, fog_top_y))
    screen.blit(fog_top2, (fog_top_x2, fog_top_y))

    screen.blit(fog_bottom1, (fog_bottom_x1, fog_bottom_y))
    screen.blit(fog_bottom2, (fog_bottom_x2, fog_bottom_y))

    pygame.display.update()

pygame.quit()