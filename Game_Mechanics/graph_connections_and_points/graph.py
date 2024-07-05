import pygame
import sys
import math

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Mechanic Test")

class Node:
    def __init__(self, position, type):
        self.position = position
        self.type = type

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node, node_location, node_type):
        if node not in self.graph:
            self.graph[node] = [Node(node_location, node_type)]

    def add_connection(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)
        else:
            print("Error: Both nodes must exist in the graph")

    def get_nodes(self):
        return list(self.graph.keys())
    
    def get_connections(self, node):
        if node in self.graph:
            return self.graph[node][1:]
        else:
            print(f"Error: {node} does not exist in the graph.")
            return []
        