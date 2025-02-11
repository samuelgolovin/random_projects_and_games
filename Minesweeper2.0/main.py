import pygame
import random

class Cell:
    def __init__(self, i, j, size):
        self.size = size
        self.i = i
        self.j = j
        self.x = i * size
        self.y = j * size
        self.revealed = False
        self.mine = False
        self.num_neighbors = 0
        
        self.text_surface = font.render(str(self.num_neighbors), True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (self.x + self.size // 2, self.y + self.size // 2)



pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")
clock = pygame.time.Clock()
running = True

pygame.font.init()
font = pygame.font.Font(None, 100)

cell_size = 40
cols = WIDTH // cell_size
rows = HEIGHT // cell_size

grid = [[0 for _ in range(cols)] for _ in range(rows)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            WIDTH += 10
            HEIGHT += 10
            screen = pygame.display.set_mode((WIDTH, HEIGHT))

    screen.fill((0, 0, 0))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()