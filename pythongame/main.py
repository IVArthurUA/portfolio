import pygame
from pygame.constants import QUIT

color = {"Black": (0, 0, 0), "White": (255, 255, 255),
         "Blue": (0, 0, 255), "Yellow": (255, 255, 0)}

pygame.init()

screen = weight, height = 800, 600
is_working = True
ball = pygame.Surface((20, 20))
ball.fill(color["White"])
ball_rect = ball.get_rect()
ball_speed = [1, 1]

main_surface = pygame.display.set_mode(screen)

while is_working:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

    ball_rect = ball_rect.move(ball_speed)
   # if ball_rect.bottom >= height or ball_rect.top <= 0:
   #    ball_speed[1] = -ball_speed[1]
   #     ball.fill(color["Blue"])
   # if ball_rect.right >= weight or ball_rect.left <= 0:
   #     ball_speed[0] = -ball_speed[0]
   #     ball.fill(color["Yellow"])
        
    main_surface.fill(color["Black"])
    main_surface.blit(ball, ball_rect)
    pygame.display.flip()
