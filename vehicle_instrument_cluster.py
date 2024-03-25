import pygame

class SevenSegmentDisplay:
    def __init__(self, position=(0,0), size=1):
        self.position = position
        self.size = size
        # Load the images for each segment
        self.segments_images = {
            'A': pygame.image.load('seg-a.png'),
            'B': pygame.image.load('seg-b.png'),
            'C': pygame.image.load('seg-c.png'),
            'D': pygame.image.load('seg-d.png'),
            'E': pygame.image.load('seg-e.png'),
            'F': pygame.image.load('seg-f.png'),
            'G': pygame.image.load('seg-g.png')
        }       
        self.segment_offsets = {
            'A': (0, 0),
            'B': (0, 0),  # Example offset
            'C': (0, 0),  # Example offset
            'D': (0, 0),  # Example offset
            'E': (0, 0),  # Example offset
            'F': (0, 0),  # Example offset
            'G': (0, 0),   # Example offset
        }
        
        # Define which segments are on for each number
        self.numbers = {
            '0': ['A', 'B', 'C', 'D', 'E', 'F'],
            '1': ['B', 'C'],
            '2': ['A', 'B', 'G', 'E', 'D'],
            '3': ['A', 'B', 'C', 'D', 'G'],
            '4': ['B', 'C', 'F', 'G'],
            '5': ['A', 'C', 'D', 'F', 'G'],
            '6': ['A', 'C', 'D', 'E', 'F', 'G'],
            '7': ['A', 'B', 'C'],
            '8': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
            '9': ['A', 'B', 'C', 'D', 'F', 'G'],
            }
    
    def set_position(self, new_position):
        # Update the position of the display
        self.position = new_position

    def set_size(self, new_size):
        # Update the size of the display
        self.size = new_size

    set segment_offsets
    def draw(self, screen, number):
        segments_to_draw = self.numbers[str(number)]
        for segment in segments_to_draw:
            segment_image = self.segments_images[segment]
            offset = self.segment_offsets[segment]
            # Calculate the absolute position for each segment
            absolute_position = (self.position[0] + offset[0], self.position[1] + offset[1])
            screen.blit(segment_image, absolute_position)

class GaugeBar:
    def __init__(self, image_path, position):
        self.image = pygame.image.load(image_path)
        self.position = position
        self.active = False  # By default, bars are not active (not lit up)

    def draw(self, screen):
        if self.active:
            screen.blit(self.image, self.position)
            
class RPMGauge:
    def __init__(self, positions, image_path):
        self.bars = [GaugeBar(image_path, pos) for pos in positions]

    def set_rpm(self, rpm):
        # Assuming rpm is a value between 1 and 7
        # Activate the bars up to the rpm value and deactivate the rest
        for i, bar in enumerate(self.bars):
            bar.active = i < rpm

    def draw(self, screen):
        for bar in self.bars:
            bar.draw(screen)


if "__main__" == __name__:
    # Pygame setup
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    # Create a SevenSegmentDisplay object at position (100, 100)
    display = SevenSegmentDisplay(position=(100, 100))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Clear the screen with black
        display.draw(screen, 3)  # Draw the number '3'
        
        pygame.display.flip()

    pygame.quit()