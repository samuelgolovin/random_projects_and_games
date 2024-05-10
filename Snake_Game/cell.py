import pygame

class Cell:
    def __init__(self, i, j, w):
        self.i = i
        self.j = j
        self.x = i * w
        self.y = j * w
        self.w = w
        self.is_snake_body = False
        self.is_snake_head = False