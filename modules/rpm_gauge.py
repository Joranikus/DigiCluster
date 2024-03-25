#rpm_gauge.py
import pygame
from modules.stuff import ImageSprite

class RPMGauge:
    """
    A class representing an RPM gauge, managing the display of individual gauge bars.
    Each bar is a unique image.
    
    Attributes:
        bars (list): A list of ImageSprite instances representing each bar in the gauge.
    """
    
    def __init__(self, base_image_path, positions):
        """
        Initialize the RPM gauge with positions and a base path for its bar images.
        It is assumed that images are named sequentially as rpm_1.png, rpm_2.png, etc.

        Args:
            base_image_path (str): The base path to the image files used for the bars.
            positions (list): A list of (x, y) tuples representing the positions of individual bars.
        """
        self.bars = []
        for i, pos in enumerate(positions):
            image_path = f'{base_image_path}rpm_{i+1}.png'  # Construct the image path for each bar
            self.bars.append(ImageSprite(image_path, pos))

    def set_rpm(self, rpm):
        """
        Set the RPM value for the gauge, which determines the number of active bars.

        Args:
            rpm (int): The RPM value to be displayed by the gauge.
        """
        active_bars = rpm // 100  # Determine the number of bars to activate based on the RPM value
        for i, bar in enumerate(self.bars):
            if i < active_bars:
                bar.activate()
            else:
                bar.deactivate()

    def draw(self, screen):
        """
        Draw the gauge on the screen, showing the active bars based on the current RPM.

        Args:
            screen (Surface): The Pygame screen surface where the gauge will be drawn.
        """
        for bar in self.bars:
            if bar.active:
                bar.draw(screen)