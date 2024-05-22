import pygame
import calculations

pygame.font.init()

font = pygame.font.Font(None, 36)

class Display:
    def __init__(self, x, y, w, h, text, color, color_border):
        self.x, self.y = x, y
        self.width, self.height = w, h
        self.color = color
        self.color_border = color_border
        self.text = text
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text_surface = font.render(self.text, True, "black")
        self.text_rect = self.text_surface.get_rect(topright = (self.rect.x + self.width, self.rect.y))
        self.stack = []
        self.num1 = 0
        self.num2 = 0
        self.num1_entered = False
        self.num2_entered = False
        self.calc_type = ""
        self.answered = False
        self.answer = 0

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, self.color_border, self.rect, 5)
        
        self.text_surface = font.render(self.text, True, "black")
        self.text_rect = self.text_surface.get_rect(topright = (self.rect.x + self.width, self.rect.y))
        surface.blit(self.text_surface, self.text_rect)

    def insert_into_stack(self, something):
        self.stack.append(something)

    def remove_from_stack(self):
        if self.stack:
            return self.stack.pop()
        
    def remove_all_from_stack(self):
        self.stack = []

    def combine_stack(self):
        all_nums_text = ["".join(self.stack)]
        return (all_nums_text.pop())
    
    def calc(self, calc_type):
        num1 = int(self.num1)
        num2 = int(self.num2)
        if calc_type == "*":
            return calculations.multiplication(num1, num2)
        if calc_type == "/":
            return calculations.division(num1, num2)
        if calc_type == "-":
            return calculations.subtraction(num1, num2)
        if calc_type == "+":
            return calculations.addition(num1, num2)