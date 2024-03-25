# segment_display.py
from modules.stuff import ImageSprite

SEGMENT_IMAGES = {
    'A': 'path/to/seg_a.png', # Top
    'B': 'path/to/seg_b.png', # Top-right
    'C': 'path/to/seg_c.png', # Bottom-right   
    'D': 'path/to/seg_d.png', # Bottom
    'E': 'path/to/seg_e.png', # Bottom-left
    'F': 'path/to/seg_f.png', # Top-left
    'G': 'path/to/seg_g.png'  # Center
}

class SevenSegmentDisplay:
    # ... (include the full SevenSegmentDisplay class as previously defined)

    def set_time(self, hour, minute):
        # Format the hour and minute to always have two digits
        hour_str = f"{hour:02d}"
        minute_str = f"{minute:02d}"

        # Set the time on the individual digits
        self.set_digit(0, hour_str[0])  # First digit of the hour
        self.set_digit(1, hour_str[1])  # Second digit of the hour
        self.set_digit(2, minute_str[0])  # First digit of the minute
        self.set_digit(3, minute_str[1])  # Second digit of the minute

    def set_digit(self, digit_position, number):
        # Activate the segments for the specified digit
        segments_to_activate = self.numbers[number]
        for segment in self.segments:
            if segment in segments_to_activate:
                self.segments[segment].activate()
            else:
                self.segments[segment].deactivate()

    def draw(self, screen):
        # Draw each digit
        for i in range(4):
            self.draw_digit(screen, i)

        # Optionally, draw the colon if you have a separate image for it
        # self.draw_colon(screen)

    def draw_digit(self, screen, digit_position):
        # Draw the active segments for the digit
        for segment_id, sprite in self.segments.items():
            if sprite.active:
                # Calculate the absolute position for each segment
                absolute_position = (self.position[0] + sprite.position[0], 
                                     self.position[1] + sprite.position[1])
                sprite.draw(screen)



class SevenSegmentClock:
    CLOCK_SEGMENT_IMAGES = {
        'A': 'path/to/seg_a.png',           # Top
        'B': 'path/to/seg_b.png',           # Top-right
        'C': 'path/to/seg_c.png',           # Bottom-right   
        'D': 'path/to/seg_d.png',           # Bottom
        'E': 'path/to/seg_e.png',           # Bottom-left
        'F': 'path/to/seg_f.png',           # Top-left
        'G': 'path/to/seg_g.png',           # Center
        'COLON': 'path/to/seg_colon.png'    # Colon between second and third digit
    }

    def __init__(self, position=(0, 0), segment_paths=None):
        if segment_paths is None:
            segment_paths = self.CLOCK_SEGMENT_IMAGES  # Use the class variable if no custom paths are provided

        self.position = position
        self.digit_displays = [SevenSegmentDisplay({k: v for k, v in segment_paths.items() if k != 'COLON'}, self.calculate_digit_position(i)) for i in range(4)]
        self.colon_image = ImageSprite(segment_paths['COLON'], self.calculate_colon_position())

    def calculate_digit_position(self, digit_index):
        # Your existing implementation
        ...

    def calculate_colon_position(self):
        # Your existing implementation or static position
        return (self.position[0] + some_x_offset, self.position[1] + some_y_offset)

    def set_time(self, hour, minute):
        # Your existing implementation
        ...

    def draw(self, screen):
        # Draw each digit
        for digit_display in self.digit_displays:
            digit_display.draw(screen)
        
        # Draw the colon
        self.colon_image.draw(screen)
