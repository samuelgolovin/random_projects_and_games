import pygame
import sys

def main():
    pygame.init()

    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        screen.fill('black')


        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()