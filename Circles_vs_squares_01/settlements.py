import pygame

class Settlement:
    def __init__(self, x, y, size, type, color):
        self.rect = pygame.Rect(x - size / 2, y - size / 2, size, size)
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.rect.center, self.rect.width / 2)

    def update(self, surface):
        self.draw(surface)

class Settlements:
    def __init__(self):
        self.settlements = []

    def create_settlement(self, x, y, size, color):
        self.settlements.append(Settlement(x, y, size, color))

    def update_settlements(self, surface):
        for settlement in self.settlements:
            settlement.update(surface)