import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 800
NODE_RADIUS = 20
NODE_COLOR = (255, 255, 255)
EDGE_COLOR = (200, 200, 200)
PLAYER_COLOR = (255, 0, 0)
GOAL_COLOR = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a dictionary to store the node positions
node_positions = {
    0: (100, 100),
    1: (200, 200),
    2: (300, 300),
    3: (400, 400),
    4: (500, 500),
    5: (600, 600),
}

# Draw the graph
def draw_graph(graph, player_node, goal_node):
    for node, edges in enumerate(graph.adjList):
        if node == player_node:
            color = PLAYER_COLOR
        elif node == goal_node:
            color = GOAL_COLOR
        else:
            color = NODE_COLOR
        pygame.draw.circle(screen, color, node_positions[node], NODE_RADIUS)
        for edge in edges:
            pygame.draw.line(screen, EDGE_COLOR, node_positions[node], node_positions[edge])

# Define the Graph class
class Graph:
    def __init__(self, edges, N):
        self.adjList = [[] for _ in range(N)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

# Specify edges of the graph
edges = [(0, 1), (1, 2), (2, 0), (2, 1), (3, 2), (4, 5), (3, 4)]

# Number of nodes in the graph
N = 6

# Construct graph
graph = Graph(edges, N)

# Set the player and goal nodes
player_node = 0
goal_node = 5

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if player_node > 0:
                    player_node -= 1
            elif event.key == pygame.K_RIGHT:
                if player_node < N - 1:
                    player_node += 1

    screen.fill((0, 0, 0))
    draw_graph(graph, player_node, goal_node)
    pygame.display.flip()

    if player_node == goal_node:
        print("You won!")
        running = False

pygame.quit()
sys.exit()
