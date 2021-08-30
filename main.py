import pygame

pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption('Snake Game!')

game_run = True
while game_run:
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            game_run = False


pygame.quit()
quit()
