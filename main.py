import pygame
import sys

size = width, height = 680, 680
speed = [2, 2]
black = 0, 0, 0


screen = pygame.display.set_mode(size)
ball = pygame.image.load("src/cock_PNG19930.png")
ball2 = pygame.image.load("src/cock_PNG19930.png")
ballrect = ball.get_rect()
# ballrect2 = ball2.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)
    # ballrect2 = ballrect2.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    # if ballrect2.left < 0 or ballrect2.right > width:
    #     speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    # if ballrect2.top < 0 or ballrect2.left > height:
    #     speed[1] = -speed[1]
    screen.fill(black)
    screen.blit(ball, ballrect)
    # screen.blit(ball2, ballrect2)
    pygame.display.flip()
