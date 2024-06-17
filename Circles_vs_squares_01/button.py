import pygame

class Button:
    def __init__(self, x, y, width, height, color, type):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.type = type
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        if self.type == 'basic_earner':
            pygame.draw.circle(surface, 'white', self.rect.center, self.rect.width / 5)
            pygame.draw.circle(surface, 'black', self.rect.center, self.rect.width / 5, self.rect.width // 15)


        elif self.type == 'city':
            pygame.draw.circle(surface, 'white', self.rect.center, self.rect.width / 3)
            pygame.draw.circle(surface, 'black', self.rect.center, self.rect.width / 3, self.rect.width // 10)

    def update(self, surface):
        self.draw(surface)