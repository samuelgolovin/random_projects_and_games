import pygame

from settlements import Settlements

# pygame setup
pygame.init()

WIDTH, HEIGHT = 925, 600 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

settlements = Settlements()

settlements.create_button(25, 500, 75, 75, (200, 200, 200), 'basic_earner')
settlements.create_button(125, 500, 75, 75, (200, 200, 200), 'basic_defender')
settlements.create_button(225, 500, 75, 75, (200, 200, 200), 'basic_relay')
settlements.create_button(325, 500, 75, 75, (200, 200, 200), 'basic_efficiency')
settlements.create_button(425, 500, 75, 75, (200, 200, 200), 'advanced_defender')
settlements.create_button(525, 500, 75, 75, (200, 200, 200), 'advanced_relay')
settlements.create_button(625, 500, 75, 75, (200, 200, 200), 'advanced_earner')
settlements.create_button(725, 500, 75, 75, (200, 200, 200), 'advanced_efficiency')
settlements.create_button(825, 500, 75, 75, (200, 200, 200), 'city')


while running:
    mouse_pos = pygame.mouse.get_pos()
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP and settlements.over_button(mouse_pos):
            settlements.create_settlement(mouse_pos[0], mouse_pos[1], 10, 'white')
        if event.type == pygame.MOUSEBUTTONDOWN and settlements.check_if_bought():
            settlements.set_settlement()


    # fill the screen with a color to wipe away anything from last frame
    screen.fill((60, 60, 90))

    pygame.draw.rect(screen, (60, 60, 40), (0, 475, 925, 125))
    pygame.draw.rect(screen, (0, 0, 0), (0, 475, 925, 125), 5)


    settlements.update_settlements(screen)
    settlements.update_buttons(screen)

    for settlement in settlements.settlements:
        if settlement.bought == True:
            settlement.update_pos_before_placed(mouse_pos)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()