# Example file showing a circle moving on screen
import pygame
import random

from snake import Snake

# pygame setup
pygame.init()
# keep the following width and height the same
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

w = 20
cols = WIDTH // w
rows = HEIGHT // w

def setup():
    global snake
    global food
    snake = Snake(cols, rows)
    food = (random.randint(0, cols - 1), random.randint(0, rows - 1))

setup()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and not snake.dir == (0, 1):
        snake.dir = (0, -1)
    if keys[pygame.K_s] and not snake.dir == (0, -1):
        snake.dir = (0, 1)
    if keys[pygame.K_a] and not snake.dir == (1, 0):
        snake.dir = (-1, 0)
    if keys[pygame.K_d] and not snake.dir == (-1, 0):
        snake.dir = (1, 0)
    
    snake.move(food)

    if snake.check_collision(cols, rows):
        setup()

    if snake.eat_food(food):
        food = (random.randint(0, cols - 1), random.randint(0, rows - 1))

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    for i in range(cols):
        for j in range(rows):
            pygame.draw.rect(screen, "gray", (i * w, j * w, w, w), 2)
            if (i, j) in snake.body:
                pygame.draw.rect(screen, "black", (i * w, j * w, w, w))
            elif (i, j) == food:
                pygame.draw.rect(screen, "red", (i * w, j * w, w, w))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(10) / 1000

pygame.quit()