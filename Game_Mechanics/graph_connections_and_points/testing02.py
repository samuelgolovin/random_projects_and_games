class Node:
    def __init__(self, position, type):
        self.position = position
        self.type = type

example_dict = {"A": Node((10, 10), 'basic'), 'B': Node((10, 10), 'super')}

print(example_dict['A'].position)