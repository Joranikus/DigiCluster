# gauges.py
import pygame

class VerticalBarGauge:
    """
    A class representing a vertical bar gauge display in Pygame.

    Attributes:
        max_bars (int): The maximum number of bars the gauge can display.
        position (tuple): The (x, y) position of the bottom bar on the screen.
        min_value (float): The minimum value the gauge can represent.
        max_value (float): The maximum value the gauge can represent.
        bar_image (Surface): The Pygame surface containing the image of a bar.
        bar_height (int): The height of a single bar.
        bars (list): A list of boolean values indicating the active state of each bar.
    """

    def __init__(self, image_path, max_bars, position, min_value, max_value):
        """
        Args:
            image_path (str): The file path to the bar image.
            max_bars (int): The total number of bars in the gauge.
            position (tuple): The position of the gauge on the screen.
            min_value (float): The minimum value the gauge can represent.
            max_value (float): The maximum value the gauge can represent.
        """
        self.max_bars = max_bars
        self.position = position
        self.min_value = min_value
        self.max_value = max_value
        self.bar_image = pygame.image.load(image_path)
        self.bar_height = self.bar_image.get_height()
        self.bars = [False] * max_bars  # Initialize all bars to 'off'

    def set_value(self, value):
        """
        Set the value of the gauge, which will update the active state of the bars.

        Args:
            value (float): The current value to represent on the gauge.
                           Must be between min_value and max_value.
        """
        normalized_value = (value - self.min_value) / (self.max_value - self.min_value)
        num_active_bars = int(normalized_value * self.max_bars)
        self.bars = [i < num_active_bars for i in range(self.max_bars)]

    def draw(self, screen):
        """
        Draw the active bars on the screen.

        Args:
            screen (Surface): The Pygame screen surface where the gauge will be drawn.
        """
        for i, active in enumerate(self.bars):
            if active:
                y_position = self.position[1] - (i * self.bar_height)
                screen.blit(self.bar_image, (self.position[0], y_position))