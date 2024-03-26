# main.py

import pygame
from modules.dashboard_handling import Dashboard

# Set the debug flag
DEBUG_MODE = True

pygame.init()
if DEBUG_MODE:
    screen_width, screen_height = 800, 480
    screen = pygame.display.set_mode((screen_width, screen_height))  # Windowed mode
else:
    screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)  # Fullscreen mode

dashboard = Dashboard()
dashboard.run()

pygame.time.Clock().tick(60)
pygame.quit()
