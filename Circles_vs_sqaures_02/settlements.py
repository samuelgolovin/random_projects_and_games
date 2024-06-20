import pygame

class Settlement:
    def __init__(self, x, y, type, bought=True):
        self.type = type

        if self.type == 'basic_earner':
            self.size = 10
            self.color = 'white'
            self.normal_color = 'white'
            self.color_when_cannot_place = 'red'
            self.bought = bought
            self.range = 50
            self.relay = False
            self.over_other_settlemnts = False

        elif self.type == 'basic_defender':
            self.size = 15
            self.color = 'darkred'
            self.normal_color = 'darkred'
            self.color_when_cannot_place = 'red'
            self.bought = bought
            self.range = 50
            self.relay = False

        elif self.type == 'basic_relay':
            self.size = 20
            self.color = 'gray'
            self.normal_color = 'gray'
            self.color_when_cannot_place = 'red'
            self.bought = bought
            self.range = 200
            self.relay = True

        elif self.type == 'city':
            self.size = 50
            self.color = 'white'
            self.normal_color = 'white'
            self.color_when_cannot_place = 'red'
            self.bought = False
            self.relay = True
            

        self.rect = pygame.Rect(x - self.size / 2, y - self.size / 2, self.size, self.size)
        self.location = self.rect.center

    def draw(self, surface, offset_x, offset_y):
        self.location = (self.rect.centerx + offset_x, self.rect.centery + offset_y)
        if self.type == 'basic_earner':
            pygame.draw.circle(surface, self.color, self.location, self.rect.width / 2)
            pygame.draw.circle(surface, 'black', self.location, self.rect.width / 2, 2)
        elif self.type == 'basic_relay':
            pygame.draw.circle(surface, self.color, self.location, self.rect.width / 2)
            pygame.draw.circle(surface, 'black', self.location, self.rect.width / 2, 2)

        elif self.type == 'city':
            pygame.draw.circle(surface, self.color, self.location, self.rect.width / 2)
            pygame.draw.circle(surface, 'black', self.location, self.rect.width / 2, 2)

class Settlements:
    def __init__(self):
        self.settlements = []
            
    def is_over_other_settlement(self, bought_settlement_rect):
        temp = False
        for settlement in self.settlements:
            if not settlement.bought:
                if bought_settlement_rect.colliderect(settlement.rect):
                    temp = True
            
        return temp

    def create_settlement(self, x, y, type):
        self.settlements.append(Settlement(x, y, type))