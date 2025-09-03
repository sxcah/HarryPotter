import pygame as py

from support import *
from assets import *

class Pause():
    def __init__(s):
        s.display_surface = py.display.get_surface()
        s.display_w = s.display_surface.get_width()
        s.display_h = s.display_surface.get_height()
        
        s.font = load_font(font, font_size)
        
    def display(s):
        dim_overlay(
            s.display_surface,
            (155, 155, 155),
            155
        )
        
        display_text(
            s.display_surface,
            s.font['med'],
            f"Game Pause!\nPress \"Enter\" to resume game!",
            (255, 255, 255),
            None,
            50
        )
        
        display_text(
            s.display_surface,
            s.font['med'],
            f"Press \"ESC\" to return to menu!",
            (0, 0, 0),
            None,
            (50 * -2 )
            
        )