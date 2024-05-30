import pygame
import sys
import math
import random

from enemies import Enemies

# Initialize Pygame
pygame.init()

# Set up display variables
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up player variables
player_radius = 20  # The radius of the player's circle
player_color = (255, 255, 255)  # The color of the player's circle (white)
player_speed = 0.1  # The speed of the player's circle
player_pos = [WIDTH // 2, HEIGHT // 2]  # The initial position of the player's circle

enemies = Enemies(WIDTH, HEIGHT)

# Set up clock
clock = pygame.time.Clock()
FPS = 60  # The desired frame rate in frames per second

# Game loop
running = True
while running:
    dt = clock.tick(FPS) / 1000  # Amount of seconds between each loop
    player_speed = 300 * dt  # The player's speed in pixels per second

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic (update game state here)
    mouse_pos = pygame.mouse.get_pos()  # The mouse's position
    dx, dy = mouse_pos[0] - player_pos[0], mouse_pos[1] - player_pos[1]
    angle = math.atan2(dy, dx)
    player_pos[0] += player_speed * math.cos(angle)
    player_pos[1] += player_speed * math.sin(angle)

    # Spawn enemies
    if random.random() < 0.01:  # 1% chance per frame
        enemies.spawn_enemy('small')
    if random.random() < 0.005:  # 0.5% chance per frame
        enemies.spawn_enemy('big')

    # Update enemies
    enemies.update_enemies(player_pos, dt)

    # Drawing/rendering
    screen.fill((0, 0, 0))  # Fill the screen with black
    pygame.draw.circle(screen, player_color, (int(player_pos[0]), int(player_pos[1])), player_radius)  # Draw the player's circle

    # Draw enemies
    enemies.draw_enemies(screen)

    pygame.display.flip()  # Update the display

# Clean up and quit
pygame.quit()
sys.exit()
