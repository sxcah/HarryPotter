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

def scale_to_screen_blit_surface(surface_image):
    display_surface = py.display.get_surface()
    surface = py.transform.scale(surface_image, display_surface.get_size())
    display_surface.blit(surface, (0, 0))

def blit_surface(surface, pos=(0, 0)):
    display_surface = py.display.get_surface()
    if surface and display_surface:
        display_surface.blit(surface, pos)
        return True