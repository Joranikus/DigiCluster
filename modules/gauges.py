# gauges.py
import pygame
from modules.visual_elements import ImageSprite

class Gauge:
    def __init__(self, asset_path, position, min_value, max_value, max_bars=20, single_image_mode=False):
        self.position = position
        self.min_value = min_value
        self.max_value = max_value
        self.max_bars = max_bars
        self.asset_path = asset_path
        self.single_image_mode = single_image_mode  # Indicates whether the gauge uses single image mode
        self.current_bar_index = 1 if single_image_mode else None  # Track the current image index if in single image mode
        self.bar_image = None if single_image_mode else pygame.image.load(f'{self.asset_path}{1}.png').convert_alpha()  # Load the first image or None

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

def calculate_rpm_value(self, progress):
    """
    Calculate the RPM value based on the current progress of the animation.

    Args:
        progress (float): The current progress of the animation, ranging from 0.0 to 1.0.

    Returns:
        float: The calculated RPM value.
    """
    if progress <= 0.5:
        # In the first half of the animation, interpolate from min to max RPM
        value = self.rpm_gauge.min_value + (self.rpm_gauge.max_value - self.rpm_gauge.min_value) * (progress * 2)
    else:
        # In the second half, interpolate back from max to min RPM
        value = self.rpm_gauge.max_value - (self.rpm_gauge.max_value - self.rpm_gauge.min_value) * ((progress - 0.5) * 2)
    return value


class RPMGauge(Gauge):
    def __init__(self, asset_path, position, min_value, max_value, max_bars):
        super().__init__(asset_path, position, min_value, max_value, max_bars, single_image_mode=True)
        self.step_value = (max_value - min_value) / (max_bars - 1)  # Defines the RPM increase per step
        self.preloaded_images = [pygame.image.load(f'{asset_path}rpm_{i}00.png').convert_alpha() for i in range(1, max_bars + 1)]

    def set_value(self, value):
        # Calculate the appropriate index from the value
        new_rpm_index = int((value - self.min_value) / self.step_value)

        # Clamp the index to be within the list bounds
        new_rpm_index = max(0, min(new_rpm_index, len(self.preloaded_images) - 1))

        # Set the current bar image to the preloaded image
        self.bar_image = self.preloaded_images[new_rpm_index]

    def update(self):
        if not self.startup_animation_active or self.start_time is None:
            return

        current_time = time.time()
        delta_time = current_time - self.last_update_time
        self.last_update_time = current_time
        self.elapsed_time += delta_time

        if self.elapsed_time <= self.animation_duration:
            progress = self.elapsed_time / self.animation_duration
            value = self.calculate_rpm_value(progress)
            self.rpm_gauge.set_value(value)
        else:
            self.startup_animation_active = False

import time
class RpmGaugeAnimation:
    def __init__(self, rpm_gauge, animation_duration=3, start_delay=2):
        self.rpm_gauge = rpm_gauge
        self.animation_duration = animation_duration
        self.start_delay = start_delay  # Delay in seconds before animation starts
        self.start_time = None
        self.animation_started = False

    def start_animation(self):
        self.start_time = time.time()

    def update(self):
        if not self.animation_started:
            current_time = time.time()
            elapsed_time = current_time - self.start_time

            if elapsed_time >= self.start_delay:
                self.animation_started = True

        if self.animation_started:
            current_time = time.time()
            elapsed_time = current_time - (self.start_time + self.start_delay)

            if 0 <= elapsed_time <= self.animation_duration:
                progress = elapsed_time / self.animation_duration

                if progress <= 0.5:
                    value = self.rpm_gauge.min_value + (self.rpm_gauge.max_value - self.rpm_gauge.min_value) * (progress * 2)
                else:
                    value = self.rpm_gauge.max_value - (self.rpm_gauge.max_value - self.rpm_gauge.min_value) * ((progress - 0.5) * 2)

                self.rpm_gauge.set_value(value)
            else:
                # Ensure that the animation stops at the end of its duration
                self.animation_started = False

    def draw(self, surface):
        if self.animation_started:
            self.rpm_gauge.draw(surface)
