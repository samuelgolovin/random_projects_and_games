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

        elif self.type == 'basic_defender':
            pygame.draw.circle(surface, 'lightblue', self.rect.center, self.rect.width / 5)
            pygame.draw.circle(surface, 'black', self.rect.center, self.rect.width / 5, self.rect.width // 19)

        elif self.type == 'city':
            pygame.draw.circle(surface, 'white', self.rect.center, self.rect.width / 3)
            pygame.draw.circle(surface, 'black', self.rect.center, self.rect.width / 3, self.rect.width // 10)

class Buttons:
    def __init__(self):
        self.buttons = []

    def draw_buttons(self, surface):
        for button in self.buttons:
            button.draw(surface)
    
    def create_button(self, x, y, width, height, color, type):
        self.buttons.append(Button(x, y, width, height, color, type))

    def over_button(self, mouse_pos):
        for button in self.buttons:
            if button.rect.collidepoint(mouse_pos):
                return button
        return False
