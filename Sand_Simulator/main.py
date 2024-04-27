import pygame
import math
import random
import colorsys

# pygame setup
pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

hue = 0.5  # Hue ranges from 0 to 1
brightness = 1
saturation = 1

def make_2D_array(rows, cols):
    arr = []
    for _ in range(rows):
        arr.append([0] * cols)
    return arr

def setup():
    rows = WIDTH // w
    cols = HEIGHT // w
    grid = make_2D_array(rows, cols)
    return grid, rows, cols

def update_grid(grid, rows, cols):
    nextGrid = make_2D_array(rows, cols)
    for i in range(rows):
        for j in range(cols):
            state = grid[i][j]
            if state > 0:
                if j < cols - 1:  # Ensure within bounds
                    below = grid[i][j + 1]

                    dir = random.choice([-1, 1])

                    belowA, belowB = 1, 1

                    if i + dir >= 0 and i + dir <= rows - 1:
                        belowA = grid[i + dir][j + 1]
                    if i - dir >= 0 and i - dir <= rows - 1:
                        belowB = grid[i - dir][j + 1]

                    if below == 0:
                        nextGrid[i][j + 1] = grid[i][j]
                    elif belowA == 0:
                        nextGrid[i + dir][j + 1] = grid[i][j]
                    elif belowB == 0:
                        nextGrid[i - dir][j + 1] = grid[i][j]
                    else:
                        nextGrid[i][j] = grid[i][j]
                else:
                    nextGrid[i][j] = grid[i][j]  # Sand stays at bottom row
    return nextGrid

w = 10 # make smaller to make the sand finer, but not too small as it runs slower
grid, rows, cols = setup()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouseRow = math.floor(mouse_x / w)
            mouseCol = math.floor(mouse_y / w)
            
            matrix = 3 #size of the sand spout around the mouse
            extent = math.floor(matrix / 2)
            for i in range(-extent, extent):
                for j in range(-extent, extent):
                    if random.random() < 0.75:
                        row = mouseRow + i
                        col = mouseCol + j
                        if row >= 0 and row <= rows - 1 and col >= 0 and col <= cols - 1:
                            grid[row][col] = hue
            hue += 0.001

    screen.fill((0, 0, 0))

    for i in range(rows):
        for j in range(cols):
            x = i * w
            y = j * w
            if grid[i][j] > 0:
                # Convert HSB to RGB
                rgb_tuple = colorsys.hsv_to_rgb(grid[i][j], saturation, brightness)
                rgb_color = [int(val * 255) for val in rgb_tuple]  # Convert to 0-255 range
                pygame.draw.rect(screen, rgb_color, (x, y, w, w))

    grid = update_grid(grid, rows, cols)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
