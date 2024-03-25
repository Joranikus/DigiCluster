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
