import pygame

class Connection:
    def __init__(self, start_pos, end_pos, color):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.color = color

    def draw(self, surface, offset_x, offset_y):
        pygame.draw.line(surface, (0, 0, 0), (self.start_pos[0] + offset_x, self.start_pos[1] + offset_y), (self.end_pos[0] + offset_x, self.end_pos[1] + offset_y))
    
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
