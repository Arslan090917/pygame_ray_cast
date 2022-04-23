import random
import sys

import pygame

size = width, height = 680, 680
black = 0, 0, 0
amp = 3

screen = pygame.display.set_mode(size)

cock = pygame.image.load("src/cock_PNG19930.png")
cockrect = cock.get_rect()
cock_speed = [3, 2]

clock = pygame.time.Clock()
fill_color = black
balls = []


def change_speed(rect, speed: list) -> list:
    """Change speed for any rect/speed pair.

    Args:
        rect (_type_): position
        speed (list): prev speed

    Returns:
        list: new speed
    """
    if rect.left < 0 or rect.right > width:
        amp_cap = size[0] * random.choice([1 / 2, 6 / 10])
        direction = 1 if speed[0] > 0 else -1
        speed[0] = min(abs(speed[0]) * amp, amp_cap) * direction * -1

    if rect.top < 0 or rect.bottom > height:
        amp_cap = size[1] * random.choice([1 / 2, 6 / 10])
        direction = 1 if speed[1] > 0 else -1
        speed[1] = min(abs(speed[1]) * amp, amp_cap) * direction * -1

    return speed


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    cockrect = cockrect.move(cock_speed)
    cock_speed = change_speed(cockrect, cock_speed)

    if any(i > size[0] * 1 / 2 for i in cock_speed):
        if random.randint(1, 100) <= 25:
            print("Drop ball!")
            _ball = pygame.image.load("src/intro_ball.gif")
            balls.append(
                {
                    "ball": _ball,
                    "rect": _ball.get_rect(),
                    "speed": [random.randint(50, 150), random.randint(50, 300)],
                }
            )
        fill_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )

    screen.fill(fill_color)

    for this_ball in balls:
        this_ball["rect"] = this_ball["rect"].move(this_ball["speed"])
        this_ball["speed"] = change_speed(this_ball["rect"], this_ball["speed"])

        print(this_ball["ball"], this_ball["rect"])
        screen.blit(this_ball["ball"], this_ball["rect"])

    screen.blit(cock, cockrect)

    pygame.display.flip()
    clock.tick(25)
