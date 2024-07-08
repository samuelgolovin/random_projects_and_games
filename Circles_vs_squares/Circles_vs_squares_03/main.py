import pygame
import sys
import random

from screen import Screen
from circles import CircleGraph
# from squares import Squares
from shop import Shop
from graph import Graph

from text_utils import draw_text_center, draw_text_topleft


def main():
    pygame.init()
    screen_width, screen_height = 900, 600
    clock = pygame.time.Clock()
    screen = Screen(screen_width, screen_height, 500, 500)
    window = screen.screen

    circlegraph = CircleGraph()

    shop = Shop()

    button_size = screen_width / 10 - 15

    shop.create_button(10, 160, button_size, button_size, (200, 200, 200), 'farm', 10)
    shop.create_button((screen_width / 10), 160, button_size, button_size, (200, 200, 200), 'defender', 10)

    money = 100

    current_scene = 'start'


    def draw_city(city_graph):
        for node in city_graph.get_nodes():
            pygame.draw.circle(screen, (255, 0, 0), node.position, 15)
            font = pygame.font.Font(None, 20)
            text_surface = font.render(node.type, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center = node.position)
            screen.blit(text_surface, text_rect)

        for node in city_graph.get_nodes():
            for connected_node in city_graph.get_connections(node):
                pygame.draw.line(screen, (0, 0, 255), node.position, connected_node.position)

    while True:
        if current_scene == 'start':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        current_scene = 'game'

            window.fill('white')

            draw_text_center(window, "Circles VS Squares", 100, "black", screen_width / 2, screen_height / 2 - 100)
            draw_text_center(window, "Press SPACE to play", 75, "black", screen_width / 2, screen_height / 2 + 100)


############################################################################################################################


        elif current_scene == 'game':
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if shop.over_button(mouse_pos) and not circlegraph.does_temp_circle_exists():
                            circlegraph.create_temp_circle(mouse_pos, 'farm')

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if screen.is_mouse_on_game(mouse_pos) and circlegraph.does_temp_circle_exists():
                            circlegraph.add_node((mouse_pos[0] - screen.offset_x, mouse_pos[1] - screen.offset_y), 'temp/change later')
                            circlegraph.remove_temp_circle()

            screen.handle_event(event)

            window.fill((80, 110, 40))

            shop.draw_shop(window, money, screen_width, screen_height)

            circlegraph.draw_temp_circle(window, mouse_pos)

            draw_city(circlegraph)

            

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == '__main__':
    main()