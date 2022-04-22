import pygame
import sys

size = width, height = 680, 680
speed = [2, 2]
black = 0, 0, 0


screen = pygame.display.set_mode(size)
cock = pygame.image.load("src/cock_PNG19930.png")
ballrect = cock.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = min(-speed[0] * 3, size[0] * -1 if speed[0] > 0 else 1)

    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = min(-speed[1] * 3, size[0] * -1 if speed[1] > 0 else 1)

    screen.fill(black)
    screen.blit(cock, ballrect)

    pygame.display.flip()
