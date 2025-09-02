import pygame as py

def handle_game_state_event(event, current_state):
    pressed_key = py.KEYDOWN
    if event.type == pressed_key:
        if event.key == py.K_ESCAPE:
            if current_state == 'pause':
                return 'menu'
        
        if event.key == py.K_RETURN:
            if current_state == 'menu':
                return 'game'
            elif current_state == 'pause':
                return 'game'

        if event.key == py.K_BACKSPACE:
            if current_state == 'game':
                return 'pause'