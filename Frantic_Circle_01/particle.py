import pygame
import random

class Particle:
    def __init__(self, pos, speed, size, value):
        self.rect = pygame.Rect(pos.x, pos.y, size, size)
        self.size = size
        self.max_speed = speed
        self.speed_after_spawn = speed
        self.speed_towards_player = 0
        self.rate_of_slowdown = speed / 30
        self.rate_of_speedup = speed / 100
        self.value = value
        self.color = (int(50 * random.random()), int(35 + 220 * random.random()), int(50 * random.random()), 0.8)
        self.direction = pygame.Vector2(2 * random.random() - 1, 2 * random.random() - 1)

    def near_player_pos(self, player_pos):
        return True if pygame.Vector2(self.rect.center).distance_to(player_pos) <= 100 else False

    def update(self, player_pos):
        if not self.near_player_pos(player_pos):
            if self.speed_after_spawn > 0:
                self.speed_after_spawn -= self.rate_of_slowdown
            else:
                self.speed_after_spawn = 0
            self.rect.center += self.direction * self.speed_after_spawn
        else:
            self.direction = player_pos - pygame.Vector2(self.rect.centerx, self.rect.centery)
            if self.speed_towards_player < self.max_speed:
                self.speed_towards_player += self.rate_of_speedup
            else:
                self.speed_towards_player = self.max_speed

            self.rect.center += self.direction * self.speed_towards_player

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.rect.center, self.size // 2)

class Particles:
    def __init__(self):
        self.particles = []

    def createParticle(self, num, pos, speed, size, value):
        for _ in range(num):
            self.particles.append(Particle(pos, speed, size, value))

    def update_and_draw_particles(self, surface, player_pos):
        for particle in self.particles:
            particle.update(player_pos)
            particle.draw(surface)