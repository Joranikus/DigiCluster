# gauges.py
import pygame
from modules.stuff import ImageSprite

class Gauge:
    def __init__(self, asset_path, position, min_value, max_value, max_bars=20, single_image_mode=False):
        self.position = position
        self.min_value = min_value
        self.max_value = max_value
        self.max_bars = max_bars
        self.asset_path = asset_path
        self.single_image_mode = single_image_mode  # Indicates whether the gauge uses single image mode
        self.current_bar_index = 1 if single_image_mode else None  # Track the current image index if in single image mode
        self.bar_image = None if single_image_mode else pygame.image.load(f'{self.asset_path}{1}.png')  # Load the first image or None

    def set_value(self, value):
        normalized_value = (value - self.min_value) / (self.max_value - self.min_value)
        new_bar_index = int(normalized_value * self.max_bars) + 1

        if self.single_image_mode:
            # For gauges that show a single image based on the value
            new_bar_index = max(1, min(new_bar_index, self.max_bars))
            if self.current_bar_index != new_bar_index:
                self.current_bar_index = new_bar_index
                self.bar_image = pygame.image.load(f'{self.asset_path}{self.current_bar_index}.png')
        else:
            # For traditional vertical bar gauges with multiple bars
            for i in range(self.max_bars):
                self.bars[i].active = i < new_bar_index

    def draw(self, screen):
        if self.single_image_mode:
            # Draw the current image for single image mode gauges
            if self.bar_image:
                screen.blit(self.bar_image, self.position)
        else:
            # Draw each active bar for traditional vertical bar gauges
            for i, bar in enumerate(self.bars):
                if bar.active:
                    y_position = self.position[1] - (i * self.bar_height)
                    screen.blit(self.bar_image, (self.position[0], y_position))

class RPMGauge(Gauge):
    def __init__(self, asset_path, position, min_value, max_value, max_bars):
        super().__init__(asset_path, position, min_value, max_value, max_bars, single_image_mode=True)
        self.step_value = (max_value - min_value) / (max_bars - 1)  # Calculate the step value based on the range and number of bars

    def set_value(self, value):
        """
        Sets the RPM value and updates the gauge to display the corresponding image.

        Args:
            value (float): The current RPM value, clamped to the min and max values.
        """
        # Ensure the value is within the valid range
        value = max(self.min_value, min(value, self.max_value))

        # Calculate the index for the image corresponding to the current RPM value
        # This calculation assumes images are named for every 100 RPM from 100 to 7000
        new_rpm_index = int((value + 99) // 100)  # Adding 99 to ensure proper rounding up for every 100 RPM

        # Ensure the new index falls within the range of available images
        new_rpm_index = max(1, min(new_rpm_index, self.max_bars))

        # Update the current RPM image if the index has changed
        if self.current_bar_index != new_rpm_index:
            self.current_bar_index = new_rpm_index
            # Load the corresponding image based on the current_rpm_index
            image_filename = f'rpm_{self.current_bar_index * 100}.png'
            self.bar_image = pygame.image.load(f'{self.asset_path}{image_filename}')


    def draw(self, screen):
        """
        Draws the current RPM image on the screen at the gauge's position.
        """
        if self.bar_image:  # Ensure there is an image to draw
            screen.blit(self.bar_image, self.position)

import time

class RpmGaugeAnimation:
    def __init__(self, rpm_gauge, animation_duration=3):
        self.rpm_gauge = rpm_gauge
        self.animation_duration = animation_duration
        self.start_time = None
        self.startup_animation_active = False

    def start_animation(self):
        self.start_time = time.time()
        self.startup_animation_active = True

    def update(self):
        if not self.startup_animation_active or self.start_time is None:
            return

        current_time = time.time()
        elapsed_time = current_time - self.start_time

        if elapsed_time <= self.animation_duration:
            progress = elapsed_time / self.animation_duration

            if progress <= 0.5:
                value = self.rpm_gauge.min_value + (self.rpm_gauge.max_value - self.rpm_gauge.min_value) * (progress * 2)
            else:
                value = self.rpm_gauge.max_value - (self.rpm_gauge.max_value - self.rpm_gauge.min_value) * ((progress - 0.5) * 2)

            self.rpm_gauge.set_value(value)
        else:
            self.startup_animation_active = False

    def draw(self, surface):
        if self.startup_animation_active:
            self.rpm_gauge.draw(surface)
