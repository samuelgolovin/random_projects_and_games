import pygame
import sys

from buttons import Buttons
from connections import Connections
from settlements import Settlements
from screenpanning import PanScreen

def main():
    pygame.init()
    dt = 0
    WIDTH, HEIGHT = 925, 600
    clock = pygame.time.Clock()
    screen = PanScreen(WIDTH, HEIGHT)


    settlements = Settlements()
    buttons = Buttons()
    connections = Connections()

    buttons.create_button(25, 500, 75, 75, (200, 200, 200), 'basic_earner')

    settlements.create_settlement(WIDTH / 2, (HEIGHT - 150) / 2, 'city')

    settlements.create_settlement(WIDTH / 3, (HEIGHT - 150) / 3, 'basic_earner')

    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP and buttons.over_button(mouse_pos) and not settlements.does_temp_settlement_exists():
                if event.button == 1:
                    settlements.create_temp_settlement(mouse_pos[0], mouse_pos[1], buttons.over_button(mouse_pos).type)

            if event.type == pygame.MOUSEBUTTONDOWN and screen.is_mouse_on_game(mouse_pos) and settlements.does_temp_settlement_exists():
                
                temp = settlements.get_temp_settlement()

                for settlement in settlements.settlements:
                    if pygame.Vector2(settlement.rect.center).distance_to(mouse_pos) <= temp.range and not settlements.is_over_other_settlement(temp.rect):
                        if temp.type == 'basic_relay' and settlement.relay:
                            connections.create_connection(mouse_pos, settlement.rect.center, 'black')    
                        elif not temp.type == 'basic_relay':
                            connections.create_connection(mouse_pos, settlement.rect.center, 'black')
                
                settlements.create_settlement(mouse_pos[0] - screen.offset_x, mouse_pos[1] - screen.offset_y, temp.type) 
                settlements.remove_temp_settlement()


            screen.handle_event(event)  # handle the screen panning

        screen.screen.fill((60, 60, 90))

        # in-game (beneath the shop)

        screen.draw_objects(connections.connections)
        
        screen.draw_objects(settlements.settlements)

        # # shop
        pygame.draw.rect(screen.screen, (60, 60, 40), (0, 475, 925, 125))
        pygame.draw.rect(screen.screen, (0, 0, 0), (0, 475, 925, 125), 5)

        buttons.draw_buttons(screen.screen)


        # in-game (above the shop)

        if settlements.does_temp_settlement_exists():
            settlements.draw_temp_settlement(screen.screen, mouse_pos)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()