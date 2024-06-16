import pygame

class Button:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, self.rect.width, self.rect.height)

    def update(self, surface):
        self.draw(surface)

class Settlement:
    def __init__(self, x, y, size, color):
        self.rect = pygame.Rect(x - size / 2, y - size / 2, size, size)
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.rect.center, self.rect.width / 2)

    def update(self, surface):
        self.draw(surface)

class Settlements:
    def __init__(self):
        self.settlements = []
        self.buttons = []

    def create_button(self, x, y, width, height, color):
        self.buttons.append(Button(x, y, width, height, color))

    def create_settlement(self, x, y, size, color):
        self.settlements.append(Settlement(x, y, size, color))

    def update_settlements(self, surface):
        for settlement in self.settlements:
            settlement.update(surface)

    def update_buttons(self, surface):
        for button in self.buttons:
            button.update(surface)