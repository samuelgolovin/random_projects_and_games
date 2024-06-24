import pygame

class Connection:
    def __init__(self, start_pos, end_pos, color):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.color = color

    def draw(self, surface, offset_x, offset_y):
        pygame.draw.line(surface, (0, 0, 0), (self.start_pos[0] + offset_x, self.start_pos[1] + offset_y), (self.end_pos[0] + offset_x, self.end_pos[1] + offset_y), 2)

class Connections:
    def __init__(self):
        self.temp_connections = []
        self.connections = []

    def create_connection(self, start_pos, end_pos, color):
        self.connections.append(Connection(start_pos, end_pos, color))

    def remove_connection(self, connection):
        print("Will be added soon")

    def create_temp_connection(self, start_pos, end_pos, color):
        self.temp_connections.append(Connection(start_pos, end_pos, color))