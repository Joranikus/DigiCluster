import pygame

class ImageSprite:
    """
    A class to represent and handle an image as a sprite in Pygame.
    
    Attributes:
        image (Surface): The Pygame surface containing the image of the sprite.
        position (tuple): The (x, y) position where the sprite will be drawn on the screen.
    """
    
    def __init__(self, image_path, position=(0, 0)):
        """
        Initialize the sprite with an image and its position.

        Args:
            image_path (str): The path to the image file.
            position (tuple): The (x, y) coordinates for the sprite's position on the screen.
        """
        self.image = pygame.image.load(image_path)
        self.position = position

    def draw(self, screen):
        """
        Draw the sprite onto the screen at its current position.

        Args:
            screen (Surface): The Pygame screen surface where the sprite will be drawn.
        """
        screen.blit(self.image, self.position)

class RPMGauge:
    """
    A class representing an RPM gauge, managing the activation and display of individual gauge bars.
    
    Attributes:
        bars (list): A list of ImageSprite instances representing each bar in the gauge.
    """
    
    def __init__(self, positions, image_path):
        """
        Initialize the RPM gauge with positions and image for its bars.

        Args:
            positions (list): A list of (x, y) tuples representing the positions of individual bars.
            image_path (str): The path to the image file used for each bar.
        """
        self.bars = [ImageSprite(image_path, pos) for pos in positions]

    def set_rpm(self, rpm):
        """
        Set the RPM value for the gauge, which determines the number of active bars.

        Args:
            rpm (int): The RPM value to be displayed by the gauge.
        """
        for i, bar in enumerate(self.bars):
            bar.active = i < rpm

    def draw(self, screen):
        """
        Draw the gauge on the screen, showing the active bars based on the current RPM.

        Args:
            screen (Surface): The Pygame screen surface where the gauge will be drawn.
        """
        for bar in self.bars:
            if bar.active:
                bar.draw(screen)

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
