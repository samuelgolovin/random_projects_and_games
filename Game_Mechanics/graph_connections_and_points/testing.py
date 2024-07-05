import pygame
import sys
import math

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("City Map")

class Graph:
    def __init__(self):
        self.graph = {}

    def add_settlement(self, settlement):
        if settlement not in self.graph:
            self.graph[settlement] = []

    def add_road(self, settlement1, settlement2):
        if settlement1 in self.graph and settlement2 in self.graph:
            self.graph[settlement1].append(settlement2)
            self.graph[settlement2].append(settlement1)
        else:
            print("Error: Both settlements must exist in the graph.")

    def get_settlements(self):
        return list(self.graph.keys())

    def get_roads(self, settlement):
        if settlement in self.graph:
            return self.graph[settlement]
        else:
            print(f"Error: {settlement} does not exist in the graph.")
            return []

    def find_closest_settlement(self, new_settlement):
        closest_settlement = None
        min_distance = float('inf')
        for settlement in self.get_settlements():
            distance = math.dist(new_settlement, settlement_positions[settlement])
            if distance < min_distance:
                min_distance = distance
                closest_settlement = settlement
        return closest_settlement

# Example usage
city_graph = Graph()
settlement_positions = {"A": (100, 100), "B": (200, 200), "C": (300, 300)}

def draw_city(city_graph, settlement_positions):
    for settlement, position in settlement_positions.items():
        pygame.draw.circle(screen, (255, 0, 0), position, 10)  # Example radius
        font = pygame.font.Font(None, 20)
        text_surface = font.render(settlement, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=position)
        screen.blit(text_surface, text_rect)

    # Draw roads
    for settlement1 in city_graph.get_settlements():
        for settlement2 in city_graph.get_roads(settlement1):
            pygame.draw.line(screen, (0, 0, 255), settlement_positions[settlement1], settlement_positions[settlement2])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                new_settlement = event.pos
                if city_graph.get_settlements():
                    new_settlement_name = chr(ord(max(city_graph.get_settlements())) + 1)  # Next letter
                else:
                    new_settlement_name = "A"  # Start with 'A' if no settlements exist
                city_graph.add_settlement(new_settlement_name)
                settlement_positions[new_settlement_name] = new_settlement  # Add new settlement to positions
                closest_settlement = city_graph.find_closest_settlement(new_settlement)
                city_graph.add_road(new_settlement_name, closest_settlement)



    screen.fill((255, 255, 255))  # Clear the screen
    draw_city(city_graph, settlement_positions)
    pygame.display.flip()
