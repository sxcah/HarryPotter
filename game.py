from support import *
from assets import *

class Game():
    def __init__(s):
        s.display_surface = py.display.get_surface()
        s.display_w, s.display_h = s.display_surface.get_width(), s.display_surface.get_height()

        s.background = load_image(MAP)

    def display_background(s):
        scale_to_screen_blit_surface(s.background)

    def display(s):
        s.display_background()

