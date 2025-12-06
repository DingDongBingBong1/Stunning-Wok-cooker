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


import pygame, time, sys

pygame.init()
SCREEN_SIZE = (720, 720)
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

def fit_to_screen(img, screen_size=SCREEN_SIZE):
    w, h = img.get_size()
    sw, sh = screen_size
    scale = min(sw / w, sh / h)
    new_w, new_h = int(w * scale), int(h * scale)
    resized = pygame.transform.smoothscale(img, (new_w, new_h))
    surface = pygame.Surface((sw, sh), pygame.SRCALPHA)
    surface.blit(resized, ((sw - new_w) // 2, (sh - new_h) // 2))
    return surface

# -------------------------------------------------------
# Load Images (change filenames if necessary)
# -------------------------------------------------------
img1 = pygame.image.load("scene 1.png").convert_alpha()
img2 = pygame.image.load("scene 2.png").convert_alpha()
img3 = pygame.image.load("scene 3.png").convert_alpha()
img4 = pygame.image.load("Scene 4.png").convert_alpha()
img5 = pygame.image.load("scene 5.png").convert_alpha()
img6 = pygame.image.load("scene 6.png").convert_alpha()
img7 = pygame.image.load("scene 7.png").convert_alpha()

# Per your request: resize images AFTER image 4 (i.e., images 5,6,7) to fit window BEFORE anything else
img5 = fit_to_screen(img5)
img6 = fit_to_screen(img6)
img7 = fit_to_screen(img7)

# Optionally, also fit img4 so it's easier to zoom around center (but we keep original img4 for smoother zoom)
img4_fitted = fit_to_screen(img4)

# -------------------------------------------------------
# Fog: flattened, tiled top + bottom and active the whole time
# -------------------------------------------------------
raw_fog = pygame.image.load("Fog.png").convert_alpha()
FLAT_HEIGHT = 80
FLAT_WIDTH = 4000  # wide tiled texture

fog_image = pygame.transform.scale(raw_fog, (FLAT_WIDTH, FLAT_HEIGHT))
fog_speed = 200  # pixels per second (feel free to tweak)

# positions for two tiles for top and bottom
fog_top_x1 = 0
fog_top_x2 = FLAT_WIDTH
fog_top_y = 0

fog_bottom_x1 = 0
fog_bottom_x2 = FLAT_WIDTH
fog_bottom_y = SCREEN_SIZE[1] - FLAT_HEIGHT

fog_enabled = True  # fog runs throughout

# -------------------------------------------------------
# Animation / state machine setup
# -------------------------------------------------------
state = "image1"

# image 1 slides right -> left. start off-screen to the right
x1 = SCREEN_SIZE[0]
speed_px_s = 400  # slide speed in pixels per second (tweak if desired)

# image 2 timing
image2_duration = 1.0
image2_start = None

# image 3 slides left -> right. start off-screen to the left
x3 = -img3.get_width()

# image4 zoom out timing (0.25s)
img4_duration = 0.25
img4_start = None
img4_scale = 1.2  # starting scale (slightly zoomed in)
img4_target_scale = 1.0

# image5 rotate slowly: start slightly tilted clockwise, rotate slowly counter-clockwise
img5_angle = -8.0  # starts tilted clockwise (negative)
img5_rotate_speed = 8.0  # degrees per second, positive -> rotates CCW (slow)
img5_start = None
img5_duration = 2.5  # total display time for image5 (tweak as desired)
img5_scale = 1.0

# image6 & image7 display durations
image6_duration = 1.0
image7_duration = 1.0
image6_start = None
image7_start = None

running = True
while running:
    dt = clock.tick(60) / 1000.0  # seconds elapsed since last frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -------------------------------------------------------
    # Fog movement (continuous)
    # -------------------------------------------------------
    if fog_enabled:
        fog_top_x1 -= fog_speed * dt
        fog_top_x2 -= fog_speed * dt
        fog_bottom_x1 -= fog_speed * dt
        fog_bottom_x2 -= fog_speed * dt

        # wrap tiles (simple tiling)
        if fog_top_x1 + FLAT_WIDTH < 0:
            fog_top_x1 = fog_top_x2 + FLAT_WIDTH
        if fog_top_x2 + FLAT_WIDTH < 0:
            fog_top_x2 = fog_top_x1 + FLAT_WIDTH

        if fog_bottom_x1 + FLAT_WIDTH < 0:
            fog_bottom_x1 = fog_bottom_x2 + FLAT_WIDTH
        if fog_bottom_x2 + FLAT_WIDTH < 0:
            fog_bottom_x2 = fog_bottom_x1 + FLAT_WIDTH

    # -------------------------------------------------------
    # State machine
    # -------------------------------------------------------
    if state == "image1":
        # slide right -> left
        x1 -= speed_px_s * dt
        # When image has reached x <= 0 (fully aligned), go to image2
        if x1 <= 0:
            x1 = 0
            state = "image2"
            image2_start = time.time()

    elif state == "image2":
        if time.time() - image2_start >= image2_duration:
            # prepare image3 start position (off left)
            x3 = -img3.get_width()
            state = "image3"

    elif state == "image3":
        # slide left -> right (entering from left)
        x3 += speed_px_s * dt
        # once image reaches x >= 0 (fully on screen), hold briefly then move to image4
        if x3 >= 0:
            x3 = 0
            # go to image4 after a short pause (0.15s)
            state = "image3_hold"
            hold_start = time.time()

    elif state == "image3_hold":
        if time.time() - hold_start >= 0.15:
            state = "image4_zoom"
            img4_start = time.time()
            img4_scale = 1.2  # re-init

    elif state == "image4_zoom":
        elapsed = time.time() - img4_start
        t = min(elapsed / img4_duration, 1.0)
        # linear interpolation of scale from start to target over img4_duration
        img4_scale = 1.2 + (img4_target_scale - 1.2) * t

        if elapsed >= img4_duration:
            # stay at final scale and proceed to image5
            state = "image5"
            img5_start = time.time()
            img5_angle = -8.0  # start slightly tilted clockwise
            img5_scale = 1.0

    elif state == "image5":
        elapsed = time.time() - img5_start
        # rotate slowly counter-clockwise (angle increases)
        img5_angle += img5_rotate_speed * dt
        if elapsed >= img5_duration:
            state = "image6"
            image6_start = time.time()

    elif state == "image6":
        if time.time() - image6_start >= image6_duration:
            state = "image7"
            image7_start = time.time()

    elif state == "image7":
        if time.time() - image7_start >= image7_duration:
            running = False

    # -------------------------------------------------------
    # Drawing
    # -------------------------------------------------------
    screen.fill((0, 0, 0))

    if state in ("image1", "image2", "image3", "image3_hold"):
        # draw img1 or img2 or img3 depending on state
        if state == "image1":
            screen.blit(img1, (int(x1), 0))
        elif state == "image2":
            screen.blit(img2, (0, 0))
        else:  # image3 or hold
            screen.blit(img3, (int(x3), 0))

    elif state == "image4_zoom":
        # use fitted img4 and scale it by img4_scale relative to fit_to_screen result:
        base = img4_fitted
        sw, sh = base.get_size()
        scaled = pygame.transform.smoothscale(base, (int(sw * img4_scale), int(sh * img4_scale)))
        sw2, sh2 = scaled.get_size()
        screen.blit(scaled, ((SCREEN_SIZE[0] - sw2) // 2, (SCREEN_SIZE[1] - sh2) // 2))

    elif state == "image5":
        # img5 already fitted to screen; rotate around center using rotozoom
        rotated = pygame.transform.rotozoom(img5, img5_angle, img5_scale)
        sw, sh = rotated.get_size()
        screen.blit(rotated, ((SCREEN_SIZE[0] - sw) // 2, (SCREEN_SIZE[1] - sh) // 2))

    elif state == "image6":
        screen.blit(img6, (0, 0))

    elif state == "image7":
        screen.blit(img7, (0, 0))

    # -------------------------------------------------------
    # Fog overlay (top and bottom), always active
    # -------------------------------------------------------
    # top tiles
    screen.blit(fog_image, (int(fog_top_x1), fog_top_y))
    screen.blit(fog_image, (int(fog_top_x2), fog_top_y))
    # bottom tiles
    screen.blit(fog_image, (int(fog_bottom_x1), fog_bottom_y))
    screen.blit(fog_image, (int(fog_bottom_x2), fog_bottom_y))

    pygame.display.flip()

pygame.quit()
