import pygame
import random

pygame.init()

width, height = 600, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("rocket shooter")

white = (255, 255, 255)
black = (0, 0, 0)
red = (220, 20, 60)
dblue = (10, 10, 40)
yellow = (255, 255, 0)
orange = (255, 140, 0)
green = (0, 255, 0)

pos = [width // 2, height - 60]
speed = 7
w = 40
h = 60

bullet_w, bullet_h = 5, 15
bullet_speed = -10
bullets = []

enemy_radius = 25
enemy_speed = 3
enemies = []
enemy_spawn_rate = 30
frame_count = 0

score = 0
font = pygame.font.SysFont(None, 36)

game_over = False
clock = pygame.time.Clock()

def dplayer(p):
    x, y = p
    points = [(x, y - h // 2), (x - w // 2, y + h // 2), (x + w // 2, y + h // 2)]
    pygame.draw.polygon(screen, green, points)
    flame_points1 = [(x, y + h // 2 + 10), (x - 10, y + h // 2), (x + 10, y + h // 2)]
    flame_points2 = [(x, y + h // 2 + 5), (x - 5, y + h // 2), (x + 5, y + h // 2)]
    pygame.draw.polygon(screen, orange, flame_points1)
    pygame.draw.polygon(screen, yellow, flame_points2)

def dbullet(rect):
    pygame.draw.rect(screen, white, rect)

def denemy(pos):
    pygame.draw.circle(screen, red, pos, enemy_radius)
    offsets = [-10, 0, 10]
    for offset in offsets:
        pygame.draw.circle(screen, white, (pos[0] + offset, pos[1]), 6)

def dtext(text, x, y):
    img = font.render(text, True, white)
    screen.blit(img, (x, y))

running = True
while running:
    clock.tick(60)
    screen.fill(dblue)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT] and pos[0] - w // 2 > 0:
            pos[0] -= speed
        if keys[pygame.K_RIGHT] and pos[0] + w // 2 < width:
            pos[0] += speed

        if keys[pygame.K_SPACE]:
            if len(bullets) == 0 or bullets[-1].y < height - 150:
                bullet_rect = pygame.Rect(pos[0] - bullet_w // 2, pos[1] - h // 2 - bullet_h, bullet_w, bullet_h)
                bullets.append(bullet_rect)

        for bullet in bullets[:]:
            bullet.y += bullet_speed
            if bullet.y < 0:
                bullets.remove(bullet)

        frame_count += 1
        if frame_count >= enemy_spawn_rate:
            frame_count = 0
            enemy_x = random.randint(enemy_radius, width - enemy_radius)
            enemies.append([enemy_x, -enemy_radius])

        for enemy_pos in enemies[:]:
            enemy_pos[1] += enemy_speed
            if enemy_pos[1] - enemy_radius > height:
                game_over = True

            player_rect = pygame.Rect(pos[0] - w // 2, pos[1] - h // 2, w, h)
            enemy_rect = pygame.Rect(enemy_pos[0] - enemy_radius, enemy_pos[1] - enemy_radius, enemy_radius * 2, enemy_radius * 2)
            if player_rect.colliderect(enemy_rect):
                game_over = True

            for bullet in bullets[:]:
                if enemy_rect.colliderect(bullet):
                    enemies.remove(enemy_pos)
                    bullets.remove(bullet)
                    score += 1
                    break

        dplayer(pos)
        for bullet in bullets:
            dbullet(bullet)
        for enemy_pos in enemies:
            denemy(enemy_pos)

        dtext(f"score: {score}", 10, 10)

    else:
        dtext("game over", width // 2 - 80, height // 2 - 30)
        dtext(f"final score: {score}", width // 2 - 110, height // 2 + 10)

    pygame.display.flip()

pygame.quit()
