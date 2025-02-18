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
pygame.font.init()
font = pygame.font.Font(None, 100)

w = 35
cols = WIDTH // w
rows = HEIGHT // w
game_over = False
game_won = False

win_text_surface = font.render("You Won!", True, (20, 20, 20))
win_text_rect = win_text_surface.get_rect()
win_text_rect.center = (WIDTH // 2, HEIGHT // 2)

lose_text_surface = font.render("You Lose!", True, (20, 20, 20))
lose_text_rect = lose_text_surface.get_rect()
lose_text_rect.center = (WIDTH //2, HEIGHT // 2)

def create2DArray(i, j):
    arr = [[0 for _ in range(cols)] for _ in range(rows)]
    return arr

def check_if_done():
    for i in range(cols):
        for j in range(rows):
            cell = grid[i][j]
            if not cell.mine and not cell.revealed:
                return False
    return True

def set_game_over():
    print("this happens")
    for i in range(cols):
        for j in range(rows):
            grid[i][j].revealed = True

def setup_game():

    global grid 
    grid = create2DArray(cols, rows)

    for i in range(cols):
        for j in range(rows):
            grid[i][j] = Cell(i, j, w)

    num_mines = 35

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
            if check_if_done() and not game_over:
                game_won = True
                game_over = True
                set_game_over()
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if game_over:
                setup_game()
                game_over = False
                game_won = False
    screen.fill((200, 200, 200))
        
    for i in range(cols):
        for j in range(rows):
            grid[i][j].draw(screen)

    if game_won:
        screen.blit(win_text_surface, win_text_rect)
    if game_over and not game_won:
        screen.blit(lose_text_surface, lose_text_rect)
    

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

