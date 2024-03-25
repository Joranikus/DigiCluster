import pygame

class ImageSprite:
    """
    A class to represent and handle an image as a sprite in Pygame.

    Attributes:
        image (Surface): The Pygame surface containing the image of the sprite.
        position (tuple): The (x, y) position where the sprite will be drawn on the screen.
        active (bool): Determines whether the sprite is active (visible) or not.
    """
    
    def __init__(self, image_path, position=(0, 0)):
        """
        Initialize the sprite with an image and its position.
        ...
        """
        self.image = pygame.image.load(image_path)
        self.position = position
        self.active = False  # Sprites are initially inactive

    def activate(self):
        """
        Activate the sprite, making it visible.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivate the sprite, making it invisible.
        """
        self.active = False

class SevenSegmentDisplay:
    """
    A class representing a seven-segment display for a clock in Pygame.
    
    Attributes:
        segments (dict): A dictionary holding ImageSprite instances for each segment.
        numbers (dict): A mapping from each number to its corresponding active segments.
        position (tuple): The top-left position for the entire display on the screen.
    """
    
    def __init__(self, segment_paths, position=(0, 0)):
        """
        Initialize the seven-segment display with the segments' image paths and position.

        Args:
            segment_paths (dict): A dictionary with keys 'A' to 'G' and 'DP' for decimal point,
                                  pointing to file paths of each segment image.
            position (tuple): The (x, y) position for the entire display on the screen.
        """
        self.position = position
        self.segments = {name: ImageSprite(path, position) for name, path in segment_paths.items()}
        self.numbers = {
            '0': ['A', 'B', 'C', 'D', 'E', 'F'],
            '1': ['B', 'C'],
            '2': ['A', 'B', 'D', 'E', 'G'],
            '3': ['A', 'B', 'C', 'D', 'G'],
            # ... other numbers up to '9'
            '8': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
            '9': ['A', 'B', 'C', 'D', 'F', 'G']
        }

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

    def get_segment_offset(self, segment, digit_position):
        """
        Gets the offset for the given segment within a digit.

        Args:
            segment (str): The segment for which to get the offset.
            digit_position (int): The position (0-3) of the digit to draw.

        Returns:
            tuple: The offset as an (x, y) tuple.
        """
        # Define offsets for each segment here. These should be tuples indicating
        # the x and y offset from the top-left corner of each digit.
        segment_offsets = {
            'A': (0, 0),
            'B': (30, 5),  # Example offsets
            'C': (30, 35),
            'D': (0, 70),
            'E': (5, 35),
            'F': (5, 5),
            'G': (0, 35),
            'DP': (35, 70)  # Assuming 'DP' stands for Decimal Point
        }
        
        # Determine the x-offset based on the digit position
        x_offset_multiplier = 50  # Adjust this value based on the width of your segments
        x_offset = x_offset_multiplier * digit_position

        # Get the base offset for the segment
        base_offset = segment_offsets[segment]

        # Return the adjusted offset
        return (base_offset[0] + x_offset, base_offset[1])

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
