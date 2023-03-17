import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

color = {"Black": (0, 0, 0), "White": (255, 255, 255),
         "Blue": (0, 0, 255), "Yellow": (255, 255, 0), "Red": (255, 0, 0), "Green": (0, 255, 0)}

pygame.init()

FPS = pygame.time.Clock()
screen = weight, height = 800, 600
is_working = True

# hero
ball = pygame.Surface((20, 20))
ball.fill(color["White"])
ball_rect = ball.get_rect()
ball_speed = 5

# AI
enemies = []


def create_enemy():
    enemy = pygame.Surface((20, 20))
    enemy.fill(color["Red"])
    enemy_rect = pygame.Rect(
        weight, random.randint(0, height), *enemy.get_size())
    enemy_speed = random.randint(2, 5)
    return [enemy, enemy_rect, enemy_speed]


#Bonus
bonuses = []


def create_bonus():
    bonus = pygame.Surface((20, 20))
    bonus.fill(color["Green"])
    bonus_rect = pygame.Rect(random.randint(0, weight), 0, *bonus.get_size())
    bonus_speed = random.randint(1, 3)
    return [bonus, bonus_rect, bonus_speed]

#events init
CREATE_EVENT_AI = pygame.USEREVENT + 1
CREATE_EVENT_BONUS = pygame.USEREVENT +2
pygame.time.set_timer(CREATE_EVENT_AI, 1500)
pygame.time.set_timer(CREATE_EVENT_BONUS, 3000)
# set game display

main_surface = pygame.display.set_mode(screen)
# game progress
while is_working:
    FPS.tick(120)
    # events
    for event in pygame.event.get():
        if event.type == QUIT:  # exit
            is_working = False
        if event.type == CREATE_EVENT_AI:  # createai
            enemies.append(create_enemy())
        if event.type == CREATE_EVENT_BONUS:
            bonuses.append(create_bonus())
    # init object
    main_surface.fill(color["Black"])
    main_surface.blit(ball, ball_rect)

    # initai
    for enemi in enemies:
        enemi[1] = enemi[1].move(-enemi[2], 0)
        main_surface.blit(enemi[0], enemi[1])
        if enemi[1].left < 0:
            enemies.pop(enemies.index(enemi))
        if ball_rect.colliderect(enemi[1]):
            enemies.pop(enemies.index(enemi))

    # initbonus
    for bonuc in bonuses:
        bonuc[1] = bonuc[1].move(0, bonuc[2])
        main_surface.blit(bonuc[0], bonuc[1])
        if bonuc[1].left > height:
            bonuses.pop(bonuses.index(bonuc))
        if ball_rect.colliderect(bonuc[1]):
            bonuses.pop(bonuses.index(bonuc))

    # move
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_DOWN] and not ball_rect.bottom >= height:
        ball_rect = ball_rect.move((0, ball_speed))
    if pressed_keys[K_UP] and not ball_rect.top <= 0:
        ball_rect = ball_rect.move((0, -ball_speed))
    if pressed_keys[K_RIGHT] and not ball_rect.right >= weight:
        ball_rect = ball_rect.move((ball_speed, 0))
    if pressed_keys[K_LEFT] and not ball_rect.left <= 0:
        ball_rect = ball_rect.move((-ball_speed, 0))

    pygame.display.flip()

################################################
   # if ball_rect.bottom >= height or ball_rect.top <= 0:
   #    ball_speed[1] = -ball_speed[1]
   #     ball.fill(color["Blue"])
   # if ball_rect.right >= weight or ball_rect.left <= 0:
   #     ball_speed[0] = -ball_speed[0]
   #     ball.fill(color["Yellow"])
 ################################################
