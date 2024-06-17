import pygame

# Initialize Pygame
pygame.init()

x, y = 400, 400

# Set up the screen (replace x and y with your desired dimensions)
screen = pygame.display.set_mode((x, y))

# Define the circle parameters
center = (x / 2, y / 2)  # Center coordinates
radius = 20       # Radius of the circle
border_width = 2  # Thickness of the circle border

# Draw the circle
pygame.draw.circle(screen, (0, 0, 255), center, radius, border_width)

# Update the display
pygame.display.update()

# Main loop (you can adapt this to your specific use case)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Clean up
pygame.quit()
