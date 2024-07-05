import heapq
import math

class Node:
    def __init__(self, position, type):
        self.position = position
        self.type = type

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

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
        x1, y1 = self.graph[node1].position
        x2, y2 = self.graph[node2].position
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