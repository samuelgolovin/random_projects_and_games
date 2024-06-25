# player.py
import pygame

class Bullet:
    def __init__(self, x, y, velocity, radius=3, color=(255, 255, 255)):
        self.pos = pygame.Vector2(x, y)
        self.size = radius
        self.velocity = velocity
        self.color = color

        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.size / 2, self.size / 2)

class Player:
    def __init__(self, screen_width, screen_height, radius=20, color=(255, 255, 255), speed=200):
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
        self.projectile_speed = 500

        self.projectile_damage = 5

        self.bullets = []


    def fire_bullet(self, player_pos, enemy_pos, speed):
        self.cooldown = 0
        target = pygame.Vector2(enemy_pos)
        direction = target - pygame.Vector2(player_pos.x, player_pos.y)

        # Normalize the direction vector and multiply by the enemy's speed to get the velocity
        velocity = direction.normalize() * speed

        bullet = Bullet(self.pos.x, self.pos.y, velocity)
        self.bullets.append(bullet)

    def closest_enemy(self, enemies, player_pos):
        if len(enemies) > 1:
            
            temp_array = []
            for enemy in enemies:
                temp_array.append(pygame.Vector2(enemy.rect.center))

            min_val = temp_array[0], 0

            for i in range(1, len(temp_array)):
                if min_val[0].distance_to(player_pos) > temp_array[i].distance_to(player_pos):
                    min_val = temp_array[i], i

            return temp_array[min_val[1]]
        else:
            for enemy in enemies:
                return enemy.rect.center


    def update_bullets(self, dt):
        for bullet in self.bullets:
            bullet.rect = pygame.Rect(bullet.pos.x, bullet.pos.y, bullet.size, bullet.size)

            # Update the bullets's position
            bullet.pos += bullet.velocity * dt

            # If the bullet has left the screen, remove it
            if bullet.pos.x > self.screen_width + 20 or bullet.pos.x < -20 or bullet.pos.y > self.screen_height + 20 or bullet.pos.y < -20:
                self.bullets.remove(bullet)

    def draw_bullets(self, screen):
        for bullet in self.bullets:
            pygame.draw.circle(screen, self.color, (int(bullet.pos.x), int(bullet.pos.y)), bullet.size)  # Draw the player's circle

    def update(self, dt, mouse_pos):
        self.cooldown += 1
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
