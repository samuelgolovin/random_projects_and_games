import pygame
import sys

class PanScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.objects = []

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button.
                self.dragging = True
                self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
                self.objects.append(Rectangle(self.mouse_x - self.offset_x, self.mouse_y - self.offset_y, 100, 100))

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button.
                self.dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.offset_x += mouse_x - self.mouse_x
                self.offset_y += mouse_y - self.mouse_y
                self.mouse_x, self.mouse_y = mouse_x, mouse_y

    def draw_objects(self):
        for obj in self.objects:
            obj.draw(self.screen, self.offset_x, self.offset_y)

class Rectangle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface, offset_x, offset_y):
        pygame.draw.rect(surface, (255, 0, 0), self.rect.move(offset_x, offset_y))

class Line:
    def __init__(self, start_pos, end_pos):
        self.start_pos = start_pos
        self.end_pos = end_pos

    def draw(self, surface, offset_x, offset_y):
        pygame.draw.line(surface, (0, 0, 255), (self.start_pos[0] + offset_x, self.start_pos[1] + offset_y), (self.end_pos[0] + offset_x, self.end_pos[1] + offset_y))

def main():
    pygame.init()
    screen = PanScreen(800, 600)
    line = Line((100, 100), (200, 200))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            screen.handle_event(event)

        screen.screen.fill((255, 255, 255))
        screen.draw_objects()
        pygame.display.flip()

if __name__ == "__main__":
    main()
