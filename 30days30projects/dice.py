import pygame
import sys
import random

pygame.init()
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dice Roller")

font = pygame.font.SysFont(None, 100)
button_font = pygame.font.SysFont(None, 40)

dice_box = pygame.Rect(width // 2 - 75, height // 2 - 75, 150, 150)
button_box = pygame.Rect(width // 2 - 60, height - 100, 120, 50)

rolling = False
roll_count = 20
roll_frame = 0
dice_num = 1

def drawdice(num):
    pygame.draw.rect(screen, (255, 255, 255), dice_box)
    pygame.draw.rect(screen, (0, 0, 0), dice_box, 5)
    txt = font.render(str(num), True, (0, 0, 0))
    txt_rect = txt.get_rect(center=dice_box.center)
    screen.blit(txt, txt_rect)

def drawbutton():
    pygame.draw.rect(screen, (0, 128, 255), button_box)
    txt = button_font.render("Roll", True, (255, 255, 255))
    txt_rect = txt.get_rect(center=button_box.center)
    screen.blit(txt, txt_rect)

clock = pygame.time.Clock()

while True:
    screen.fill((30, 30, 30))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            if button_box.collidepoint(e.pos) and not rolling:
                rolling = True
                roll_frame = 0

    if rolling:
        dice_num = random.randint(1, 6)
        roll_frame += 1
        if roll_frame >= roll_count:
            rolling = False

    drawdice(dice_num)
    drawbutton()

    pygame.display.flip()
    clock.tick(30)
