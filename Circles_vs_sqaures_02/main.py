import pygame
import sys

from buttons import Buttons
from connections import Connections
from settlements import Settlements
from screenpanning import PanScreen



class Rectangle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface, offset_x, offset_y):
        pygame.draw.rect(surface, (255, 0, 0), self.rect.move(offset_x, offset_y))

class Line:
    def __init__(self, start_pos, end_pos):
        self.start_pos = start_pos
        self.end_pos = end_pos

    def draw(self, surface, offset_x, offset_y):
        pygame.draw.line(surface, (0, 0, 255), (self.start_pos[0] + offset_x, self.start_pos[1] + offset_y), (self.end_pos[0] + offset_x, self.end_pos[1] + offset_y))

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

    # settlements.create_settlement(WIDTH / 2, (HEIGHT - 150) / 2, 'city')

    while True:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            screen.handle_event(event)  # handle the screen panning
            buttons.handle_event(event)

        screen.screen.fill((60, 60, 90))

        # in-game (above shop)
        


        # shop
        pygame.draw.rect(screen.screen, (60, 60, 40), (0, 475, 925, 125))
        pygame.draw.rect(screen.screen, (0, 0, 0), (0, 475, 925, 125), 5)

        buttons.draw_buttons(screen.screen)
        

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()