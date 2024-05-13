import pygame
from cell import Cell
import random

# pygame setup
pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")
clock = pygame.time.Clock()
running = True

w = 40
cols = WIDTH // w
rows = HEIGHT // w
game_over = False

def create2DArray(i, j):
    arr = [[0 for _ in range(cols)] for _ in range(rows)]
    return arr

def setup_game():

    global grid 
    grid = create2DArray(cols, rows)

    for i in range(cols):
        for j in range(rows):
            grid[i][j] = Cell(i, j, w)

    num_mines = 40

    mine_positions = random.sample(range(cols * rows), num_mines)

    for pos in mine_positions:
        col = pos % cols
        row = pos // cols
        grid[col][row].mine = True

    for i in range(cols):
        for j in range(rows):
            grid[i][j].find_num_neighbors(grid, cols, rows)

setup_game()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i in range(cols):
                for j in range(rows):
                    grid[i][j].mouse_over(mouse_pos[0], mouse_pos[1], grid, cols, rows)
                    if grid[i][j].is_game_over:
                        game_over = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if game_over:
                setup_game()
                game_over = False
    screen.fill((200, 200, 200))
        
    for i in range(cols):
        for j in range(rows):
            grid[i][j].draw(screen)
    

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
