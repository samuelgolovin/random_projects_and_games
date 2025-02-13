import pygame
import random


class Cell:
    def __init__(self, i, j, size, temp_value):
        self.size = size
        self.i = i
        self.j = j
        self.x = j * size
        self.y = i * size
        self.rect = pygame.Rect(self.x, self.y, size, size)
        self.revealed = False
        self.mine = False
        self.num_neighbors = 0
        # for revealing all zeroes when using a queue
        self.visited = False

        # self.temp_value = temp_value
        
        # self.text_surface = font.render("(" + str(self.i) + "," + str(self.j) + ")", True, (0, 0, 0))
        # self.text_surface = font.render(str(self.temp_value), True, (0, 0, 0))
        self.text_surface = font.render(str(self.num_neighbors), True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (self.x + self.size // 2, self.y + self.size // 2)

    def update_text(self):
        self.text_surface = font.render(str(self.num_neighbors), True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (self.x + self.size // 2, self.y + self.size // 2)



pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("test")
clock = pygame.time.Clock()
running = True

game_started = False


pygame.font.init()
font = pygame.font.Font(None, 24)

cell_size = 40
rows = 8
cols = 10

game_surface = pygame.Surface((cols * cell_size, rows * cell_size))
game_surface_rect = game_surface.get_rect(center = (WIDTH // 2, HEIGHT // 2))

grid = [[0 for _ in range(cols)] for _ in range(rows)]

# print(grid)

temp_value = 0

for i in range(rows):
    for j in range(cols):
        grid[i][j] = Cell(i, j, cell_size, temp_value)
        temp_value += 1

num_of_mines = 10

mine_positions = random.sample(range(rows * cols), num_of_mines)

for pos in mine_positions:
    row = pos // cols
    col = pos % cols
    grid[row][col].mine = True

def find_num_neighbors(cell):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            neighbor_x = cell.i + i
            neighbor_y = cell.j + j

            if 0 <= neighbor_x < rows and 0 <= neighbor_y < cols:
                if grid[neighbor_x][neighbor_y].mine:
                    cell.num_neighbors += 1
                    cell.update_text()

for i in range(rows):
    for j in range(cols):
        find_num_neighbors(grid[i][j])

def reveal_all_cells():
    for i in range(rows):
        for j in range(cols):
            grid[i][j].revealed = True


def reveal_cell(cell):
    if cell.mine:
        reveal_all_cells()
        return

    if cell.num_neighbors > 0:
        cell.revealed = True
        return


    queue = [cell]

    while queue:
        element = queue.pop(0)
        element.revealed = True
        # element.visited = True
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue

                neighbor_x = element.i + i
                neighbor_y = element.j + j

                if 0 <= neighbor_x < rows and 0 <= neighbor_y < cols:
                    neighbor = grid[neighbor_x][neighbor_y]

                    if not neighbor.mine and not neighbor.revealed:
                        neighbor.revealed = True
                        # neighbor.visited = True

                        if neighbor.num_neighbors == 0:
                            queue.append(neighbor)

def random_sample_excluding(range_start, range_end, exclude_set, sample_size):
    # Create a set of all numbers in the specified range
    all_numbers = set(range(range_start, range_end))
    
    # Subtract the exclude_set from all_numbers
    available_numbers = list(all_numbers - exclude_set)
    
    # Randomly sample from the available numbers
    sample = random.sample(available_numbers, sample_size)
    
    return sample

def start_new_game(cell):
    for i in range(rows):
        for j in range(cols):
            element = grid[i][j]
            element.revealed = False
            element.mine = False
            element.num_neighbors = 0

    # find linear position from cell coordinates
    starting_set = set()
    starting_set.add(cell.i * cols + cell.j)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            
            neighbor_x = cell.i - i
            neighbor_y = cell.j - j

            neighbor = grid[neighbor_x][neighbor_y]
            starting_set.add(neighbor.i * cols + neighbor.j)

    # set mine positions and put them on the board
    num_of_mines = 10

    mine_positions = random_sample_excluding(0, (rows * cols), starting_set, num_of_mines)
    
    for pos in mine_positions:
        row = pos // cols
        col = pos % cols
        grid[row][col].mine = True

    # find all neighbors code
    for i in range(rows):
        for j in range(cols):
            find_num_neighbors(grid[i][j])
    
    reveal_cell(cell)
    
    global game_started
    game_started = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i in range(rows):
                for j in range(cols):
                    cell = grid[i][j]
                    if cell.rect.collidepoint((mouse_pos[0] - game_surface_rect.x, mouse_pos[1] - game_surface_rect.y)):
                        if game_started:
                            reveal_cell(cell)
                        else:
                            start_new_game(cell)

    screen.fill((50, 50, 0))
    game_surface.fill((100, 100, 100))

    for i in range(rows):
        for j in range(cols):
            cell = grid[i][j]
            if cell.revealed:
                if cell.mine:
                    pygame.draw.rect(game_surface, (200, 0, 0), cell.rect, cell.size // 10)
                else:
                    pygame.draw.rect(game_surface, (0, 0, 0), cell.rect, cell.size // 10)
                    game_surface.blit(cell.text_surface, cell.text_rect)
            else:
                pygame.draw.rect(game_surface, (30, 30, 30), cell.rect, cell.size // 10)
    
    screen.blit(game_surface, game_surface_rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
