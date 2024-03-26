# main.py

import pygame
from object_handling.dashboard_handling import Dashboard

# Set the debug flag
DEBUG_MODE = True

pygame.init()
if DEBUG_MODE:
    screen_width, screen_height = 800, 480
    screen = pygame.display.set_mode((screen_width, screen_height))  # Windowed mode
else:
    screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)  # Fullscreen mode

# Initialize obj ects
dashboard = Dashboard()
dashboard.run()

# Cap the frame rate
pygame.time.Clock().tick(120)

pygame.quit()
