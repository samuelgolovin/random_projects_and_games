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

    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP and buttons.over_button(mouse_pos) and not settlements.temp_settlement_exists():
                if event.button == 1:
                    settlements.create_temp_settlement(mouse_pos[0], mouse_pos[1], buttons.over_button(mouse_pos).type)

                    print("working on this soon")



            screen.handle_event(event)  # handle the screen panning

        screen.screen.fill((60, 60, 90))

        # in-game (beneath the shop)
        


        # shop
        pygame.draw.rect(screen.screen, (60, 60, 40), (0, 475, 925, 125))
        pygame.draw.rect(screen.screen, (0, 0, 0), (0, 475, 925, 125), 5)

        buttons.draw_buttons(screen.screen)

        # in-game (above the shop)

        screen.draw_objects(settlements.settlements)

        if settlements.temp_settlement_exists:
            settlements.update_temp_settlemnt(mouse_pos)
            settlements.draw_temp_settlement(screen.screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()