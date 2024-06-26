# text_utils.py
import pygame

def draw_text_center(screen, text, textsize, color, x, y):
    pygame.font.init()
    font = pygame.font.Font(None, textsize)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def draw_text_topleft(screen, text, textsize, color, x, y):
    pygame.font.init()
    font = pygame.font.Font(None, textsize)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

def draw_text_midtop(screen, text, textsize, color, x, y):
    pygame.font.init()
    font = pygame.font.Font(None, textsize)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

def draw_text_topright(screen, text, textsize, color, x, y):
    pygame.font.init()
    font = pygame.font.Font(None, textsize)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topright = (x, y)
    screen.blit(text_surface, text_rect)