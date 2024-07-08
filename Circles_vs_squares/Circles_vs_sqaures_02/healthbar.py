# healthbar.py
import pygame

class HealthBar:
    def __init__(self, x, y, width, height, max_health, num_invincibility_frames=100):
        self.rect = pygame.Rect(x, y, width, height)
        self.max_health = max_health
        self.current_health = max_health
        self.invincible = False
        self.timer_for_invincibility = 0
        self.num_invincibility_frames = num_invincibility_frames

        self.location = self.rect.center

    def set_invincible(self):
        self.invincible = True

    def is_invincible(self):
        return self.invincible

    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0
        # self.set_invincible()

    def update(self):
        if self.timer_for_invincibility < self.num_invincibility_frames and self.invincible == True:
            self.timer_for_invincibility += 1
        else: 
            self.invincible = False
            self.timer_for_invincibility = 0

    def draw(self, screen, offset_x, offset_y):
        self.location = (self.rect.centerx + offset_x - self.rect.width / 2, self.rect.centery + offset_y + self.rect.height / 2 + (self.rect.height / 10))
        # Draw the background of the health bar (indicating lost health)
        pygame.draw.rect(screen, (255, 0, 0), ((self.location), (self.rect.width, self.rect.height / 10)))
        # Draw the foreground of the health bar (indicating remaining health)
        pygame.draw.rect(screen, (0, 255, 0), ((self.location), (self.rect.width * (self.current_health / self.max_health), self.rect.height / 10)))
