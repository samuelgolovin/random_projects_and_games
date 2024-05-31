# main.py
import pygame
import sys
import random
from enemies import Enemies
from player import Player

# Initialize Pygame
pygame.init()

# Set up display variables
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up player
player = Player(WIDTH // 2, HEIGHT // 2)

enemies = Enemies(WIDTH, HEIGHT)

# Set up clock
clock = pygame.time.Clock()
FPS = 60  # The desired frame rate in frames per second

# Game loop
running = True
while running:
    dt = clock.tick(FPS) / 1000  # Amount of seconds between each loop

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic (update game state here)
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())  # The mouse's position
    player.update(dt, mouse_pos)

    # Spawn enemies
    if random.random() < 0.01:  # 1% chance per frame
        enemies.spawn_enemy('small', player.pos)
    if random.random() < 0.005:  # 0.5% chance per frame
        enemies.spawn_enemy('big', player.pos)

    # Update enemies
    enemies.update_enemies(dt)

    # Drawing/rendering
    screen.fill((0, 0, 0))  # Fill the screen with black
    player.draw(screen)  # Draw the player's circle

    # Draw enemies
    enemies.draw_enemies(screen)

    pygame.display.flip()  # Update the display

# Clean up and quit
pygame.quit()
sys.exit()
