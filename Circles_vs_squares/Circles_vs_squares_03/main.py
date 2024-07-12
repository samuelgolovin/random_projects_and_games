import pygame
import sys

from graph import Graph
from screenpanning import PanScreen

from text_utils import draw_text_center

pygame.init()
screen_width, screen_height = 800, 600
screen = PanScreen(screen_width, screen_height, 500, 500)
pygame.display.set_caption("Game")
window = screen.screen


city_graph = Graph()
city_graph.add_border(pygame.Rect(-500, -500, 1800, 100))
city_graph.add_border(pygame.Rect(-500, -500, 100, 1600))
city_graph.add_border(pygame.Rect(-500, 1000, 1800, 100))
city_graph.add_border(pygame.Rect(1200, -500, 1800, 1600))

city_graph.add_node(pygame.Rect(screen_width / 2, screen_height / 2, 50, 50), 'A')


city_graph.add_connection(city_graph.add_node(pygame.Rect(0, 0, 20, 20), 'A'), city_graph.add_node(pygame.Rect(screen_width, screen_height, 20, 20), 'B'))

def draw_city(city_graph):
    screen.draw_objects(city_graph.get_nodes())
    screen.draw_objects(city_graph.connections_to_draw)
    screen.draw_objects(city_graph.borders_to_draw)
    screen.draw_objects(city_graph.shop)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_pos = event.pos

                if city_graph.on_node(screen.get_mouse_position_on_map()):
                    print('on node')
                    # print(city_graph.get_selected_node(screen.get_mouse_position_on_map()))
                    city_graph.create_shop(city_graph.get_selected_node(screen.get_mouse_position_on_map()))
                else:
                    print('not on node')

                # current_node = city_graph.add_node(pygame.Rect(mouse_pos[0] - screen.offset_x, mouse_pos[1] - screen.offset_y, 20, 20), 'A')
                # if len(city_graph.get_nodes()) > 1:
                #     for node in city_graph.get_nodes():
                #         if city_graph.calculate_distance(current_node, node) < 100:
                #             city_graph.add_connection(current_node, node)


        screen.handle_event(event)


    window.fill((28, 90, 36))
    draw_city(city_graph)



    draw_text_center(window, str(screen.get_mouse_position_on_map()[0]) + ", " + str(screen.get_mouse_position_on_map()[1]), 20, 'black', 400, 20)

    pygame.display.flip()
