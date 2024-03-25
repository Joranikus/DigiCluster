import pygame
from modules.stuff import ImageSprite
from datetime import datetime

class SevenSegmentClock:
    # Default paths for digit and colon images
    DEFAULT_DIGIT_ASSETS_FOLDERS = [
        'images/clock/digit_1',
        'images/clock/digit_2',
        'images/clock/digit_3',
        'images/clock/digit_4'
    ]
    DEFAULT_COLON_ASSET_PATH = 'images/clock/colon.png'

    def __init__(self, position=(0, 0), folders=None, colon_path=None):
        # Use provided folders and colon_path if given, otherwise use the default constants
        digit_folders = folders if folders is not None else self.DEFAULT_DIGIT_ASSETS_FOLDERS
        colon_asset_path = colon_path if colon_path is not None else self.DEFAULT_COLON_ASSET_PATH

        self.digit_images = []
        for folder in digit_folders:
            # Load images named '0.png' to '9.png' for each digit
            images = [pygame.image.load(f"{folder}/{i}.png") for i in range(10)]
            self.digit_images.append(images)

        # Load the colon image
        self.colon_image = pygame.image.load(colon_asset_path)

        # Store the position where the clock will be drawn
        self.position = position

        # Initialize digits to midnight
        self.digits = [0, 0, 0, 0]  # Representing HHMM

    def set_time_now(self):
        # Fetch the current local time
        now = datetime.now()
        # Set the clock to the current time
        self.set_time(now.hour, now.minute)
        
    def set_time(self, hours, minutes):
        # Update the digits list with the new time, ensuring two digits for hours and minutes
        self.digits = [hours // 10, hours % 10, minutes // 10, minutes % 10]

    def draw(self, surface):
        # Since the images are pre-positioned, draw each digit at the same position
        for i, digit in enumerate(self.digits):
            # Select the correct image for the current digit
            image = self.digit_images[i][digit]
            surface.blit(image, self.position)

            # If i is 1, it means we just drew the second digit of the hours, so draw the colon next
            if i == 1:
                surface.blit(self.colon_image, self.position)

class BatteryVoltageDisplay:
    DEFAULT_DIGIT_ASSETS_FOLDERS = [
        'images/voltage_display/digit_1',
        'images/voltage_display/digit_2',
        'images/voltage_display/digit_3'
    ]
    DEFAULT_DOT_ASSET_PATH = 'images/voltage_display/dot.png'

    def __init__(self, position=(0, 0), folders=None, dot_path=None):
        # Use provided folders and dot_path if given, otherwise use the default constants
        digit_folders = folders if folders is not None else self.DEFAULT_DIGIT_ASSETS_FOLDERS
        dot_asset_path = dot_path if dot_path is not None else self.DEFAULT_DOT_ASSET_PATH

        self.digit_images = []
        for folder in digit_folders:
            # Load images named '0.png' to '9.png' for each digit
            images = [pygame.image.load(f"{folder}/{i}.png") for i in range(10)]
            self.digit_images.append(images)

        # Load the dot image
        self.dot_image = pygame.image.load(dot_asset_path)

        # Store the position where the voltage will be drawn
        self.position = position

        # Initialize digits to 0.0V (assuming a format like X.XV)
        self.digits = [0, 0, 0]  # Representing the voltage as X.XX
    def set_value(self, voltage):
        clamped_voltage = max(9.0, min(voltage, 15.9))  # Adjust the range as needed
        int_voltage = int(clamped_voltage * 10)  # Convert to XX.X format
        self.digits = [int_voltage // 100,  # Tens
                    (int_voltage % 100) // 10,  # Ones
                    int_voltage % 10]  # Tenths


    def draw(self, surface):
        # Draw each digit at the base position
        for i, digit in enumerate(self.digits):
            image = self.digit_images[i][digit]
            surface.blit(image, self.position)  # No offset, draw at the base position

        # After the second digit (ones place), draw the dot
        if len(self.digits) > 2:  # Ensure there are enough digits
            surface.blit(self.dot_image, self.position)  # Draw the dot at the base position



