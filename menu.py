import pygame as py
from support import *
from assets import *
from settings import *

class Menu():
    def __init__(s):
        s.display_surface = py.display.get_surface()
        s.display_w = s.display_surface.get_width()
        s.display_h = s.display_surface.get_height()
        
        s.font = load_font(FONT, FONT_SIZE)
        
    def display(s):
        dim_overlay(
            s.display_surface,
            (255, 255, 255),
            155
        )

        display_text(
            s.display_surface,
            s.font['med'],
            f"Harry Potter\nand the\nPhilosopher's Stone",
            (0, 0, 0),
            (s.display_w // 2, s.display_h // 2 + (10 * -20)),
            (55)
        )
        
        display_text(
            s.display_surface,
            s.font['med'],
            f"Press \"Enter\" to play the Game!",
            (0, 0, 0),
            (s.display_w // 2, s.display_h // 2 + (10 * 20)),
            55
        )