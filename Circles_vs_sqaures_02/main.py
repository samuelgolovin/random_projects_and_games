import pygame
import sys
import random

from buttons import Buttons
from connections import Connections
from settlements import Settlements
from screenpanning import PanScreen
from enemy import Enemies

from text_utils import draw_text_center, draw_text_topleft

def main():
    pygame.init()
    dt = 0
    WIDTH, HEIGHT = 925, 600
    clock = pygame.time.Clock()
    screen = PanScreen(WIDTH, HEIGHT, 200, 200)
    window = screen.screen

    money = 100

    current_scene = 'start'

    enemies = Enemies(1000, 200, WIDTH, HEIGHT)

    settlements = Settlements()
    buttons = Buttons()
    connections = Connections()

    buttons.create_button(25, 500, 75, 75, (200, 200, 200), 'basic_earner', 10)
    buttons.create_button(125, 500, 75, 75, (200, 200, 200), 'basic_relay', 25)
    buttons.create_button(225, 500, 75, 75, (200, 200, 200), 'basic_defender', 30)

    settlements.create_settlement(WIDTH / 2, (HEIGHT - 150) / 2, 'city')

    while True:

# start screen
        if current_scene == 'start':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        current_scene = 'game'

            window.fill('white')

            draw_text_center(window, "Circles VS Squares", 100, "black", WIDTH / 2, HEIGHT / 2 - 100)
            draw_text_center(window, "Press SPACE to play", 75, "black", WIDTH / 2, HEIGHT / 2 + 100)

# game

        elif current_scene == 'game':
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # if screen.is_mouse_on_game(mouse_pos):
                #     if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                #         enemies.spawn_enemy(settlements.get_city_settlement().rect.center, 20, 20, 50, 5)

                if buttons.over_button(mouse_pos):
                    if event.type == pygame.MOUSEBUTTONUP and buttons.over_button(mouse_pos).cost <= money and not settlements.does_temp_settlement_exists():
                        if event.button == 1:
                            money -= buttons.over_button(mouse_pos).cost
                            settlements.create_temp_settlement(mouse_pos[0], mouse_pos[1], buttons.over_button(mouse_pos).type)

                if event.type == pygame.MOUSEBUTTONDOWN and screen.is_mouse_on_game(mouse_pos) and settlements.does_temp_settlement_exists():
                    
                    temp = settlements.get_temp_settlement()
                    can_place = False

                    for settlement in settlements.settlements:
                        if pygame.Vector2(settlement.location).distance_to(mouse_pos) <= temp.range and not settlements.is_too_close_to_other_settlement(temp.rect):
                            can_place = True
                            if temp.type == 'basic_relay' and settlement.relay:
                                connections.create_connection((mouse_pos[0] - screen.offset_x, mouse_pos[1] - screen.offset_y), (settlement.location[0] - screen.offset_x, settlement.location[1] - screen.offset_y), 'black')    
                            elif not temp.type == 'basic_relay':
                                connections.create_connection((mouse_pos[0] - screen.offset_x, mouse_pos[1] - screen.offset_y), (settlement.location[0] - screen.offset_x, settlement.location[1] - screen.offset_y), 'black')
                    
                            # settlements.create_settlement(mouse_pos[0] - screen.offset_x, mouse_pos[1] - screen.offset_y, temp.type) 
                            # settlements.remove_temp_settlement()

                    if not settlements.is_too_close_to_other_settlement(temp.rect) and can_place == True:
                        settlements.create_settlement(mouse_pos[0] - screen.offset_x, mouse_pos[1] - screen.offset_y, temp.type) 
                        settlements.remove_temp_settlement()
                    else:
                        print("can't place that here")


                screen.handle_event(event)  # handle the screen panning

            # Spawn enemies
            if random.random() < 0.01:  # 1% chance per frame
            # if random.random() < 0.10:  # 10% chance per frame
            # if random.random() < 0.50:  # 50% chance per frame
                enemies.spawn_enemy(settlements.get_city_settlement().rect.center, 20, 20, 50, 5)

            # Update enemies
            enemies.update_enemies(dt)

            for enemy in enemies.enemies:
                if not enemy.rect.collidelist(settlements.settlements) == -1:
                    print("should remove this enemy and add inflict damage on the settlement")


            window.fill((60, 60, 90))

            # in-game (beneath the shop)
        
            screen.draw_objects(connections.connections)

            screen.draw_objects(enemies.enemies)

            if settlements.get_temp_settlement():
                for settlement in settlements.settlements:
                    temp = settlements.get_temp_settlement()
                    if pygame.Vector2(settlement.location).distance_to(mouse_pos) <= temp.range and not settlements.is_too_close_to_other_settlement(temp.rect):
                        if temp.type == 'basic_relay' and settlement.relay:
                            pygame.draw.line(window, 'black', ((mouse_pos[0]), mouse_pos[1]), (settlement.location[0], settlement.location[1]))
                        elif not temp.type == 'basic_relay':
                            pygame.draw.line(window, 'black', ((mouse_pos[0]), mouse_pos[1]), (settlement.location[0], settlement.location[1]))
                    
            
            screen.draw_objects(settlements.settlements)

            for settlement in settlements.settlements:
                if settlement.type == 'basic_earner':
                    if settlement.earning_cooldown_timer >= settlement.earning_cooldown:
                        money += settlement.earning_rate
                        settlement.earning_cooldown_timer = 0
                    else:
                        settlement.earning_cooldown_timer += 1

                if settlement.type == 'basic_defender':
                    if settlement.cooldown > settlement.cooldown_limit and enemies.enemies:
                        if pygame.Vector2(settlement.rect.center).distance_to(settlement.closest_enemy(enemies.enemies)) <= settlement.projectile_range:
                            settlement.fire_bullet(settlement.closest_enemy(enemies.enemies))
                    else:
                        settlement.cooldown += 1

                    for bullet in settlement.bullets:
                        if not bullet.rect.collidelist(enemies.enemies) == -1:
                            enemies.damage_enemy(enemies.enemies[bullet.rect.collidelist(enemies.enemies)], bullet.damage)
                            settlement.bullets.remove(bullet)

                    settlement.update_bullets(dt)
                    screen.draw_objects(settlement.bullets)

                    if settlement.mouse_over(mouse_pos):
                        pygame.draw.circle(window, "red", settlement.location, settlement.projectile_range_max, 1)
                        pygame.draw.circle(window, "green", settlement.location, settlement.projectile_range, 1)

                

            # # shop
            pygame.draw.rect(window, (60, 60, 40), (0, 475, 925, 125))
            pygame.draw.rect(window, (0, 0, 0), (0, 475, 925, 125), 5)

            buttons.draw_buttons(window)


            # in-game (above the shop)

            if settlements.does_temp_settlement_exists():
                temp = settlements.get_temp_settlement()
                if settlements.is_too_close_to_other_settlement(temp.rect):
                    temp.color = temp.color_when_cannot_place
                else:
                    temp.color = temp.normal_color

                settlements.draw_temp_settlement(window, mouse_pos)

            draw_text_topleft(window, f"money: {money}", 24, "white", 10, 10)


            # end of loop conditions and checks
            

        

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()