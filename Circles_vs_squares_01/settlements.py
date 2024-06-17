import pygame

class Button:
    def __init__(self, x, y, width, height, color, type):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.type = type
    
    def draw(self, surface):
        if self.type == 'basic_earner':
            pygame.draw.rect(surface, self.color, self.rect)
            pygame.draw.circle(surface, 'white', self.rect.center, self.rect.width / 3)
            pygame.draw.circle(surface, 'black', self.rect.center, self.rect.width / 3, self.rect.width // 10)

    def update(self, surface):
        self.draw(surface)

class Settlement:
    def __init__(self, x, y, size, color):
        self.rect = pygame.Rect(x - size / 2, y - size / 2, size, size)
        self.color = color

        self.bought = True

    def draw(self, surface):
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
    
    def over_button(self, mouse_pos):
        for button in self.buttons:
            if button.rect.collidepoint(mouse_pos):
                return True
            else:
                return False
            
    def check_if_bought(self):
        for settlement in self.settlements:
            if settlement.bought == True:
                return True
            
        
    def set_settlement(self):
        for settlement in self.settlements:
            if settlement.bought == True:
                settlement.bought = False
                return

    def create_button(self, x, y, width, height, color, type):
        self.buttons.append(Button(x, y, width, height, color, type))

    def create_settlement(self, x, y, size, color):
        self.settlements.append(Settlement(x, y, size, color))

    def update_settlements(self, surface):
        if self.settlements:
            for settlement in self.settlements:
                settlement.update(surface)

    def update_buttons(self, surface):
        if self.buttons:
            for button in self.buttons:
                button.update(surface)