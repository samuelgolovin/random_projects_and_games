import heapq
import math
import pygame

class Shop:
    def __init__(self, node):
        self.type = node.type

        if node.type == 'A':
            self.rect = pygame.Rect(node.rect.center, (300, 200))

        if node.type == 'B':
            self.rect = pygame.Rect(node.rect.center, (150, 100))

        self.location = self.rect.topleft

    def draw(self, surface, offset_x, offset_y):
        self.location = (self.rect.topleft[0] + offset_x, self.rect.topleft[1] + offset_y)
        pygame.draw.rect(surface, "gray", ((self.location), (self.rect.size)), border_radius=5)
        pygame.draw.rect(surface, "black", (self.location, (self.rect.size)), 2, 5)

class Borders:
    def __init__(self, rect):
        self.rect = rect
        self.location = self.rect.topleft

    def draw(self, surface, offset_x, offset_y):
        self.location = (self.rect.topleft[0] + offset_x, self.rect.topleft[1] + offset_y)
        pygame.draw.rect(surface, (15, 48, 19), (self.location, self.rect.size))

class DrawLine:
    def __init__(self, node1, node2):
        self.start_pos = node1.rect.center
        self.end_pos = node2.rect.center

    def draw(self, surface, offset_x, offset_y):
        self.start_pos_location = (self.start_pos[0] + offset_x, self.start_pos[1] + offset_y)
        self.end_pos_location = (self.end_pos[0] + offset_x, self.end_pos[1] + offset_y)
        pygame.draw.line(surface, 'black', self.start_pos_location, self.end_pos_location)

class Node:
    def __init__(self, rect, type):
        self.rect = rect
        self.type = type

        self.rect_location = self.rect.topleft

        self.location = self.rect.center

    def draw(self, surface, offset_x, offset_y):
        self.location = (self.rect.centerx + offset_x, self.rect.centery + offset_y)
        pygame.draw.circle(surface, 'red', self.location, 15)
        pygame.draw.circle(surface, 'white', self.location, 15, 2)

        self.rect_location = (self.rect.topleft[0] + offset_x, self.rect.topleft[1] + offset_y)
        pygame.draw.rect(surface, 'black', (self.rect_location, self.rect.size), 1)

class Graph:
    def __init__(self):
        self.graph = {}
        self.connections_to_draw = []
        self.borders_to_draw = []
        self.shop = []

    def create_shop(self, node):
        self.shop.append(Shop(node))

    def on_node(self, mouse_pos):
        for node in self.get_nodes():
            if node.rect.collidepoint(mouse_pos):
                return True
        return False
    
    def get_selected_node(self, mouse_pos) -> Node:
        for node in self.get_nodes():
            if node.rect.collidepoint(mouse_pos):
                return node
    
    def add_border(self, rect):
        self.borders_to_draw.append(Borders(rect))

    def add_node(self, rect, type):
        node = Node(rect, type)
        if node not in self.graph:
            self.graph[node] = []
            return node

    def add_connection(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)
            self.connections_to_draw.append(DrawLine(node1, node2))
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
        x1, y1 = node1.rect.center
        x2, y2 = node2.rect.center
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