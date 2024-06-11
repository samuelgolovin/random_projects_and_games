# main.py
import pygame
import sys
import random
from enemies import Enemies
from player import Player
from healthbar import HealthBar

# Initialize Pygame
pygame.init()

# Set up display variables
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up player
player = Player(WIDTH, HEIGHT)

# Set up health bar
health_bar = HealthBar(10, 10, 200, 20, 100)  # Adjust the position, size, and max health as needed

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            health_bar.current_health = 100

    # Game logic (update game state here)
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())  # The mouse's position
    player.update(dt, mouse_pos)

    if player.cooldown > player.cooldown_limit:
        for enemy in enemies.enemies:
            player.fire_bullet(player.pos, enemy.pos, player.projectile_speed)

    player.update_bullets(dt)

    # Spawn enemies
    if random.random() < 0.01:  # 1% chance per frame
        enemies.spawn_enemy('small', player.pos)
    if random.random() < 0.005:  # 0.5% chance per frame
        enemies.spawn_enemy('big', player.pos)

    # Update enemies
    enemies.update_enemies(dt)

    # Update healthbar
    health_bar.update()

    # Collision
    for enemy in enemies.enemies:
        if enemy.rect.colliderect(player.rect) and not health_bar.is_invincible():
            health_bar.take_damage(enemy.damage)

    # Drawing/rendering
    screen.fill((0, 0, 0))  # Fill the screen with black

    # Draw enemies
    enemies.draw_enemies(screen)

    player.draw(screen, health_bar.is_invincible(), health_bar.timer_for_invincibility)  # Draw the player's circle

    player.draw_bullets(screen)

    health_bar.draw(screen)  # Draw the health bar

    pygame.display.flip()  # Update the display

# Clean up and quit
pygame.quit()
sys.exit()
