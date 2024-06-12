import pygame

pygame.font.init()
font = pygame.font.Font(None, 36)

class Button:
    def __init__(self, x, y, width, height, text, color):
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)

        self.text_surface = font.render(text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (self.rect.center)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surface, self.text_rect)

class Shop:
    def __init__(self):
        self.buttons = []

        self.buttons.append(Button(10, 10, 100, 50, 'Attack Damage', (230, 150, 173)))

    def draw_buttons(self, screen):
        for button in self.buttons:
            button.draw(screen)