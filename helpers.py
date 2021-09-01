import random


def message(dis, font_style, msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [30, 30])


def has_intersect_borders(window_width, window_height, x, y, snake_width, snake_height) -> bool:
    if y <= 0:
        return True
    elif y >= window_height - snake_height:
        return True
    elif x <= 0:
        return True
    elif x >= window_width - snake_width:
        return True
    return False


def has_intersect_food(snake_x, snake_y,
                       snake_x_append, snake_y_append,
                       snake_width, snake_height,
                       food_x, food_y,
                       food_width, food_height) -> bool:
    if food_x is None or food_y is None:
        return False

    if (snake_x + snake_width == food_x) and (snake_y == food_y) and snake_x_append:
        return True  # left side
    if (snake_x == food_x) and (snake_y + snake_height == food_y) and snake_y_append:
        return True  # top side

    if (snake_x == food_x + food_width) and (snake_y == food_y) and snake_x_append:
        return True  # right side

    if (snake_x == food_x) and (snake_y == food_y + food_height) and snake_y_append:
        return True  # bottom side

    return False


def generate_food(window_width, window_height, snake_width, snake_height):
    return (
        (round(random.randrange(0, window_width - snake_width) / 10.0) * 10.0),
        (round(random.randrange(0, window_height - snake_height) / 10.0) * 10.0)
    )
