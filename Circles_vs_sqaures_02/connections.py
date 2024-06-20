import pygame

class Connection:
    def __init__(self, start_pos, end_pos, color):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.color = color

    def draw(self, surface):
        pygame.draw.line(surface, self.color, self.start_pos, self.end_pos, 3)
    
    def update_line_before_set(self, mouse_pos):
        self.start_pos = mouse_pos

    def update(self, surface):
        self.draw(surface)

class Connections:
    def __init__(self):
        self.connections = []

    def create_connection(self, start_pos, end_pos, color):
        self.connections.append(Connection(start_pos, end_pos, color))

    def remove_connection(self, connection):
        print("Will be added soon")
