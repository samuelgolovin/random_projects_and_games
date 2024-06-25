import pygame
import random

class Enemy:
    def __init__(self, x, y, width, height, velocity, health, speed, color, target):
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity = velocity
        self.speed = speed
        self.health = health
        self.color = color

        self.target = target
    
        self.location = self.rect.center

    def draw(self, surface, offset_x, offset_y):
        self.location = (self.rect.centerx + offset_x, self.rect.centery + offset_y)
        pygame.draw.rect(surface, self.color, ((self.location[0] - self.rect.width / 2, self.location[1] - self.rect.height / 2), self.rect.size))

    def move_enemy(self, dt):
        direction = self.target - self.rect.center

        # Normalize the direction vector and multiply by the enemy's speed to get the velocity
        self.velocity = direction.normalize() * self.speed

        # Update the self's position
        self.rect.center += self.velocity * dt


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
        direction = target - pygame.Vector2(x + width / 2, y + height / 2)

        # Normalize the direction vector and multiply by the enemy's speed to get the velocity
        velocity = direction.normalize() * speed

        self.enemies.append(Enemy(x, y, width, height, velocity, health, speed, 'black', target))

    def damage_enemy(self, enemy, damage):
        enemy.health -= damage
        if enemy.health <= 0:
            self.kill_enemy(enemy)

    def kill_enemy(self, enemy):
        self.enemies.remove(enemy)

    def check_if_target_hit(self, enemy):
        if enemy.rect.collidepoint(enemy.target):
            self.kill_enemy(enemy)

    def update_enemies(self, dt):
        for enemy in self.enemies:
            if enemy.rect.centerx > self.screen_width + 20 or enemy.rect.centerx < -20 or enemy.rect.centery > self.screen_height + 20 or enemy.rect.centery < -20:
                self.kill_enemy(enemy)

            self.check_if_target_hit(enemy)

            enemy.move_enemy(dt)
            
            