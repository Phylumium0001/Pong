from sys import exit
import pygame
from random import choice

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((600,400))
screen.fill("BlueViolet")

sky_obj = pygame.image.load('Pong Assets/bg_1_1.png').convert()


# Create Surface
pad1_surf = pygame.Surface((15,70))
pad2_surf = pygame.Surface((15,70))
ball_surf = pygame.Surface((15,15))

# Rect
pad1_rect = pad1_surf.get_rect(topleft=(20,165))
pad2_rect = pad1_surf.get_rect(topleft=(570,165))
ball_rect = ball_surf.get_rect(center=(300,200))

direction_x = choice([2,-2])
direction_y = choice([2,-2])

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # When a key is pressed
        if event.type == pygame.KEYDOWN:
            # Move up
            if event.key == pygame.K_w:
                if pad1_rect.topleft[1] >= 0:
                    pad1_rect.y -= 20
                

            # Move down
            if event.key == pygame.K_s:
                pad1_rect.y += 20

    screen.blit(sky_obj, (0,0))

    pygame.draw.rect(screen,"Red", pad1_rect)
    pygame.draw.rect(screen,"Blue",pad2_rect)

    # Direction
    # direction = ('left','right','bottom','right')

    # Ball Motion
    #Up
    if ball_rect.midtop[1] <= 2:
        print(ball_rect.midtop)
        direction_y = 2

    # Down
    if ball_rect.midbottom[1] >= 400:
        direction_y = -2

    #Left collision
    if ball_rect.midleft[0] <= 2:
        direction_x = 2

    # Right Collision
    if ball_rect.midright[0] >= 600:
        direction_x = -2 

    ball_rect.y += direction_y
    ball_rect.x += direction_x

    # print(ball_rect.center)

    # Collisions
    if pad1_rect.collidepoint(ball_rect.midleft):
        direction_x,direction_y = direction_y,direction_x
        print("Collision")
    pygame.draw.ellipse(screen,"Yellow",ball_rect)

    pygame.display.update()
    clock.tick(60)
