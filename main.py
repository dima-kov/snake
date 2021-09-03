import random

import pygame
from helpers import message, has_intersect_borders, generate_food, has_intersect_food, snake_intersects_block, \
    snake_intersects_itself

# CONSTANTS
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 800

BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SNAKE_WIDTH, SNAKE_HEIGHT = 10, 10
FOOD_WIDTH, FOOD_HEIGHT = SNAKE_WIDTH, SNAKE_HEIGHT

VELOCITY = 10

# VARIABLES
X = 200
Y = 150

SNAKE = [[X, Y]]

X_APPEND = 0
Y_APPEND = 0
SCORE = 0

FOOD_X = None
FOOD_Y = None
# start
pygame.init()
dis = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.update()
pygame.display.set_caption('Snake Game!')
pygame.font.init()

clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)
font_style_score = pygame.font.SysFont(None, 24)
game_run = True
game_end = False
game_before_init = True
new_head = False

def direction_x_by_append(x_append, y_append):
    return True if x_append else False


while game_run:
    dis.fill(WHITE)
    message(dis, font_style_score, f"Score: {SCORE}", BLACK)
    while game_end is True:
        message(dis, font_style, "The end. Press C to continue or Q to exit", RED)
        pygame.display.update()

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                game_run = False
                game_end = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    game_end = False
                    game_run = True
                    X = 200
                    Y = 150
                    X_APPEND = 0
                    Y_APPEND = 0
                    SNAKE = [[X, Y]]

                if event.key == pygame.K_q:
                    game_end = False
                    game_run = False

    for event in pygame.event.get():
        # print(event)

        if event.type == pygame.QUIT:
            game_run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                X_APPEND = -VELOCITY
                Y_APPEND = 0
                if game_before_init:
                    FOOD_X, FOOD_Y = generate_food(WINDOW_WIDTH, WINDOW_HEIGHT, SNAKE_WIDTH, SNAKE_HEIGHT)
                    game_before_init = False

            elif event.key == pygame.K_RIGHT:
                X_APPEND = VELOCITY
                Y_APPEND = 0

                if game_before_init:
                    FOOD_X, FOOD_Y = generate_food(WINDOW_WIDTH, WINDOW_HEIGHT, SNAKE_WIDTH, SNAKE_HEIGHT)
                    game_before_init = False

            elif event.key == pygame.K_UP:
                X_APPEND = 0
                Y_APPEND = -VELOCITY

                if game_before_init:
                    FOOD_X, FOOD_Y = generate_food(WINDOW_WIDTH, WINDOW_HEIGHT, SNAKE_WIDTH, SNAKE_HEIGHT)
                    game_before_init = False

            elif event.key == pygame.K_DOWN:
                X_APPEND = 0
                Y_APPEND = VELOCITY

                if game_before_init:
                    FOOD_X, FOOD_Y = generate_food(WINDOW_WIDTH, WINDOW_HEIGHT, SNAKE_WIDTH, SNAKE_HEIGHT)
                    game_before_init = False

    if has_intersect_borders(WINDOW_WIDTH, WINDOW_HEIGHT, X, Y, SNAKE_WIDTH, SNAKE_HEIGHT):
        game_end = True

    if snake_intersects_block(
            X, Y,
            SNAKE_WIDTH, SNAKE_HEIGHT,
            direction_x_by_append(X_APPEND, Y_APPEND),
            FOOD_X, FOOD_Y,
            FOOD_WIDTH, FOOD_HEIGHT,
    ):
        FOOD_X, FOOD_Y = generate_food(WINDOW_WIDTH, WINDOW_HEIGHT, SNAKE_WIDTH, SNAKE_HEIGHT)
        new_head = True
        SCORE += 1

    X += X_APPEND
    Y += Y_APPEND

    snake_head = [X, Y]
    SNAKE.append(snake_head)

    if len(SNAKE) > 1:
        del SNAKE[0]

    if new_head:
        X += X_APPEND
        Y += Y_APPEND
        SNAKE.append([X, Y])
        new_head = False

    if snake_intersects_itself(SNAKE):
        print('INTERSECTS')
        game_end = True

    if FOOD_X is not None and FOOD_Y is not None:
        pygame.draw.rect(dis, BLUE, [FOOD_X, FOOD_Y, FOOD_WIDTH, FOOD_HEIGHT])

    for coord_block in SNAKE:
        pygame.draw.rect(dis, BLUE, [coord_block[0], coord_block[1], SNAKE_WIDTH, SNAKE_HEIGHT])

    pygame.display.update()

    clock.tick(10)

pygame.quit()
quit()
