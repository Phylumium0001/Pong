from sys import exit
import pygame
from random import choice

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((600,400))
screen.fill("BlueViolet")

space_obj = pygame.image.load('Pong Assets/bg_1_1.png').convert()
scoreBoard_obj = pygame.image.load('Pong Assets/background.jpg').convert()
score_font = pygame.font.Font(None, 25)

player1_score = 0
player2_score = 0

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

velocity = 10

# Menu Screen
play = False
menu_font = pygame.font.Font(None,60)

menu_obj = pygame.image.load('Pong Assets/menu2.jpg').convert()

while not play:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if exit_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
                exit()

            if start_rect.collidepoint(pygame.mouse.get_pos()):
                play = True

    screen.blit(menu_obj,(0,0))

    # Menu
    # Start
    start_surf = menu_font.render("Start Game",False, "WhiteSmoke")
    start_rect = start_surf.get_rect(center=(150,150))
    # Hovering effect
    if start_rect.collidepoint(pygame.mouse.get_pos()):
        start_surf = menu_font.render("Start Game",False, "Black")
    screen.blit(start_surf, start_rect)

    # Option
    options_surf = menu_font.render("Options",False, "WhiteSmoke")
    options_rect = options_surf.get_rect(center=(150,220))
    # Hovering effect
    if options_rect.collidepoint(pygame.mouse.get_pos()):
        options_surf = menu_font.render("Options",False, "Black")
    screen.blit(options_surf, options_rect)

    # Exit
    exit_surf = menu_font.render("Exit",False, "WhiteSmoke")
    exit_rect = exit_surf.get_rect(center=(150,290))
    if exit_rect.collidepoint(pygame.mouse.get_pos()):
        exit_surf = menu_font.render("Exit",False, "Black")
    screen.blit(exit_surf, exit_rect)

    


    pygame.display.update()
    clock.tick(60)


while play:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # When a key is pressed
        if pygame.key.get_pressed()[pygame.K_w]:
            if pad1_rect.topleft[1] >= 35:
                pad1_rect.y -= velocity
        if pygame.key.get_pressed()[pygame.K_s]:
            if pad1_rect.bottomleft[1] <= 395:
                pad1_rect.y += velocity

        # Pad 2
        if pygame.key.get_pressed()[pygame.K_UP]:
            # Prevent the pad from leaving the screen
            if pad2_rect.topleft[1] >= 35:
                pad2_rect.y -= velocity

        if pygame.key.get_pressed()[pygame.K_DOWN]:
            if pad2_rect.bottomleft[1] <= 395:
                pad2_rect.y += 20

        if event.type == pygame.KEYDOWN:
            # Continue
            if event.key == pygame.K_SPACE:
                # Ball start if in the centerw
                if ball_rect.center == (300,200):
                    direction_x = choice([2,-2])
                    direction_y = choice([2,-2])
 

    screen.blit(space_obj, (0,25))
    screen.blit(scoreBoard_obj, (0,0))

    # Score Board
    score_surf = score_font.render(f"{player1_score} : {player2_score}",False, "WhiteSmoke")
    score_rect = score_surf.get_rect(center=(300,10))
    screen.blit(score_surf,score_rect)

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

    if ball_rect.left < 25:
        ball_rect.center = (300,200)
        pygame.draw.ellipse(screen,"Yellow",ball_rect)
        direction_y = 0
        direction_x = 0
        player2_score += 1

    if ball_rect.right > 575:
        ball_rect.center = (300,200)
        pygame.draw.ellipse(screen,"Yellow",ball_rect)
        direction_y = 0
        direction_x = 0
        player1_score += 1

    ball_rect.y += direction_y
    ball_rect.x += direction_x
    # print(pad1_rect.topright)
        
    pygame.draw.ellipse(screen,"Yellow",ball_rect)

    pygame.display.update()
    clock.tick(60)
