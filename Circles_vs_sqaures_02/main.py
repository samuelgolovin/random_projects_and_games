import pygame
import sys
import random

from buttons import Buttons
from connections import Connections
from settlements import Settlements
from screenpanning import PanScreen
from enemy import Enemies

def main():
    pygame.init()
    dt = 0
    WIDTH, HEIGHT = 925, 600
    clock = pygame.time.Clock()
    screen = PanScreen(WIDTH, HEIGHT)


    enemies = Enemies(1000, 200, WIDTH, HEIGHT)

    settlements = Settlements()
    buttons = Buttons()
    connections = Connections()

    buttons.create_button(25, 500, 75, 75, (200, 200, 200), 'basic_earner')
    buttons.create_button(125, 500, 75, 75, (200, 200, 200), 'basic_relay')
    buttons.create_button(225, 500, 75, 75, (200, 200, 200), 'basic_defender')

    settlements.create_settlement(WIDTH / 2, (HEIGHT - 150) / 2, 'city')

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
                    if pygame.Vector2(settlement.location).distance_to(mouse_pos) <= temp.range and not settlements.is_too_close_to_other_settlement(temp.rect):
                        if temp.type == 'basic_relay' and settlement.relay:
                            connections.create_connection((mouse_pos[0] - screen.offset_x, mouse_pos[1] - screen.offset_y), (settlement.location[0] - screen.offset_x, settlement.location[1] - screen.offset_y), 'black')    
                        elif not temp.type == 'basic_relay':
                            connections.create_connection((mouse_pos[0] - screen.offset_x, mouse_pos[1] - screen.offset_y), (settlement.location[0] - screen.offset_x, settlement.location[1] - screen.offset_y), 'black')
                
                if not settlements.is_too_close_to_other_settlement(temp.rect):
                    settlements.create_settlement(mouse_pos[0] - screen.offset_x, mouse_pos[1] - screen.offset_y, temp.type) 
                    settlements.remove_temp_settlement()
                else:
                    print("can't place that here")


            screen.handle_event(event)  # handle the screen panning

        # Spawn enemies
        if random.random() < 0.01:  # 1% chance per frame
            enemies.spawn_enemy(settlements.get_city_settlement().rect.center, 20, 20, 100, 100)
        # if random.random() < 0.005:  # 0.5% chance per frame
        #     enemies.spawn_enemy('big', player.pos)
        # if boss_clock >= boss_cooldown:
        #     boss_clock = 0
        #     enemies.spawn_enemy('boss', player.pos)
        # else:
        #     boss_clock += 1

        # Update enemies
        enemies.update_enemies(dt)


        screen.screen.fill((60, 60, 90))

        # in-game (beneath the shop)
    
        screen.draw_objects(connections.connections)

        screen.draw_objects(enemies.enemies)

        if settlements.get_temp_settlement():
            for settlement in settlements.settlements:
                temp = settlements.get_temp_settlement()
                if pygame.Vector2(settlement.location).distance_to(mouse_pos) <= temp.range and not settlements.is_too_close_to_other_settlement(temp.rect):
                    if temp.type == 'basic_relay' and settlement.relay:
                        pygame.draw.line(screen.screen, 'black', ((mouse_pos[0]), mouse_pos[1]), (settlement.location[0], settlement.location[1]))
                    elif not temp.type == 'basic_relay':
                        pygame.draw.line(screen.screen, 'black', ((mouse_pos[0]), mouse_pos[1]), (settlement.location[0], settlement.location[1]))
                
        
        screen.draw_objects(settlements.settlements)

        for settlement in settlements.settlements:
            if settlement.type == 'basic_defender':
                if settlement.cooldown > settlement.cooldown_limit and enemies.enemies:
                    settlement.fire_bullet(settlement.closest_enemy(enemies.enemies))
                else:
                    settlement.cooldown += 1

                settlement.update_bullets(dt)
                screen.draw_objects(settlement.bullets)

        # # shop
        pygame.draw.rect(screen.screen, (60, 60, 40), (0, 475, 925, 125))
        pygame.draw.rect(screen.screen, (0, 0, 0), (0, 475, 925, 125), 5)

        buttons.draw_buttons(screen.screen)


        # in-game (above the shop)

        if settlements.does_temp_settlement_exists():
            temp = settlements.get_temp_settlement()
            if settlements.is_too_close_to_other_settlement(temp.rect):
                temp.color = temp.color_when_cannot_place
            else:
                temp.color = temp.normal_color

            settlements.draw_temp_settlement(screen.screen, mouse_pos)

        

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()