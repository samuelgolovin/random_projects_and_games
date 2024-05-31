# player.py
import pygame

class Player:
    def __init__(self, x, y, radius=20, color=(255, 255, 255), speed=300):
        self.pos = pygame.Vector2(x, y)
        self.radius = radius
        self.color = color
        self.speed = speed

    def update(self, dt, mouse_pos):
        direction = (mouse_pos - self.pos).normalize()
        threshold_distance = 2  # You can adjust this value as needed

        # Check if the distance between the player and the mouse is greater than the threshold
        if (mouse_pos - self.pos).length() > threshold_distance:
            self.pos += direction * self.speed * dt  # Update the player's position

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), self.radius)  # Draw the player's circle
