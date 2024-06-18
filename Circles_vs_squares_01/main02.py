import pygame
import sys

from settlements02 import Settlements
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
    screen = PanScreen(925, 600)
    rectangle = Rectangle(50, 50, 100, 100)
    line = Line((0, 0), (500, 500))

    objects = [rectangle, line]

    settlements = Settlements()

    settlements.create_button(25, 500, 75, 75, (200, 200, 200), 'basic_earner')

    settlements.create_settlement(WIDTH / 2, (HEIGHT - 150) / 2, 'city')

    for button in settlements.buttons:
        if button.type == 'city':
            settlements.buttons.remove(button)

    for settlement in settlements.settlements:
        objects.append(settlement)

    while True:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP and settlements.over_button(mouse_pos):
                settlements.buy_settlement(mouse_pos[0], mouse_pos[1], settlements.over_button(mouse_pos).type)
                print('bought')

            if event.type == pygame.MOUSEBUTTONDOWN and len(settlements.settlement_just_bought) > 0:

                for settlement in settlements.settlements:
                    
                    print(settlements.settlement_just_bought[0].range)
                    if pygame.Vector2(settlement.rect.center).distance_to(mouse_pos) <= settlements.settlement_just_bought[0].range:
                            if settlements.settlement_just_bought[0].type == 'basic_relay' and settlement.relay:
                                settlements.create_connection(mouse_pos, settlement.rect.center, 'black')    
                            elif not settlements.settlement_just_bought[0].type == 'basic_relay':
                                settlements.create_connection(mouse_pos, settlement.rect.center, 'black')    
                    
                if not settlements.is_over_other_settlement(settlements.settlement_just_bought[0].rect):
                    print('hellow')
                    settlements.set_settlement(screen.mouse_x, screen.mouse_y, screen.offset_x, screen.offset_y)
                    settlements.create_connection(mouse_pos, settlement.rect.center, 'black')  
                    objects.append(settlements.settlements[-1])
                    
                else:
                    print("can't place that here")

            screen.handle_event(event)  # handle the screen panning

        screen.screen.fill((60, 60, 90))

        if settlements.check_if_bought():
            for settlement in settlements.settlements:
                if pygame.Vector2(settlement.location).distance_to(mouse_pos) <= settlements.which_is_bought().range and not settlement.bought:
                        if settlements.which_is_bought().type == 'basic_relay' and settlement.relay:
                            pygame.draw.line(screen.screen, 'black', mouse_pos, settlement.location)
                        elif not settlements.which_is_bought().type == 'basic_relay':
                            pygame.draw.line(screen.screen, 'black', mouse_pos, settlement.location)
        if settlements.which_is_bought():
            if settlements.is_over_other_settlement(settlements.which_is_bought().rect):
                settlements.which_is_bought().color = settlements.which_is_bought().color_when_cannot_place
            else:
                settlements.which_is_bought().color = settlements.which_is_bought().normal_color


        # settlements.update_settlements(screen.screen)
        screen.draw_objects(objects)

        pygame.draw.rect(screen.screen, (60, 60, 40), (0, 475, 925, 125))
        pygame.draw.rect(screen.screen, (0, 0, 0), (0, 475, 925, 125), 5)

        settlements.update_buttons(screen.screen)

        for settlement in settlements.settlement_just_bought:
            if settlement.bought == True:
                settlement.update_pos_before_placed(mouse_pos)
                settlement.draw_bought(screen.screen)

        

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()