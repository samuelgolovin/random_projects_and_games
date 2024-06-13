import pygame

pygame.font.init()
font = pygame.font.Font(None, 16)

class Button:
    def __init__(self, x, y, width, height, text, color, cost):
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.cost = cost

        self.text_surface = font.render(self.text + '\n' + str(self.cost), True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (self.rect.center)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surface, self.text_rect)

    def mouse_over(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
    def update(self):
        self.text_surface = font.render(self.text + '\n' + str(self.cost), True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (self.rect.center)

class Shop:
    def __init__(self):
        self.buttons = []

        self.buttons.append(Button(275, 300, 100, 50, 'Attack Damage', (230, 150, 173), 10))
        self.buttons.append(Button(275, 400, 100, 50, 'Speed', (230, 150, 173), 25))
        self.buttons.append(Button(425, 300, 100, 50, 'Heal', (230, 150, 173), 50))
        self.buttons.append(Button(425, 400, 100, 50, 'money mult', (230, 150, 173), 1000))

    def draw_buttons(self, screen):
        for button in self.buttons:
            button.update()
            button.draw(screen)
