import pygame

class ImageSprite:
    """
    A class to represent and handle an image as a sprite in Pygame.
    ...
    """

    def __init__(self, image_path, position=(0, 0)):
        """
        Initialize the sprite with an image and its position.
        ...
        """
        self.image = pygame.image.load(image_path)
        self.position = position
        self.active = True  # Default to active, but can be toggled off

    def draw(self, screen):
        if self.active:
            screen.blit(self.image, self.position)


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
        self.image = pygame.image.load(image_path)

    def draw(self, screen):
        """
        Draws the background onto the provided screen.

        Args:
            screen (Surface): The Pygame screen surface where the background will be drawn.
        """
        screen.blit(self.image, (0, 0))