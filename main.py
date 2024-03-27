# main.py

import pygame
from modules.dashboard_handling import Dashboard

# Set the debug flag
DEBUG_MODE = True

dashboard = Dashboard(debug_mode=DEBUG_MODE)
dashboard.run()
