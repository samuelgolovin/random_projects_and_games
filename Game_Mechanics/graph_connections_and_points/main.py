import pygame
import sys

from graph import Graph

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Mechanic Test")

city_graph = Graph()

city_graph.add_node('A', (200, 200), 'Basic')
city_graph.add_node('B', (100, 200), 'Super')
city_graph.add_node('C', (300, 100), 'Extra')

for node in city_graph.graph:
    print(node)
    print(city_graph.graph[node][0].position)

# print(city_graph.graph)
# print(city_graph.get_nodes())

city_graph.add_connection('A', 'B')
city_graph.add_connection('B', 'C')
# print(city_graph.graph)

# print(city_graph.get_connections('B'))


def draw_city(city_graph):
    for node in city_graph.graph:
        pygame.draw.circle(screen, (255, 0, 0), city_graph.graph[node][0].position, 15)
        font = pygame.font.Font(None, 20)
        text_surface = font.render(node, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center = city_graph.graph[node][0].position)
        screen.blit(text_surface, text_rect)

    for node1 in city_graph.get_nodes():
        for node2 in city_graph.get_connections(node1):
            pygame.draw.line(screen, (0, 0, 255), city_graph.graph[node1][0].position, city_graph.graph[node2][0].position)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # elif event.type == pygame.MOUSEBUTTONDOWN:

    screen.fill((255, 255, 255))
    draw_city(city_graph)
    pygame.display.flip()
