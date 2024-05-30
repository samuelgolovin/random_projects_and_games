import pygame
import random
import math

class Enemy:
    def __init__(self, type, pos, speed):
        self.type = type
        self.pos = pos
        self.speed = speed

class Enemies:
    def __init__(self, width, height):
        self.enemies = []
        self.width = width
        self.height = height

    def spawn_enemy(self, type):
        # Spawn offscreen
        x = random.choice([0, self.width])
        y = random.choice([0, self.height])
        speed = random.uniform(50, 1050) if type == 'small' else random.uniform(20, 800)

        enemy = Enemy(type, [x, y], speed)
        self.enemies.append(enemy)

    def update_enemies(self, player_pos, dt):
        for enemy in self.enemies:
            dx, dy = player_pos[0] - enemy.pos[0], player_pos[1] - enemy.pos[1]
            angle = math.atan2(dy, dx)
            enemy.pos[0] += enemy.speed * math.cos(angle) * dt
            enemy.pos[1] += enemy.speed * math.sin(angle) * dt

    def draw_enemies(self, screen):
        for enemy in self.enemies:
            size = 10 if enemy.type == 'small' else 20
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(int(enemy.pos[0]), int(enemy.pos[1]), size, size))
