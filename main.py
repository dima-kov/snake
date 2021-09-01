import random

import pygame
from helpers import message, has_intersect_borders, generate_food, has_intersect_food

# CONSTANTS
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 800

BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

SNAKE_WIDTH, SNAKE_HEIGHT = 10, 10
FOOD_WIDTH, FOOD_HEIGHT = SNAKE_WIDTH, SNAKE_HEIGHT

VELOCITY = 10

# VARIABLES
X = 200
Y = 150

X_APPEND = 0
Y_APPEND = 0

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
game_run = True
game_end = False
game_before_init = True

while game_run:
    while game_end is True:
        message(dis, font_style, "The end. Press C to continue or Q to exit", RED)
        pygame.display.update()

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    game_end = False
                    game_run = True
                    X = 200
                    Y = 150
                    X_APPEND = 0
                    Y_APPEND = 0

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

    if has_intersect_food(
            X, Y,
            X_APPEND, Y_APPEND,
            SNAKE_WIDTH, SNAKE_HEIGHT,
            FOOD_X, FOOD_Y,
            FOOD_WIDTH, FOOD_HEIGHT
    ):
        FOOD_X, FOOD_Y = generate_food(WINDOW_WIDTH, WINDOW_HEIGHT, SNAKE_WIDTH, SNAKE_HEIGHT)

    X += X_APPEND
    Y += Y_APPEND

    # Draw on frame
    dis.fill(WHITE)
    pygame.draw.rect(dis, BLUE, [X, Y, SNAKE_WIDTH, SNAKE_HEIGHT])
    if FOOD_X is not None and FOOD_Y is not None:
        pygame.draw.rect(dis, BLUE, [FOOD_X, FOOD_Y, FOOD_WIDTH, FOOD_HEIGHT])

    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()
