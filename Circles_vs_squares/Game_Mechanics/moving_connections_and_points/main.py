import pygame
import sys

from graph import Graph
from screenpanning import PanScreen

pygame.init()
screen_width, screen_height = 800, 600
screen = PanScreen(screen_width, screen_height, 500, 500)
pygame.display.set_caption("Game Mechanic Test")
window = screen.screen

city_graph = Graph()


def draw_city(city_graph):
    # for node in city_graph.get_nodes():
    #     pygame.draw.circle(window, (255, 0, 0), node.position, 15)
    #     font = pygame.font.Font(None, 20)
    #     text_surface = font.render(node.type, True, (0, 0, 0))
    #     text_rect = text_surface.get_rect(center = node.position)
    #     window.blit(text_surface, text_rect)

    screen.draw_objects(city_graph.get_nodes())

    # for node in city_graph.get_nodes():
    #     for connected_node in city_graph.get_connections(node):
    #         pygame.draw.line(window, (0, 0, 255), node.position, connected_node.position)

    screen.draw_objects(city_graph.connections_to_draw)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:  # Left mouse button
                mouse_pos = event.pos

                current_node = city_graph.add_node((mouse_pos[0] - screen.offset_x, mouse_pos[1] - screen.offset_y), 'A')
                if len(city_graph.get_nodes()) > 1:
                    for node in city_graph.get_nodes():
                        if city_graph.calculate_distance(current_node, node) < 100:
                            city_graph.add_connection(current_node, node)

        screen.handle_event(event)


    window.fill((255, 255, 255))
    draw_city(city_graph)
    pygame.display.flip()
