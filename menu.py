import pygame as py
from support import *
from assets import *

class Menu():
    def __init__(s):
        s.display_surface = py.display.get_surface()
        s.display_w = s.display_surface.get_width()
        s.display_h = s.display_surface.get_height()
        
        s.font = load_font(font, font_size)
        
    def display(s):
        s.display_surface.fill((255, 255, 255))
        
        display_text(
            s.display_surface,
            s.font['med'],
            "Menu Screen\nPress \"Enter\" to play the Game!",
            (0, 0, 0),
            None,
            55
        )