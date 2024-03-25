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