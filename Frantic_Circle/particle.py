import pygame
import random

class Particle:
    def __init__(self, pos, speed, size, value, color):
        self.rect = pygame.Rect(pos.x, pos.y, size, size)
        self.size = size
        self.max_speed = speed
        self.speed = speed
        self.rate_of_slowdown = speed / 30
        self.rate_of_speedup = speed / 100
        self.value = value
        self.color = color
        self.direction = pygame.Vector2(2 * random.random() - 1, 2 * random.random() - 1)

    def near_player_pos(self, player_pos):
        return True if pygame.Vector2(self.rect.center).distance_to(player_pos) <= 100 else False

    def update(self, player_pos):
        self.rect.center += self.direction * self.speed
        if not self.near_player_pos(player_pos):
            if self.speed > 0:
                self.speed -= self.rate_of_slowdown
            else:
                self.speed = 0
        else:
            self.direction = player_pos - pygame.Vector2(self.rect.centerx, self.rect.centery)
            if self.speed < self.max_speed:
                self.speed += self.rate_of_speedup
            else:
                self.speed = self.max_speed

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.rect.center, self.size // 2)

class Particles:
    def __init__(self):
        self.particles = []

    def createParticle(self, num, pos, speed, size, value, color):
        for _ in range(num):
            self.particles.append(Particle(pos, speed, size, value, color))

    def update_and_draw_particles(self, surface, player_pos):
        for particle in self.particles:
            particle.update(player_pos)
            particle.draw(surface)