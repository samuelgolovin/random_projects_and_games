import pygame

class PanScreen:
    def __init__(self, width, height, pan_limit_x, pan_limit_y):
        self.width = width
        self.height = height
        self.pan_limit_x = pan_limit_x
        self.pan_limit_y = pan_limit_y
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
        self.mouse_x = 0
        self.mouse_y = 0

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[1] < 475:
            if event.button == 1:
                self.dragging = True
                self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
            
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                new_offset_x = self.offset_x + mouse_x - self.mouse_x
                new_offset_y = self.offset_y + mouse_y - self.mouse_y
                
                # Check if the new offsets are within the limits
                if abs(new_offset_x) <= self.pan_limit_x:
                    self.offset_x = new_offset_x
                    self.mouse_x = mouse_x
                if abs(new_offset_y) <= self.pan_limit_y:
                    self.offset_y = new_offset_y
                    self.mouse_y = mouse_y

    def draw_objects(self, objects):
        for obj in objects:
            obj.draw(self.screen, self.offset_x, self.offset_y)
    

    def is_mouse_on_game(self, mouse_pos):
        return True if mouse_pos[1] < 475 else False
