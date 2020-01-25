import pygame

from colors import WHITE_DR, GREEN_DR, YELLOW_DR

pygame.font.init()


def create_font(size, bold=False):
    return pygame.font.SysFont("menlo", size, bold=bold)


def white_font(font, text):
    return font.render(text, 1, WHITE_DR)


def green_font(font, text):
    return font.render(text, 1, GREEN_DR)


def yellow_font(font, text):
    return font.render(text, 1, YELLOW_DR)
