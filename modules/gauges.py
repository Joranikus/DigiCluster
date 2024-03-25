# gauges.py
import pygame
from modules.stuff import ImageSprite

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
        self.bars = [True] * max_bars  # Initialize all bars to 'off'
    
    def set_value(self, value):
        normalized_value = (value - self.min_value) / (self.max_value - self.min_value)
        num_active_bars = int(normalized_value * self.max_bars)
        for i, bar in enumerate(self.bars):
            bar.active = i < num_active_bars



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

class OilPressureGauge(VerticalBarGauge):
    """
    A class representing an oil pressure gauge in Pygame, showing only one image at a time
    based on the current oil pressure value.
    """
    OIL_PRESSURE_GAUGE_ASSET_PATH = 'images/bars/oil_pressure/'

    def __init__(self, position, min_value, max_value):
        """
        Initializes the oil pressure gauge with a position and value range. The gauge
        will display a specific image based on the current value.

        Args:
            position (tuple): The position of the gauge on the screen.
            min_value (float): The minimum value the gauge can represent.
            max_value (float): The maximum value the gauge can represent.
        """
        super().__init__(self.OIL_PRESSURE_GAUGE_ASSET_PATH + 'oil_pressure_1.png', 20, position, min_value, max_value)
        self.current_bar = None

    def set_value(self, value):
        """
        Sets the oil pressure value and updates the gauge to display the corresponding image.

        Args:
            value (float): The current oil pressure value.
        """
        normalized_value = (value - self.min_value) / (self.max_value - self.min_value)
        bar_index = int(normalized_value * 20)  # Assuming 20 total images

        # Clamp the index to be within the range of available images
        bar_index = max(1, min(bar_index, 20))

        # Update the current bar image based on the value
        if self.current_bar != bar_index:
            self.current_bar = bar_index
            self.bar_image = pygame.image.load(self.OIL_PRESSURE_GAUGE_ASSET_PATH + f'oil_pressure_{self.current_bar}.png')

    def draw(self, screen):
        """
        Draws the current bar image on the screen at the gauge's position.
        """
        if self.bar_image:  # Ensure there is an image to draw
            screen.blit(self.bar_image, self.position)


