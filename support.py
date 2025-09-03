import pygame as py
import os

py.init()

def load_image(path, colorkey=None):
    try:
        image = py.image.load(path)
        image = image.convert_alpha() if image.get_alpha() else image.convert()
        if colorkey is not None:
            image.set_colorkey(colorkey)
        return image
    except Exception as e:
        print(f"Failed to load image: {path}\n{e}")
        return None

def load_images_from_folder(folder, colorkey=None):
    images = {}
    for filename in os.listdir(folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
            path = os.path.join(folder, filename)
            images[filename] = load_image(path, colorkey)
    return images

def load_font(font, font_size):
    fonts = {}

    for size_key, size in font_size.items():
        fonts[size_key] = py.font.Font(font, size)

    return fonts
        
def display_text(display, font, text, color, center=None, spacing=0):
    fonts = font
    lines = text.split('\n')
    line_spacing = spacing        

    if center is None:
        center = (display.get_width() // 2, display.get_height() // 2)

    total_height = len(lines) * line_spacing
    start_y = center[1] - (total_height // 2)

    for i, line in enumerate(lines):
        text_surf = fonts.render(line, True, color)
        text_rect = text_surf.get_rect(center=(center[0], start_y + i * line_spacing))
        blit_surface(text_surf, text_rect)

def dim_overlay(surface, color, alpha):
    overlay = py.Surface(surface.get_size(), py.SRCALPHA)
    overlay.fill(color)
    overlay.set_alpha(alpha)
    
    surface.blit(overlay, (0, 0))

def scale_to_screen_blit_surface(surface_image):
    display_surface = py.display.get_surface()
    surface = py.transform.scale(surface_image, display_surface.get_size())
    display_surface.blit(surface, (0, 0))

def blit_surface(surface, pos=(0, 0)):
    display_surface = py.display.get_surface()
    if surface and display_surface:
        display_surface.blit(surface, pos)
        return True