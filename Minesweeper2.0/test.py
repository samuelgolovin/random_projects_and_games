import pygame
import random


class Cell:
    def __init__(self, i, j, size, temp_value):
        self.size = size
        self.i = i
        self.j = j
        self.x = j * size
        self.y = i * size
        self.revealed = False
        self.mine = False
        self.num_neighbors = 0

        self.temp_value = temp_value
        
        # self.text_surface = font.render("(" + str(self.i) + "," + str(self.j) + ")", True, (0, 0, 0))
        self.text_surface = font.render(str(self.temp_value), True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (self.x + self.size // 2, self.y + self.size // 2)




pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("test")
clock = pygame.time.Clock()
running = True


game_surface = pygame.Surface((300, 400))
game_surface_rect = game_surface.get_rect(center = (WIDTH // 2, HEIGHT // 2))


pygame.font.init()
font = pygame.font.Font(None, 24)

cell_width = 50
rows = 5
cols = 4

grid = [[0 for _ in range(cols)] for _ in range(rows)]

print(grid)

temp_value = 0

for i in range(rows):
    for j in range(cols):
        grid[i][j] = Cell(i, j, cell_width, temp_value)
        temp_value += 1

# num_of_mines = 5

# mine_positions = random.sample(range(rows * cols), num_of_mines)

# for pos in mine_positions:
#     row = pos // cols
#     col = pos % cols
#     grid[row][col].mine = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((50, 50, 0))
    game_surface.fill((100, 100, 100))

    for i in range(rows):
        for j in range(cols):
            cell = grid[i][j]
            if cell.mine:
                pygame.draw.rect(screen, (200, 0, 0), (cell.x, cell.y, cell.size, cell.size), 5)
            else:
                pygame.draw.rect(game_surface, (0, 0, 0), (cell.x, cell.y, cell.size, cell.size), 5)
                game_surface.blit(cell.text_surface, cell.text_rect)
    
    screen.blit(game_surface, game_surface_rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
