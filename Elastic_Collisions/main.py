# Example file showing a circle moving on screen
import pygame


class Circle:
    def __init__(self, pos, radius, velocity):
        self.pos = pos
        self.radius = radius
        self.velocity = velocity
        self.mass = radius * 2

    def draw(self, screen):
        pygame.draw.circle(screen, 'gray', self.pos, self.radius)

    def update(self):
        if self.pos[0] - self.radius < 0:
            self.pos[0] = self.radius
            self.velocity[0] *= -1
        if self.pos[1] - self.radius < 0:
            self.pos[1] = self.radius
            self.velocity[1] *= -1
        if self.pos[0] + self.radius > screen.get_width():
            self.pos[0] = screen.get_width() - self.radius
            self.velocity[0] *= -1
        if self.pos[1] + self.radius > screen.get_height():
            self.pos[1] = screen.get_height() - self.radius
            self.velocity[1] *= -1


        self.pos += self.velocity

    def update_velocity(self, change_to_velocity):
        self.velocity += change_to_velocity



# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

circles = [Circle(pygame.Vector2(100, 100), 20, pygame.Vector2(-5, -5)), Circle(pygame.Vector2(140, 500), 40, pygame.Vector2(-2, -2))]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    for circle in circles:
        circle.update()
        circle.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()






