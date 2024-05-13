import pygame

class Snake:
    def __init__(self, cols, rows):
        self.body = [(cols // 2, rows // 2)]

        self.dir = (1, 0)

    def move(self, food):
        head_x, head_y = self.body[0]
        dx, dy = self.dir
        new_head = (head_x + dx, head_y + dy)
        self.body.insert(0, new_head)

        if not self.eat_food(food):
            self.body.pop()

    def eat_food(self, food):
        head_x, head_y = self.body[0]
        if (head_x, head_y) == food:
            return True
        return False
    
    def check_collision(self, cols, rows):
        head_x, head_y = self.body[0]
        if (
            head_x < 0
            or head_x >= cols
            or head_y < 0
            or head_y >= rows
            or len(self.body) != len(set(self.body))
        ):
            return True
        return False