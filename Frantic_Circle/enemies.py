import pygame
import random

class Enemy:
    def __init__(self, type, pos, speed, velocity):
        self.type = type
        self.pos = pygame.Vector2(pos)
        self.speed = speed
        self.velocity = velocity

class Enemies:
    def __init__(self, width, height):
        self.enemies = []
        self.width = width
        self.height = height

    def spawn_enemy(self, type, player_pos):
        # Spawn offscreen
        side = random.choice(['top', 'bottom', 'left', 'right'])
        if side == 'top':
            x = random.uniform(0, self.width)
            y = -10  # 10 units above the screen
        elif side == 'bottom':
            x = random.uniform(0, self.width)
            y = self.height + 10  # 10 units below the screen
        elif side == 'left':
            x = -10  # 10 units to the left of the screen
            y = random.uniform(0, self.height)
        else:  # 'right'
            x = self.width + 10  # 10 units to the right of the screen
            y = random.uniform(0, self.height)

        speed = random.uniform(50, 150) if type == 'small' else random.uniform(20, 80)

        # Calculate the direction vector to the target
        target = pygame.Vector2(player_pos)
        direction = target - pygame.Vector2(x, y)

        # Normalize the direction vector and multiply by the enemy's speed to get the velocity
        velocity = direction.normalize() * speed

        enemy = Enemy(type, (x, y), speed, velocity)
        self.enemies.append(enemy)

    def update_enemies(self, dt):
        for enemy in self.enemies:
            # Update the enemy's position
            enemy.pos += enemy.velocity * dt

            # If the enemy has left the screen, remove it
            if enemy.pos.x > self.width + 20 or enemy.pos.x < -20 or enemy.pos.y > self.height + 20 or enemy.pos.y < -20:
                self.enemies.remove(enemy)



    def draw_enemies(self, screen):
        for enemy in self.enemies:
            size = 10 if enemy.type == 'small' else 20
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(int(enemy.pos.x), int(enemy.pos.y), size, size))
