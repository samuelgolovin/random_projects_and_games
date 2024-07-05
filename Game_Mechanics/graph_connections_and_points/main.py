import pygame
import sys

from graph import Graph
from graph import Node

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Mechanic Test")

city_graph = Graph()

node1 = Node((100, 100), 'A')
node2 = Node((200, 100), 'B')
node3 = Node((300, 200), 'C')
node4 = Node((400, 300), 'D')

node5 = Node((150 + 100, 150 + 100), 'A1')
node6 = Node((250 + 100, 150 + 100), 'B1')
node7 = Node((350 + 100, 250 + 100), 'C1')
node8 = Node((450 + 100, 350 + 100), 'D1')

city_graph.add_node(node1)
city_graph.add_node(node2)
city_graph.add_node(node3)
city_graph.add_node(node4)
city_graph.add_node(node5)
city_graph.add_node(node6)
city_graph.add_node(node7)
city_graph.add_node(node8)


city_graph.add_connection(node1, node2)
city_graph.add_connection(node2, node3)
city_graph.add_connection(node3, node4)
city_graph.add_connection(node4, node5)

# print(city_graph.graph)


def draw_city(city_graph):
    for node in city_graph.graph:
        pygame.draw.circle(screen, (255, 0, 0), city_graph.graph[node][0].position, 15)
        font = pygame.font.Font(None, 20)
        text_surface = font.render(city_graph.graph[node][0].type, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center = city_graph.graph[node][0].position)
        screen.blit(text_surface, text_rect)

    for node in city_graph.get_nodes():
        for connected_node in city_graph.get_connections(node):
            pygame.draw.line(screen, (0, 0, 255), city_graph.graph[node][0].position, city_graph.graph[connected_node][0].position)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # elif event.type == pygame.MOUSEBUTTONDOWN:

    screen.fill((255, 255, 255))
    draw_city(city_graph)
    pygame.display.flip()
