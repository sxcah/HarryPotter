import pygame as py, sys

from settings import *
from assets import *
from support import *
from game_state_control import handle_game_state_event

from game import Game


py.init()

display_surface = py.display.set_mode((0, 0), py.RESIZABLE)

class Main():
    def __init__(s):
        s.clock = py.time.Clock()

        s.game_state = {
                        'menu': 'menu',
                        'game': 'game',
                        'pause': 'pause',
                        'game_over': 'game_over',
                        'victory': 'victory'
                        }
        
        s.game_current_state = s.game_state['game']

        s.game = Game()

    def run(s):
        running = True
        while running:
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False

                new_state = handle_game_state_event(event, s.game_current_state)
                if new_state:
                    s.game_current_state = new_state

            if s.game_current_state == 'menu':
                display_surface.fill((255, 255, 255))
            elif s.game_current_state == 'game':
                s.game.display()
            elif s.game_current_state == 'pause':
                display_surface.fill((155, 155, 155))
            else:
                pass

            py.display.flip()
            s.clock.tick(FPS)

        py.quit()
        sys.exit()

if __name__ == "__main__":
    main = Main()
    main.run()