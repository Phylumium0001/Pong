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


# Pausing Game
pause = False

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # When a key is pressed
        if event.type == pygame.KEYDOWN:
            # Continue
            if event.key == pygame.K_SPACE:
                if ball_rect.center == (300,200):
                    direction_x = choice([2,-2])
                    direction_y = choice([2,-2])

            # Move up
            if event.key == pygame.K_w:
                # Prevent the pad from leaving the screen
                if pad1_rect.topleft[1] >= 35:
                    pad1_rect.y -= 20
                

            # Move down
            if event.key == pygame.K_s:
                if pad1_rect.bottomleft[1] <= 395:
                    pad1_rect.y += 20

            # pad2
            # Move up
            if event.key == pygame.K_UP:
                # Prevent the pad from leaving the screen
                if pad2_rect.topleft[1] >= 35:
                    pad2_rect.y -= 20
                

            # Move down
            if event.key == pygame.K_DOWN:
                if pad2_rect.bottomleft[1] <= 395:
                    pad2_rect.y += 20

    screen.blit(sky_obj, (0,25))

    pygame.draw.rect(screen,"Red", pad1_rect)
    pygame.draw.rect(screen,"Blue",pad2_rect)

    # Direction
    # direction = ('left','right','bottom','right')

    # Ball Motion
    #Upward Collision
    if ball_rect.midtop[1] <= 27:
        direction_y = 2

    # Down Collision
    if ball_rect.midbottom[1] >= 400:
        direction_y = -2

    #Left collision
    if ball_rect.midleft[0] <= 2:
        direction_x = 2

    # Right Collision
    if ball_rect.midright[0] >= 600:
        direction_x = -2 

    # Collisions

    # Pad1 collision
    if pad1_rect.collidepoint(ball_rect.left,ball_rect.y):
        print(ball_rect.left)
        if direction_x == 2:direction_x = -2
        else: direction_x = 2

    # Pad2 collision
    if pad2_rect.collidepoint(ball_rect.right,ball_rect.y):
        print(ball_rect.right)
        if direction_x == 2:direction_x = -2
        else: direction_x = 2

    if ball_rect.left < 25 or ball_rect.right > 575:
        ball_rect.center = (300,200)
        pygame.draw.ellipse(screen,"Yellow",ball_rect)
        direction_y = 0
        direction_x = 0

    ball_rect.y += direction_y
    ball_rect.x += direction_x
    # print(pad1_rect.topright)
        
    pygame.draw.ellipse(screen,"Yellow",ball_rect)

    pygame.display.update()
    clock.tick(60)
