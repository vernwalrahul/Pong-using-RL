#License MIT 2016 Ahmad Retha

import pygame
import random
##
# Game mode
#
WIDTH = 640
HEIGHT = 480
SCREEN_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()
pygame.key.set_repeat(50, 50)
pygame.init()

##
# Game consts
#
FONT = pygame.font.Font(None, 40)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0 ,0, 255)
GRAY  = (100, 100, 100)
MODE_PLAY = 1
MODE_QUIT = 0
FRAME_RATE = 120

##
# Game Vars
#
score_left = 0
score_right = 0
current_mode = MODE_PLAY
BALL_SPEED = 3
pos_x = int(0.5 * WIDTH)
speed_x = BALL_SPEED
pos_y = int(0.5 * HEIGHT)
speed_y = BALL_SPEED
BALL_COLOR = BLACK
BALL_RADIUS = 4
PADDLE_SPEED = 3
PADDLE_HEIGHT = 80
PADDLE_WIDTH = 4
PADDLE_LEFT_COLOR = RED
PADDLE_RIGHT_COLOR = BLUE
PADDLE_LEFT_X = PADDLE_WIDTH + 2
PADDLE_RIGHT_X = WIDTH - (PADDLE_WIDTH + PADDLE_WIDTH + 2)
paddle_left_y = int(0.5 * HEIGHT - 0.5 * PADDLE_HEIGHT)
paddle_right_y = paddle_left_y

def R_moveUp():
    global paddle_right_y, PADDLE_SPEED
    paddle_right_y = paddle_right_y - PADDLE_SPEED
    if paddle_right_y < 0:
        paddle_right_y = 0;

def R_moveDown():
    global paddle_right_y, HEIGHT, PADDLE_HEIGHT, PADDLE_SPEED
    paddle_right_y = paddle_right_y + PADDLE_SPEED
    if paddle_right_y > (HEIGHT - PADDLE_HEIGHT):
        paddle_right_y = HEIGHT - PADDLE_HEIGHT   

def L_moveUp():
    global paddle_left_y, PADDLE_SPEED
    paddle_left_y = paddle_left_y - PADDLE_SPEED
    if paddle_left_y < 0:
        paddle_left_y = 0 

def L_moveDown():
    global paddle_left_y, HEIGHT, PADDLE_HEIGHT, PADDLE_SPEED
    paddle_left_y = paddle_left_y + PADDLE_SPEED
    if paddle_left_y > (HEIGHT - PADDLE_HEIGHT):
        paddle_left_y = HEIGHT - PADDLE_HEIGHT 

def Get_Expected_Hit_Pos():
    global pos_x, pos_y, speed_x, speed_y
    m = speed_y/speed_x
    y = pos_y - m*pos_x
    return y

def Random_Move():
    x = random.randint(0,100)
    if(x%2==0):
        L_moveUp()
    else:
        L_moveDown()

def Ideal_Move():
    global pos_x, pos_y, paddle_left_y

    y = Get_Expected_Hit_Pos()

    if(y<paddle_left_y+0.5*PADDLE_HEIGHT):
        L_moveUp()
    else:
        L_moveDown()    

def Left_Control():
    x = random.randint(0,10000)
    if(x%2==0):
        Ideal_Move()
    else:
        Random_Move()            
##
# Game loop
#
while current_mode == MODE_PLAY:
    ##
    # Handle keyboard
    #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            current_mode = MODE_QUIT
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            current_mode = MODE_QUIT

    keysPressed = pygame.key.get_pressed()
    if keysPressed[pygame.K_UP]:
        R_moveUp()
    elif keysPressed[pygame.K_DOWN]:
        R_moveDown()
    if keysPressed[pygame.K_a]:
        L_moveUp()
    elif keysPressed[pygame.K_z]:
        L_moveDown()
    Left_Control()    

    ##
    # Draw arena and score
    #
    screen.fill(WHITE)
    pygame.draw.line(screen, GRAY, [int(0.5 * WIDTH), 0], [int(0.5 * WIDTH), HEIGHT], 1)
    text = FONT.render("%2s:%2s" % (str(score_left), str(score_right)), 1, GRAY)
    textpos = text.get_rect(centerx=WIDTH/2)
    screen.blit(text, textpos)

    ##
    # Draw paddles
    #
    pygame.draw.rect(screen, PADDLE_LEFT_COLOR, (PADDLE_LEFT_X, paddle_left_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, PADDLE_RIGHT_COLOR, (PADDLE_RIGHT_X, paddle_right_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    ##
    # Move ball and update scores
    #
    pos_x = pos_x + speed_x
    if pos_x > WIDTH:
        if pos_y > (0.5 * HEIGHT):
            speed_y = abs(speed_y)
        else:
            speed_y = -abs(speed_y)
        speed_x *= -1    
        # pos_x = int(0.5 * WIDTH)
        # pos_y = int(0.5 * HEIGHT)
        score_left += 1
    elif pos_x < 0:
        if pos_y > (0.5 * HEIGHT):
            speed_y = abs(speed_y)
        else:
            speed_y = -abs(speed_y)
        speed_x *= -1    
        # pos_x = int(0.5 * WIDTH)
        # pos_y = int(0.5 * HEIGHT)
        score_right += 1
    pos_y = pos_y + speed_y
    if pos_y > HEIGHT:
        speed_y = -speed_y
    elif pos_y < 0:
        speed_y = abs(speed_y)
    pygame.draw.circle(screen, BALL_COLOR, [pos_x, pos_y], BALL_RADIUS)

    ##
    # Bounce ball off paddles
    #
    if pos_x <= (PADDLE_LEFT_X + PADDLE_WIDTH) and pos_y >= paddle_left_y and pos_y <= (paddle_left_y + PADDLE_HEIGHT):
        pos_x = PADDLE_LEFT_X + PADDLE_WIDTH
        speed_x = abs(speed_x)
    elif pos_x >= PADDLE_RIGHT_X and pos_y >= paddle_right_y and pos_y <= (paddle_right_y + PADDLE_HEIGHT):
        pos_x = PADDLE_RIGHT_X
        speed_x = -speed_x

    ##
    # Tick-tock
    #
    pygame.display.update()
    clock.tick(FRAME_RATE)

pygame.quit()
