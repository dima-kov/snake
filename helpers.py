def message(dis, font_style, msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [30, 30])


def has_intersects(window_width, window_height, x, y, snake_width, snake_height) -> bool:
    if y <= 0:
        return True
    elif y >= window_height - snake_height:
        return True
    elif x <= 0:
        return True
    elif x >= window_width - snake_width:
        return True
    return False
