# main.py
import pygame
import sys
import random
from enemies import Enemies
from player import Player
from healthbar import HealthBar
from shop import Shop
from particle import Particles

# Initialize Pygame
pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 36)

# Set up display variables
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

money = 0
moneyMult = 1

scene = 'game'

# Set up player
player = Player(WIDTH, HEIGHT)

# Set up player health bar
health_bar = HealthBar(10, 10, 200, 20, 100)  # Adjust the position, size, and max health as needed

enemies = Enemies(WIDTH, HEIGHT)

boss_cooldown = 1000
boss_clock = 0

shop = Shop()

particles = Particles()

# Set up clock
clock = pygame.time.Clock()
FPS = 60  # The desired frame rate in frames per second

# Game loop
running = True
while running:
    dt = clock.tick(FPS) / 1000  # Amount of seconds between each loop

    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())  # The mouse's position

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if scene == 'game':
                scene = 'shop'
            elif scene == 'shop':
                scene = 'game'
        for button in shop.buttons:
            if button.mouse_over(mouse_pos):
                if event.type == pygame.MOUSEBUTTONUP:
                    if button.text == 'Attack Damage' and money >= button.cost:
                        player.projectile_damage += 1
                        money -= button.cost
                        button.cost += button.cost // 3 + 1
                    if button.text == 'Speed' and money >= button.cost:
                        player.speed += 10
                        money -= button.cost // 3
                        button.cost += button.cost
                    if button.text == 'Heal' and money >= button.cost and health_bar.current_health < health_bar.max_health:
                        health_bar.current_health += 10
                        money -= button.cost
                        button.cost += button.cost // 10
                    if button.text == 'money mult' and money >= button.cost:
                        moneyMult += 1
                        money -= button.cost
                        button.cost += button.cost // 2
                        


    # Game logic (update game state here)
    

    if scene == 'game':

        player.update(dt, mouse_pos)

        if player.cooldown > player.cooldown_limit and enemies.enemies:
            player.fire_bullet(player.pos, player.closest_enemy(enemies.enemies, player.pos), player.projectile_speed)

        player.update_bullets(dt)

        # Spawn enemies
        if random.random() < 0.01:  # 1% chance per frame
            enemies.spawn_enemy('small', player.pos)
        if random.random() < 0.005:  # 0.5% chance per frame
            enemies.spawn_enemy('big', player.pos)
        if boss_clock >= boss_cooldown:
            boss_clock = 0
            enemies.spawn_enemy('boss', player.pos)
        else:
            boss_clock += 1

        # Update enemies
        enemies.update_enemies(dt)

        # Update healthbar
        health_bar.update()

        # Collision
        for enemy in enemies.enemies:
            if enemy.rect.colliderect(player.rect) and not health_bar.is_invincible():
                health_bar.take_damage(enemy.damage)
            if enemy.healthbar.current_health <= 0:
                if enemy.type == 'small':
                    particles.createParticle(3, enemy.pos, 3, 10, 20)
                elif enemy.type == 'big':
                    particles.createParticle(7, enemy.pos, 5, 10, 20)
                else:
                    particles.createParticle(100, enemy.pos, 10, 10, 20)
                enemies.kill_enemy(enemy)

            for bullet in player.bullets:
                if enemy.rect.colliderect(bullet):
                    enemy.healthbar.current_health = enemy.healthbar.current_health - player.projectile_damage
                    player.bullets.remove(bullet)

        for particle in particles.particles:
            if player.rect.colliderect(particle.rect):
                particles.particles.remove(particle)
                money += 1



        # Drawing/rendering
        screen.fill((0, 0, 0))  # Fill the screen with black

        particles.update_and_draw_particles(screen, player.pos)

        # Draw enemies
        enemies.draw_enemies(screen)

        player.draw(screen, health_bar.is_invincible(), health_bar.timer_for_invincibility)  # Draw the player's circle

        player.draw_bullets(screen)

        health_bar.draw(screen)  # Draw the health bar

        text_surface = font.render('Money: ' + str(money), True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (400, 100)

        screen.blit(text_surface, text_rect)



    elif scene == 'shop':
        screen.fill((50, 50, 50))

        

        text_surface = font.render('Current Stats: ' + str(player.projectile_damage), True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (100, 100)

        screen.blit(text_surface, text_rect)

        text_surface = font.render('Money: ' + str(money), True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (100, 125)

        screen.blit(text_surface, text_rect)

        shop.draw_buttons(screen)



    pygame.display.flip()  # Update the display

# Clean up and quit
pygame.quit()
sys.exit()
