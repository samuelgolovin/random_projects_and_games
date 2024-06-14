import pygame
import random

class Particle:
    def __init__(self, pos, speed, size, value, color):
        self.rect = pygame.Rect(pos.x, pos.y, size, size)
        self.size = size
        self.speed = speed
        self.rate_of_slowdown = speed / 30
        self.value = value
        self.color = color
        self.direction = pygame.Vector2(2 * random.random() - 1, 2 * random.random() - 1)

    def update(self):
        self.rect.center -= self.direction * self.speed
        if self.speed > 0:
            self.speed -= self.rate_of_slowdown
        else:
            self.speed = 0

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.rect.center, self.size // 2)

class Particles:
    def __init__(self):
        self.particles = []

    def createParticle(self, num, pos, speed, size, value, color):
        for _ in range(num):
            self.particles.append(Particle(pos, speed, size, value, color))

    def update_and_draw_particles(self, surface):
        for particle in self.particles:
            particle.update()
            particle.draw(surface)