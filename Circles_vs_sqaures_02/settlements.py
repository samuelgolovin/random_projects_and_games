import pygame

class Bullet:
    def __init__(self, x, y, velocity, size, damage, color=(255, 255, 255)):
        self.rect = pygame.Rect(x, y, size / 2, size / 2)
        self.velocity = velocity
        self.color = color
        self.damage = damage

        self.location = self.rect.center

    def draw(self, surface, offset_x, offset_y):
        self.location = (self.rect.centerx + offset_x, self.rect.centery + offset_y)
        pygame.draw.circle(surface, self.color, self.location, self.rect.width / 2)

class Settlement:
    def __init__(self, x, y, type):
        self.type = type

        if self.type == 'basic_earner':
            self.size = 10
            self.color = 'white'
            self.normal_color = 'white'
            self.color_when_cannot_place = 'red'
            self.range = 60
            self.relay = False
            self.over_other_settlemnts = False
            self.earning_rate = 1
            self.earning_cooldown = 60
            self.earning_cooldown_timer = 0

        elif self.type == 'basic_defender':
            self.size = 16
            self.color = 'lightblue'
            self.normal_color = 'lightblue'
            self.color_when_cannot_place = 'red'
            self.range = 40
            self.relay = False
            self.projectile_size = 10
            self.projectile_range = 75
            self.projectile_range_max = 100
            self.cooldown_limit = 80
            self.cooldown = 0
            self.projectile_speed = 500
            self.projectile_damage = 5
            self.bullets = []

        elif self.type == 'basic_relay':
            self.size = 20
            self.color = 'gray'
            self.normal_color = 'gray'
            self.color_when_cannot_place = 'red'
            self.range = 200
            self.relay = True

        elif self.type == 'city':
            self.size = 50
            self.color = 'white'
            self.normal_color = 'white'
            self.color_when_cannot_place = 'red'
            self.relay = True
            

        self.rect = pygame.Rect(x - self.size / 2, y - self.size / 2, self.size, self.size)
        self.location = self.rect.center

    def draw(self, surface, offset_x, offset_y):
        self.location = (self.rect.centerx + offset_x, self.rect.centery + offset_y)
        pygame.draw.circle(surface, self.color, self.location, self.rect.width / 2)
        pygame.draw.circle(surface, 'black', self.location, self.rect.width / 2, 2)
        # if self.type == 'basic_defender':
        #     pygame.draw.circle(surface, "red", self.location, self.projectile_range_max, 1)
        #     pygame.draw.circle(surface, "green", self.location, self.projectile_range, 1)
    
    def fire_bullet(self, enemy_pos):
        self.cooldown = 0
        target = pygame.Vector2(enemy_pos)
        direction = target - pygame.Vector2(self.rect.centerx, self.rect.centery)

        # Normalize the direction vector and multiply by the enemy's speed to get the velocity
        velocity = direction.normalize() * self.projectile_speed

        bullet = Bullet(self.rect.centerx, self.rect.centery, velocity, self.projectile_size, self.projectile_damage)
        self.bullets.append(bullet)

    def closest_enemy(self, enemies):
        if len(enemies) > 1:
            
            temp_array = []
            for enemy in enemies:
                temp_array.append(pygame.Vector2(enemy.rect.center))

            min_val = temp_array[0], 0

            for i in range(1, len(temp_array)):
                if min_val[0].distance_to(pygame.Vector2(self.rect.center)) > temp_array[i].distance_to(pygame.Vector2(self.rect.center)):
                    min_val = temp_array[i], i

            return temp_array[min_val[1]]
        else:
            for enemy in enemies:
                return enemy.rect.center

    def update_bullets(self, dt):
        for bullet in self.bullets:

            # Update the bullets's position
            bullet.rect.center += bullet.velocity * dt

            # If the bullet has left the screen, remove it
            if pygame.Vector2(self.rect.center).distance_to(pygame.Vector2(bullet.rect.center)) > self.projectile_range_max:
                self.bullets.remove(bullet)

    def mouse_over(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False



class Temp_Settlement:
    def __init__(self, x, y, type):
        self.type = type

        if self.type == 'basic_earner':
            self.size = 10
            self.color = 'white'
            self.normal_color = 'white'
            self.color_when_cannot_place = 'red'
            self.range = 60
            self.relay = False
            self.over_other_settlemnts = False

        elif self.type == 'basic_defender':
            self.size = 16
            self.color = 'lightblue'
            self.normal_color = 'lightblue'
            self.color_when_cannot_place = 'red'
            self.range = 40
            self.relay = False

        elif self.type == 'basic_relay':
            self.size = 20
            self.color = 'gray'
            self.normal_color = 'gray'
            self.color_when_cannot_place = 'red'
            self.range = 200
            self.relay = True

        elif self.type == 'city':
            self.size = 50
            self.color = 'white'
            self.normal_color = 'white'
            self.color_when_cannot_place = 'red'
            self.relay = True

        self.rect = pygame.Rect(x - self.size / 2, y - self.size / 2, self.size, self.size)

    def draw(self, surface, mouse_pos):
        self.rect.update((mouse_pos[0] - self.size / 2, mouse_pos[1] - self.size / 2), (self.size, self.size))
        pygame.draw.circle(surface, self.color, self.rect.center, self.rect.width / 2)
        pygame.draw.circle(surface, 'black', self.rect.center, self.rect.width / 2, 2)


class Settlements:
    def __init__(self):
        self.settlements = []
        self.temp_settlement = []
            
    def is_too_close_to_other_settlement(self, bought_settlement_rect):
        for settlement in self.settlements:
            if pygame.Vector2(bought_settlement_rect.center).distance_to(settlement.location) <= settlement.rect.width / 2 + bought_settlement_rect.width / 2:
                return True
        return False

    def create_settlement(self, x, y, type):
        self.settlements.append(Settlement(x, y, type))

    def create_temp_settlement(self, x, y, type):
        self.temp_settlement.append(Temp_Settlement(x, y, type))

    def remove_temp_settlement(self):
        for temp_settlement in self.temp_settlement:
            self.temp_settlement.remove(temp_settlement)

    def does_temp_settlement_exists(self):
        return True if len(self.temp_settlement) > 0 else False

    def get_temp_settlement(self):
        for temp_settlement in self.temp_settlement:
            return temp_settlement

    def draw_temp_settlement(self, surface, mouse_pos):
        for temp_settlement in self.temp_settlement:
            temp_settlement.draw(surface, mouse_pos)

    def get_city_settlement(self):
        for settlement in self.settlements:
            if settlement.type == 'city':
                return settlement