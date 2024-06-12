# healthbar.py
import pygame

class HealthBar:
    def __init__(self, x, y, width, height, max_health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_health = max_health
        self.current_health = max_health


    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0

    def update(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        # Draw the background of the health bar (indicating lost health)
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, self.width, self.height))
        # Draw the foreground of the health bar (indicating remaining health)
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(self.x, self.y, self.width * (self.current_health / self.max_health), self.height))
