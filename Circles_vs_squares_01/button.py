import pygame

class Button:
    def __init__(self, x, y, width, height, color, type):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.type = type
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=10)
        pygame.draw.rect(surface, "black", self.rect, width=4, border_radius=10)
        if self.type == 'basic_earner':
            pygame.draw.circle(surface, 'white', self.rect.center, self.rect.width / 7)
            pygame.draw.circle(surface, 'black', self.rect.center, self.rect.width / 7, self.rect.width // 18)

        elif self.type == 'basic_relay':
            pygame.draw.circle(surface, 'gray', self.rect.center, self.rect.width / 4)
            pygame.draw.circle(surface, 'black', self.rect.center, self.rect.width / 4, self.rect.width // 20)


        elif self.type == 'city':
            pygame.draw.circle(surface, 'white', self.rect.center, self.rect.width / 3)
            pygame.draw.circle(surface, 'black', self.rect.center, self.rect.width / 3, self.rect.width // 10)

    def update(self, surface):
        self.draw(surface)