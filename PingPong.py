import pygame
import random

# Initsialiseerib Pygamei ja loob ekraani
pygame.init()
laius, kõrgus = 640, 480
ekraan = pygame.display.set_mode((laius, kõrgus))
pygame.display.set_caption("Palli mäng")

# Värvid ja font
taust = (249, 230, 132)
tekst = (0, 0, 0)
font = pygame.font.Font(None, 36)

# Laeb pildid ja suuruse
ball_img = pygame.transform.scale(pygame.image.load("ball.png"), (20, 20))
pad_img = pygame.transform.scale(pygame.image.load("pad.png"), (120, 20))

# Palli seaded
ball_rect = ball_img.get_rect()
ball_rect.x = random.randint(20, laius - 20)
ball_rect.y = kõrgus // 2
ball_speed = [4 * random.choice([-1, 1]), 4]

# Aluse seaded
pad_rect = pad_img.get_rect()
pad_rect.x = (laius - pad_rect.width) // 2
pad_rect.y = int(kõrgus / 1.5)
aluse_kiirus = 2
suund = 1

# Punktid
score = 0

# Mängutsükkel
run = True
while run:
    pygame.time.delay(15)
    ekraan.fill(taust)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Palli liikuminre
    ball_rect.x += ball_speed[0]
    ball_rect.y += ball_speed[1]

    # Seinapõrked
    if ball_rect.left <= 0 or ball_rect.right >= laius:
        ball_speed[0] *= -1
    if ball_rect.top <= 0:
        ball_speed[1] *= -1
    if ball_rect.bottom >= kõrgus:
        ball_speed[1] *= -1
        score -= 1

    # Kokkupõrge alusega
    if ball_rect.colliderect(pad_rect) and ball_speed[1] > 0:
        ball_speed[1] *= -1
        score += 1

    # Aluse liikumine
    pad_rect.x += aluse_kiirus * suund
    if pad_rect.left <= 0 or pad_rect.right >= laius:
        suund *= -1

    # Joonistab asjad ekraanile
    ekraan.blit(ball_img, ball_rect)
    ekraan.blit(pad_img, pad_rect)
    ekraan.blit(font.render(f"Punktid: {score}", True, tekst), (10, 10))

    pygame.display.update()

pygame.quit()