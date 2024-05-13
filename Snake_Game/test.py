import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 40  # Number of rows and columns
CELL_SIZE = WIDTH // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(GRID_SIZE // 2, GRID_SIZE // 2)]  # Initial position
        self.direction = (1, 0)  # Start moving right

    def move(self):
        # Update snake's position based on direction
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        self.body.insert(0, new_head)  # Add new head position

        # Remove the tail segment
        if not self.eat_food(food):
            self.body.pop()

    def check_collision(self):
        # Check if snake hits the wall or itself
        head_x, head_y = self.body[0]
        if (
            head_x < 0
            or head_x >= GRID_SIZE
            or head_y < 0
            or head_y >= GRID_SIZE
            or len(self.body) != len(set(self.body))
        ):
            return True
        return False

    def eat_food(self, food):
        # Check if snake eats food
        head_x, head_y = self.body[0]
        if (head_x, head_y) == food:
            return True
        return False

# Initialize game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
snake = Snake()
food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle user input (arrow keys)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake.direction = (0, -1)
    elif keys[pygame.K_DOWN]:
        snake.direction = (0, 1)
    elif keys[pygame.K_LEFT]:
        snake.direction = (-1, 0)
    elif keys[pygame.K_RIGHT]:
        snake.direction = (1, 0)

    # Move snake
    snake.move()

    # Check collisions
    if snake.check_collision():
        print("Game over!")
        pygame.quit()
        sys.exit()

    # Check if snake eats food
    if snake.eat_food(food):
        food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))

    # Draw grid cells
    screen.fill(BLACK)

    # Draw grid lines
    for i in range(GRID_SIZE):
        pygame.draw.line(screen, GREEN, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT))
        pygame.draw.line(screen, GREEN, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE))

    # Draw snake and food
    for segment in snake.body:
        x, y = segment
        pygame.draw.rect(screen, GREEN, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

    # Limit frame rate
    pygame.time.Clock().tick(10)