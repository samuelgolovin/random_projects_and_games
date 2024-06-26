import pygame

from button import Button
from connection import Connection

class Settlement:
    def __init__(self, x, y, type):
        self.type = type

        if self.type == 'basic_earner':
            self.size = 10
            self.color = 'white'
            self.normal_color = 'white'
            self.color_when_cannot_place = 'red'
            self.bought = True
            self.range = 50
            self.relay = False
            self.over_other_settlemnts = False

        elif self.type == 'basic_defender':
            self.size = 15
            self.color = 'darkred'
            self.normal_color = 'darkred'
            self.color_when_cannot_place = 'red'
            self.bought = True
            self.range = 50
            self.relay = False

        elif self.type == 'basic_relay':
            self.size = 20
            self.color = 'gray'
            self.normal_color = 'gray'
            self.color_when_cannot_place = 'red'
            self.bought = True
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



    def draw(self, surface):
        if self.type == 'basic_earner':
            pygame.draw.circle(surface, self.color, self.rect.center, self.rect.width / 2)
            pygame.draw.circle(surface, 'black', self.rect.center, self.rect.width / 2, 2)
        elif self.type == 'basic_relay':
            pygame.draw.circle(surface, self.color, self.rect.center, self.rect.width / 2)
            pygame.draw.circle(surface, 'black', self.rect.center, self.rect.width / 2, 2)

        elif self.type == 'city':
            pygame.draw.circle(surface, self.color, self.rect.center, self.rect.width / 2)
            pygame.draw.circle(surface, 'black', self.rect.center, self.rect.width / 2, 2)

    def update_pos_before_placed(self, mouse_pos):
        self.rect.update(mouse_pos[0] - self.rect.width / 2, mouse_pos[1] - self.rect.height / 2, self.rect.width, self.rect.height)

    def update(self, surface):
        self.draw(surface)

class Settlements:
    def __init__(self):
        self.settlements = []
        self.buttons = []
        self.connections = []


    
    def over_button(self, mouse_pos):
        for button in self.buttons:
            if button.rect.collidepoint(mouse_pos):
                return button
            
    def is_over_other_settlement(self, bought_settlement_rect):
        temp = False
        for settlement in self.settlements:
            if not settlement.bought:
                if bought_settlement_rect.colliderect(settlement.rect):
                    temp = True
            
        return temp
            
    def check_if_bought(self):
        for settlement in self.settlements:
            if settlement.bought == True:
                return True
            
    def which_is_bought(self):
        for settlement in self.settlements:
            if settlement.bought == True:
                return settlement
        
    def set_settlement(self):
        for settlement in self.settlements:
            if settlement.bought == True:
                settlement.bought = False
        return

    def create_button(self, x, y, width, height, color, type):
        self.buttons.append(Button(x, y, width, height, color, type))

    def create_settlement(self, x, y, type):
        self.settlements.append(Settlement(x, y, type))

    def create_connection(self, start_pos, end_pos, color):
        self.connections.append(Connection(start_pos, end_pos, color))

    def remove_connection(self, connection):
        self.connections.remove(connection)

    def update_settlements(self, surface):
        if self.settlements:
            for settlement in self.settlements:
                settlement.update(surface)

    def update_buttons(self, surface):
        if self.buttons:
            for button in self.buttons:
                button.update(surface)
            
    def update_connections(self, surface):
        if self.connections:
            for connection in self.connections:
                connection.update(surface)