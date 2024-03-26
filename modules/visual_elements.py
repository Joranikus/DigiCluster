import pygame
import os

class ImageSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, position):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()  # Load and convert with transparency
        self.rect = self.image.get_rect(topleft=position)
        self.active = True  # Attribute to control visibility

    def activate(self):
        """Make the sprite visible."""
        self.active = True

    def deactivate(self):
        """Make the sprite invisible."""
        self.active = False

    def draw(self, surface):
        """Draw the sprite on the surface if it's active."""
        if self.active:
            surface.blit(self.image, self.rect)

class PlaceObject:
    """
    A simple class for managing and drawing the background.

    Attributes:
        image (Surface): The Pygame surface containing the background image.
    """

    def __init__(self, image_path):
        """
        Initializes the Background with the given image path.

        Args:
            image_path (str): Path to the background image file.
        """
        self.image = pygame.image.load(image_path).convert_alpha()  # Load and convert with transparency

    def draw(self, screen):
        """
        Draws the background onto the provided screen.

        Args:
            screen (Surface): The Pygame screen surface where the background will be drawn.
        """
        screen.blit(self.image, (0, 0))

class LightsManager:
    WARNING_LIGTHS_ASSETS_FOLDER = 'images/lights/lights'

    def __init__(self, lights_folder=None, position=(0, 0)):
        self.lights = {}
        self.active_lights = set()
        self.base_position = position

        if not lights_folder:
            lights_folder = self.WARNING_LIGTHS_ASSETS_FOLDER

        for filename in os.listdir(lights_folder):
            if filename.endswith('.png'):
                image_path = os.path.join(lights_folder, filename)
                key, _ = os.path.splitext(filename)
                self.lights[key] = ImageSprite(image_path, position)

    def set_value(self, key, value):
        """Set the visibility of a light based on a boolean value."""
        if key in self.lights:
            if value:
                self.active_lights.add(key)
            else:
                self.active_lights.discard(key)

    def draw(self, surface):
        """Draw all active lights."""
        for key in self.active_lights:
            self.lights[key].draw(surface)
