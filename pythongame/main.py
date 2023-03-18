import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

#vars
color = {"Black": (0, 0, 0), "White": (255, 255, 255),
         "Blue": (0, 0, 255), "Yellow": (255, 255, 0), "Red": (255, 0, 0), "Green": (0, 255, 0)}
is_working = True

#start
pygame.init()


# set game display
FPS = pygame.time.Clock()
screen = weight, height = 800, 600
main_surface = pygame.display.set_mode(screen)
scores = 0
scores_font = pygame.font.SysFont("Verdana", 20)


# bg
bg = pygame.transform.scale(pygame.image.load("background.png").convert(), screen)
bg_x0 = 0
bg_x = bg.get_width()
bg_speed = 3

# hero
player = pygame.image.load("player.png").convert_alpha()
player_rect = player.get_rect()
player_speed = 5

# AI
enemies = []


def create_enemy():  
    enemy = pygame.image.load("enemy.png").convert_alpha()
    enemy_rect = pygame.Rect(
        weight, random.randint(0, height-enemy.get_width()), *enemy.get_size())
    enemy_speed = random.randint(2, 5)
    return [enemy, enemy_rect, enemy_speed]


#Bonus
bonuses = []


def create_bonus():
    bonus = pygame.image.load("bonus.png").convert_alpha()
    bonus_rect = pygame.Rect(random.randint(0, weight-bonus.get_width()), 0, *bonus.get_size())
    bonus_speed = random.randint(1, 3)
    return [bonus, bonus_rect, bonus_speed]

#events init
CREATE_EVENT_AI = pygame.USEREVENT + 1
CREATE_EVENT_BONUS = pygame.USEREVENT +2
pygame.time.set_timer(CREATE_EVENT_AI, 1500)
pygame.time.set_timer(CREATE_EVENT_BONUS, 3000)



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
    # init bg


    bg_x0 -= bg_speed
    bg_x -= bg_speed
    if bg_x0 < -bg.get_width():
        bg_x0 = bg.get_width()
    if bg_x < -bg.get_width():
        bg_x = bg.get_width()
    main_surface.blit(bg, (bg_x0, 0))
    main_surface.blit(bg, (bg_x, 0))

    # init object
    main_surface.blit(player, player_rect)
    main_surface.blit(scores_font.render(str(scores), True, color["Blue"]),( weight-30, 0))

    # initai
    for enemi in enemies:
        enemi[1] = enemi[1].move(-enemi[2], 0)
        main_surface.blit(enemi[0], enemi[1])
        if enemi[1].left < 0:
            enemies.pop(enemies.index(enemi))
        if player_rect.colliderect(enemi[1]):
            is_working = False

    # initbonus
    for bonuc in bonuses:
        bonuc[1] = bonuc[1].move(0, bonuc[2])
        main_surface.blit(bonuc[0], bonuc[1])
        if bonuc[1].left > height:
            bonuses.pop(bonuses.index(bonuc))
        if player_rect.colliderect(bonuc[1]):
            bonuses.pop(bonuses.index(bonuc))
            scores +=1

    # move
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_DOWN] and not player_rect.bottom >= height:
        player_rect = player_rect.move((0, player_speed))
    if pressed_keys[K_UP] and not player_rect.top <= 0:
        player_rect = player_rect.move((0, -player_speed))
    if pressed_keys[K_RIGHT] and not player_rect.right >= weight:
        player_rect = player_rect.move((player_speed, 0))
    if pressed_keys[K_LEFT] and not player_rect.left <= 0:
        player_rect = player_rect.move((-player_speed, 0))

    pygame.display.flip()
#end

################################################
   # if player_rect.bottom >= height or player_rect.top <= 0:
   #    player_speed[1] = -player_speed[1]
   #     player.fill(color["Blue"])
   # if player_rect.right >= weight or player_rect.left <= 0:
   #     player_speed[0] = -player_speed[0]
   #     player.fill(color["Yellow"])
 ################################################
    # player = pygame.Surface((20, 20))
    # player.fill(color["White"])
    # enemy = pygame.Surface((20, 20))
    # enemy.fill(color["Red"])
    # bonus = pygame.Surface((20, 20))
    # bonus.fill(color["Green"])
    # main_surface.fill(color["Black"])
    # main_surface.blit(bg,(0, 0))
