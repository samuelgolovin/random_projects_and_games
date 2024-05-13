# Example file showing a circle moving on screen
import pygame
from button import Button

# pygame setup
pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

buttons = [
    # number buttons
    Button(110, 500, 80, 80, "0", "lightgray"),
    Button(10, 400, 80, 80, "1", "lightgray"),
    Button(110, 400, 80, 80, "2", "lightgray"),
    Button(210, 400, 80, 80, "3", "lightgray"),
    Button(10, 300, 80, 80, "4", "lightgray"),
    Button(110, 300, 80, 80, "5", "lightgray"),
    Button(210, 300, 80, 80, "6", "lightgray"),
    Button(10, 200, 80, 80, "7", "lightgray"),
    Button(110, 200, 80, 80, "8", "lightgray"),
    Button(210, 200, 80, 80, "9", "lightgray"),
    # operation buttons on the right
    Button(310, 500, 80, 80, "+", "lightgray"),
    Button(310, 400, 80, 80, "-", "lightgray"),
    Button(310, 300, 80, 80, "/", "lightgray"),
    Button(310, 200, 80, 80, "*", "lightgray"),
    # operation buttons on the top
    Button(210, 120, 180, 60, "<---", "lightgray"),
    Button(10, 120, 180, 60, "C", "lightgray"),
]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for button in buttons:
                if button.mouse_on_button(mouse_x, mouse_y):
                    print(button.text)

    screen.fill("white")

    for button in buttons:
        button.draw(screen)


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    clock.tick(60)

pygame.quit()