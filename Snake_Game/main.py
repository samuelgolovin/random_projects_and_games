# Example file showing a circle moving on screen
import pygame
import random

from cell import Cell

# pygame setup
pygame.init()
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

w = 50
cols = WIDTH // w
rows = HEIGHT // w

grid = [[0] * cols for _ in range(rows)]

for i in range(cols):
    for j in range(rows):
        grid[i][j] = Cell(i, j, w)

snake_x_start = random.randint(0, 9)
snake_y_start = random.randint(0, 14)

grid[5][5].is_snake_head = True


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    for i in range(cols):
        for j in range(rows):
            pygame.draw.rect(screen, "gray", (grid[i][j].x, grid[i][j].y, grid[i][j].w, grid[i][j].w), 2)
            if grid[i][j].is_snake_head == True:
                pygame.draw.rect(screen, "black", (grid[i][j].x, grid[i][j].y, grid[i][j].w, grid[i][j].w), 2)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()