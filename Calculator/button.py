import pygame

pygame.font.init()

font = pygame.font.Font(None, 36)

class Button:
    def __init__(self, x, y, w, h, text, color):
        self.x, self.y = x, y
        self.width, self.height = w, h
        self.color = color
        self.text = text
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text_surface = font.render(self.text, True, "black")
        self.text_rect = self.text_surface.get_rect(center = (self.rect.x + self.width // 2, self.rect.y + self.height // 2))

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(self.text_surface, self.text_rect)

    def mouse_on_button(self, mouse_x, mouse_y):
        if self.rect.collidepoint(mouse_x, mouse_y):
            return True
        return False