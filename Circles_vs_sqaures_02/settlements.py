import pygame

class Settlement:
    def __init__(self, x, y, type):
        self.type = type

        if self.type == 'basic_earner':
            self.size = 10
            self.color = 'white'
            self.normal_color = 'white'
            self.color_when_cannot_place = 'red'
            self.range = 50
            self.relay = False
            self.over_other_settlemnts = False

        elif self.type == 'basic_defender':
            self.size = 15
            self.color = 'darkred'
            self.normal_color = 'darkred'
            self.color_when_cannot_place = 'red'
            self.range = 50
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
        self.location = self.rect.center

    def draw(self, surface, offset_x, offset_y):
        self.location = (self.rect.centerx + offset_x, self.rect.centery + offset_y)
        pygame.draw.circle(surface, self.color, self.location, self.rect.width / 2)
        pygame.draw.circle(surface, 'black', self.location, self.rect.width / 2, 2)

class Temp_Settlement:
    def __init__(self, x, y, type):
        self.type = type

        if self.type == 'basic_earner':
            self.size = 10
            self.color = 'white'
            self.normal_color = 'white'
            self.color_when_cannot_place = 'red'
            self.range = 50
            self.relay = False
            self.over_other_settlemnts = False

        elif self.type == 'basic_defender':
            self.size = 15
            self.color = 'darkred'
            self.normal_color = 'darkred'
            self.color_when_cannot_place = 'red'
            self.range = 50
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