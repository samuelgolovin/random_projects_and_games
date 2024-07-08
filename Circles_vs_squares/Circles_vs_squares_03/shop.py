import pygame

from text_utils import draw_text_topleft

class Button:
    def __init__(self, x, y, width, height, color, type, cost):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.type = type
        self.cost = cost
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=10)
        pygame.draw.rect(surface, "black", self.rect, width=4, border_radius=10)
        if self.type == 'farm':
            pygame.draw.circle(surface, 'white', self.rect.center, self.rect.width / 7)
            pygame.draw.circle(surface, 'black', self.rect.center, self.rect.width / 7, self.rect.width // 18)

        elif self.type == 'basic_relay':
            pygame.draw.circle(surface, 'gray', self.rect.center, self.rect.width / 4)
            pygame.draw.circle(surface, 'black', self.rect.center, self.rect.width / 4, self.rect.width // 20)

        elif self.type == 'defender':
            pygame.draw.circle(surface, 'lightblue', self.rect.center, self.rect.width / 5)
            pygame.draw.circle(surface, 'black', self.rect.center, self.rect.width / 5, self.rect.width // 19)

        elif self.type == 'city':
            pygame.draw.circle(surface, 'white', self.rect.center, self.rect.width / 3)
            pygame.draw.circle(surface, 'black', self.rect.center, self.rect.width / 3, self.rect.width // 10)

class Shop:
    def __init__(self):
        self.buttons = []

    def draw_shop(self, surface, money, screen_width, screen_height):
        pygame.draw.rect(surface, 'white', (0, 0, screen_width / 5, screen_height))
        pygame.draw.rect(surface, 'black', (0, 0, screen_width / 5, screen_height), 5)
        pygame.draw.rect(surface, 'black', (0, 0, screen_width / 5, 150), 5)
        draw_text_topleft(surface, f"money: {money}", 24, "white", 10, 10)
        for button in self.buttons:
            button.draw(surface)
    
    def create_button(self, x, y, width, height, color, type, cost):
        self.buttons.append(Button(x, y, width, height, color, type, cost))

    def over_button(self, mouse_pos):
        for button in self.buttons:
            if button.rect.collidepoint(mouse_pos):
                return button
        return False