import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Physics Engine")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Particle class
class Particle:
    def __init__(self, x, y, radius, color, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.dx = random.choice([-1, 1]) * speed
        self.dy = random.choice([-1, 1]) * speed

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Bounce off the walls
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.dx *= -1
        if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
            self.dy *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def collide(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        distance = math.hypot(dx, dy)

        if distance < self.radius + other.radius:
            angle = math.atan2(dy, dx)
            total_mass = self.radius + other.radius

            # Update velocities based on elastic collision
            self.dx = (self.dx * (self.radius - other.radius) + 2 * other.radius * other.dx) / total_mass
            self.dy = (self.dy * (self.radius - other.radius) + 2 * other.radius * other.dy) / total_mass
            other.dx = (other.dx * (other.radius - self.radius) + 2 * self.radius * self.dx) / total_mass
            other.dy = (other.dy * (other.radius - self.radius) + 2 * self.radius * self.dy) / total_mass

            # Move particles apart to avoid overlap
            overlap = 0.5 * (self.radius + other.radius - distance + 1)
            self.x += math.cos(angle) * overlap
            self.y += math.sin(angle) * overlap
            other.x -= math.cos(angle) * overlap
            other.y -= math.sin(angle) * overlap

# Create particles
particles = [Particle(random.randint(20, WIDTH-20), random.randint(20, HEIGHT-20), 10, WHITE, 5) for _ in range(10)]

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    for i, particle in enumerate(particles):
        particle.move()
        for other in particles[i+1:]:
            particle.collide(other)
        particle.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
