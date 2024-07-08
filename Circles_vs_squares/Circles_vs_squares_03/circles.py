import pygame
import heapq
import math

class Circle:
    def __init__(self, position, type):
        if type == 'farm':
            self.size = 10
            self.color = 'green'
        elif type == 'defender':
            self.size = 25
            self.color = 'blue'
        else:
            self.size = 100
            self.color = 'white'

        self.rect = pygame.Rect(position[0] - self.size / 2, position[1] - self.size / 2, self.size, self.size)
        self.location = self.rect.center

    def draw(self, surface, offset_x, offset_y):
        self.location = (self.rect.centerx + offset_x, self.rect.centery + offset_y)
        pygame.draw.circle(surface, self.color, self.location, self.rect.width / 2)
        pygame.draw.circle(surface, 'black', self.location, self.rect.width / 2, 2)

class Temp_Circle:
    def __init__(self, mouse_pos, type):
        if type == 'farm':
            self.size = 10
            self.color = 'green'
        elif type == 'defender':
            self.size = 25
            self.color = 'blue'
        else:
            self.size = 100
            self.color = 'white'

        self.rect = pygame.Rect(mouse_pos[0] - self.size / 2, mouse_pos[1] - self.size / 2, self.size, self.size)

    def draw(self, surface, mouse_pos):
        self.rect.update((mouse_pos[0] - self.size / 2, mouse_pos[1] - self.size / 2), (self.size, self.size))
        pygame.draw.circle(surface, self.color, self.rect.center, self.rect.width / 2)
        pygame.draw.circle(surface, 'black', self.rect.center, self.rect.width / 2, 2)

class CircleGraph:
    def __init__(self):
        self.graph = {}
        self.temp_circle_graph = []

    def add_node(self, position, type):
        node = Circle(position, type)
        if node not in self.graph:
            self.graph[node] = []
            return node

    def add_connection(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)
        else:
            print("Error: Both nodes must exist in the graph")

    def remove_connection(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].remove(node2)
            self.graph[node2].remove(node1)
        else:
            print("Error: Both nodes must exist in the graph")

    def get_nodes(self):
        return list(self.graph.keys())
    
    def get_connections(self, node):
        if node in self.graph:
            return self.graph[node]#[1:]
        else:
            print(f"Error: {node} does not exist in the graph.")
            return []
        
    def calculate_distance(self, node1, node2):
        x1, y1 = node1.position
        x2, y2 = node2.position
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
    def pathfinding(self, start, end):
        queue = [(0, start, [])]
        seen = set()
        while queue:
            (cost, node, path) = heapq.heappop(queue)
            if node not in seen:
                path = path + [node]
                seen.add(node)
                if node == end:
                    return path
                for connected_node in self.get_connections(node):
                    total_cost = cost + self.calculate_distance(node, connected_node)
                    heapq.heappush(queue, (total_cost, connected_node, path))
        return []
    


    def create_temp_circle(self, mouse_pos, type):
        self.temp_circle_graph.append(Temp_Circle(mouse_pos, type))

    def remove_temp_circle(self):
        for temp_circle in self.temp_circle_graph:
            self.temp_circle_graph.remove(temp_circle)

    def does_temp_circle_exists(self):
        return True if len(self.temp_circle_graph) > 0 else False

    def get_temp_circle(self):
        for temp_circle in self.temp_circle_graph:
            return temp_circle

    def draw_temp_circle(self, surface, mouse_pos):
        for temp_circle in self.temp_circle_graph:
            temp_circle.draw(surface, mouse_pos)