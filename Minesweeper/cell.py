import pygame
from collections import deque

pygame.font.init()

font = pygame.font.Font(None, 36)

class Cell:
    def __init__(self, i, j, w):
        self.w = w
        self.i = i
        self.j = j
        self.x = self.i * w
        self.y = self.j * w
        self.revealed = False
        self.mine = False
        self.num_neighbors = 0
        self.is_game_over = False

        self.text_surface = font.render(str(self.num_neighbors), True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (self.x + self.w / 2, self.y + self.w / 2)

    def update(self):
        self.text_surface = font.render(str(self.num_neighbors), True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (self.x + self.w / 2, self.y + self.w / 2)

    def mouse_over(self, mouse_x, mouse_y, grid, cols, rows):
        if self.x + self.w > mouse_x > self.x and self.y + self.w > mouse_y > self.y:
            if not self.revealed:
                self.revealed = True
                if self.mine:
                    self.game_over(grid, cols, rows)
            if self.num_neighbors == 0 and not self.mine:
                self.reveal_zeros(grid, cols, rows)
                

    def reveal_zeros(self, grid, cols, rows):
        self.revealed = True
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                
                neighbor_x = self.i + i
                neighbor_y = self.j + j

                if 0 <= neighbor_x < cols and 0 <= neighbor_y < rows:
                    if not grid[neighbor_x][neighbor_y].revealed:
                        if not grid[neighbor_x][neighbor_y].revealed:
                            grid[neighbor_x][neighbor_y].revealed = True
                        if grid[neighbor_x][neighbor_y].num_neighbors == 0 and not grid[neighbor_x][neighbor_y].mine:
                            grid[neighbor_x][neighbor_y].reveal_zeros(grid, cols, rows)

    def game_over(self, grid, cols, rows):
        self.is_game_over = True
        for i in range(cols):
            for j in range(rows):
                grid[i][j].revealed = True
    
    def draw(self, surface):
        pygame.draw.rect(surface, (80, 80, 80), (self.x, self.y, self.w, self.w), 2)
        if self.revealed:
            if self.mine:
                pygame.draw.circle(surface, (120, 120, 120), (self.x + self.w / 2, self.y + self.w / 2), self.w / 4)
            elif self.num_neighbors > -1:
                surface.blit(self.text_surface, self.text_rect)

    def find_num_neighbors(self, grid, cols, rows):
        for i in range(-1, 2):
            for j in range(-1, 2):

                # The code below is me sorting out how to do this all step by step
                # The later code is how ChatGPT said to do it and it is basically the
                # the same, but with a lot less steps

                # if self.i > 0 and self.i < 9 and self.j > 0 and self.j < 9:
                #     if grid[self.i + i][self.j + j].mine:
                #         self.num_neighbors += 1
                #         self.update()
                # elif self.i == 0 and self.j == 0 and i > -1 and j > -1:
                #     if grid[self.i + i][self.j + j].mine:
                #         self.num_neighbors += 1
                #         self.update()
                # elif self.i == 0 and self.j == rows - 1 and i > -1 and j < 1:
                #     if grid[self.i + i][self.j + j].mine:
                #         self.num_neighbors += 1
                #         self.update()
                # elif self.i == cols - 1 and self.j == rows - 1 and i < 1 and j < 1:
                #     if grid[self.i + i][self.j + j].mine:
                #         self.num_neighbors += 1
                #         self.update()
                # elif self.i == cols - 1 and self.j == 0 and i < 1 and j > -1:
                #     if grid[self.i + i][self.j + j].mine:
                #         self.num_neighbors += 1
                #         self.update()
                # elif self.i == 0 and not self.j == 0 and not self.j == rows - 1 and i > -1:
                #     if grid[self.i + i][self.j + j].mine:
                #         self.num_neighbors += 1
                #         self.update()
                # elif self.i == cols - 1 and not self.j == 0 and not self.j == rows - 1 and i < 1:
                #     if grid[self.i + i][self.j + j].mine:
                #         self.num_neighbors += 1
                #         self.update()
                # elif self.j == 0 and not self.i == 0 and not self.i == cols - 1 and j > -1:
                #     if grid[self.i + i][self.j + j].mine:
                #         self.num_neighbors += 1
                #         self.update()
                # elif self.j == rows - 1 and not self.i == 0 and not self.i == cols - 1 and j < 1:
                #     if grid[self.i + i][self.j + j].mine:
                #         self.num_neighbors += 1
                #         self.update()

                # ChatGPT's code that I implemented eliminate the above (my) code

                if i == 0 and j == 0:
                    continue
                
                neighbor_x = self.i + i
                neighbor_y = self.j + j

                if 0 <= neighbor_x < cols and 0 <= neighbor_y < rows:
                    if grid[neighbor_x][neighbor_y].mine:
                        self.num_neighbors += 1

        self.update()