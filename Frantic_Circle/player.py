# player.py
import pygame

class Bullet:
    def __init__(self, x, y, radius=3, color=(255, 255, 255), speed=500):
        self.rect = pygame.rect()

class Player:
    def __init__(self, screen_width, screen_height, radius=20, color=(255, 255, 255), speed=300):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.pos = pygame.Vector2(screen_width // 2, screen_height // 2)
        self.radius = radius
        self.color = color
        self.change_color = False
        self.speed = speed
        self.hitbox_size = radius * 1.5
        self.rect = pygame.Rect(self.pos.x - self.hitbox_size / 2, self.pos.y - self.hitbox_size / 2, self.hitbox_size, self.hitbox_size)

        self.cooldown = 0
        self.cooldown_limit = 10

        self.bullets = []


    def fire_bullet(self):
        bullet = Bullet(self.pos.x, self.pos.y)
        self.bullets.append(bullet)

    def update_bullets(self, dt):
        for bullet in self.bullets:
            bullet.rect = pygame.Rect(bullet.pos.x, bullet.pos.y, bullet.size, bullet.size)

            # Update the bullets's position
            bullet.pos += bullet.velocity * dt

            # If the bullet has left the screen, remove it
            if bullet.pos.x > self.width + 20 or bullet.pos.x < -20 or bullet.pos.y > self.height + 20 or bullet.pos.y < -20:
                self.bullets.remove(bullet)

    def update(self, dt, mouse_pos):
        self.cooldown += 1
        if self.cooldown > self.cooldown_limit:
            self.fire_bullet()
        self.rect = pygame.Rect(self.pos.x - self.hitbox_size / 2, self.pos.y - self.hitbox_size / 2, self.hitbox_size, self.hitbox_size)
        direction = (mouse_pos - self.pos).normalize()
        threshold_distance = 3  # You can adjust this value as needed

        # Check if the distance between the player and the mouse is greater than the threshold
        if (mouse_pos - self.pos).length() > threshold_distance:
            self.pos += direction * self.speed * dt  # Update the player's position

    def draw(self, screen, is_invincible, timer):
        # when invincible, changes colors every few frames
        if (timer % 5) == 0 and is_invincible:
            self.change_color = not self.change_color

        if is_invincible and self.change_color:
            pygame.draw.circle(screen, "darkgray", (int(self.pos.x), int(self.pos.y)), self.radius)  # Draw the player's circle
        elif is_invincible and not self.change_color:
            pygame.draw.circle(screen, "lightgray", (int(self.pos.x), int(self.pos.y)), self.radius)  # Draw the player's circle
        else:
            pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), self.radius)  # Draw the player's circle
        # hitbox
        # pygame.draw.rect(screen, "white", self.rect)
