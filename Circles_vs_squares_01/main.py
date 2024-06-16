import pygame

from settlements import Settlements

# pygame setup
pygame.init()

WIDTH, HEIGHT = 900, 600 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

settlements = Settlements()


while running:
    mouse_posx, mouse_posy = pygame.mouse.get_pos()
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            settlements.create_settlement(mouse_posx, mouse_posy, 50, 'white')

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((30, 30, 60))

    settlements.update_settlements(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()