import pygame
import random

class Enemy:
    def __init__(self, x, y, width, height, velocity, health, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity = velocity
        self.speed = speed
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def move_enemy(self, dt):
        self.rect.update(self.rect.x, self.rect.y, self.rect.width, self.rect.height)

        # Update the self's position
        self.rect.center += self.velocity * dt

    def set_target(self, target):
        # Calculate the direction vector to the target
        target = pygame.Vector2(target)
        direction = target - pygame.Vector2(x, y)

        # Normalize the direction vector and multiply by the enemy's speed to get the velocity
        self.velocity = direction.normalize() * self.speed
    

    def update(self, surface, dt):
        self.move_enemy(dt)
        self.draw(surface)

class Enemies:
    def __init__(self, time_of_attack, time_between_attacks, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.enemies = []
        self.time_of_attack = time_of_attack
        self.time_between_attacks = time_between_attacks

    def spawn_enemy(self, target, width, height, speed, health):
        # Spawn offscreen
        side = random.choice(['top', 'bottom', 'left', 'right'])
        if side == 'top':
            x = random.uniform(0, self.screen_width)
            y = -10  # 10 units above the screen
        elif side == 'bottom':
            x = random.uniform(0, self.screen_width)
            y = self.screen_height + 10  # 10 units below the screen
        elif side == 'left':
            x = -10  # 10 units to the left of the screen
            y = random.uniform(0, self.screen_height)
        else:  # 'right'
            x = self.screen_width + 10  # 10 units to the right of the screen
            y = random.uniform(0, self.screen_height)

        # Calculate the direction vector to the target
        target = pygame.Vector2(target)
        direction = target - pygame.Vector2(x, y)

        # Normalize the direction vector and multiply by the enemy's speed to get the velocity
        velocity = direction.normalize() * speed

        enemy = Enemy(x, y, width, height, velocity, health, speed)
        self.enemies.append(enemy)

    def damage_enemy(self, enemy, damage):
        enemy.health -= damage
        if enemy.health <= 0:
            self.kill_enemy(enemy)

    def kill_enemy(self, enemy):
        self.enemies.remove(enemy)

    def update_enemies(self, surface, dt):
        for enemy in self.enemies:
            enemy.update(surface, dt)
            
            if enemy.rect.centerx > self.screen_width + 20 or enemy.rect.centerx < -20 or enemy.rect.centery > self.screen_height + 20 or enemy.rect.centery < -20:
                self.enemies.remove(enemy)