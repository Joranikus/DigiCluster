import pygame

#   Screen Size
WIDTH, HEIGHT = 800, 480  # use your screens display information
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
FPS = 60

# Title and Icon
ICON = "images/speedometer.png"
BG = "images/background.png"
program_icon = pygame.image.load(ICON)
project_name = "Digifiz Dashboard - "
digifiz_ver = "v.0.5"

#   Colours
NEON_YELLOW = (236, 253, 147)   #   Speedo Colour
NEON_GREEN = (145, 213, 89)     #   Lower gauge colours, clock, odo etc
DARK_GREY = (9, 52, 50)         #   background of the digits (for the 7segment appearance)

#   Font Details
FONT_PATH = "fonts/DSEG7Classic-Bold.ttf"
FONT_LARGE = 174    #   Speedo size
FONT_MEDIUM = 94    #   Clock, MFA, Fuel size
FONT_SMALL = 67     #   Odo Size

#   Locations for gauge graphics, each has the same start XY but builds upon it, check images folder
RPM_XY = (135, 5)
COOLANT_XY = (1481, 105)
EGT_XY = (1599, 105)
OILPRESSURE_XY = (1711, 105)
BOOST_XY = (1822, 105)
CLOCK_XY = (555, 620)
FUEL_XY = (1560, 620)
ODO_XY = (60, 644)
ODO_L_XY = (395, 678)
MFA_XY = (1435, 668)
MFABG_XY = (1021, 563)
SPEEDO_XY = (1247, 305)

'''                         LOAD IMAGES                         '''
BACKGROUND = pygame.image.load(BG).convert_alpha()
MFA = pygame.image.load("images/indicators/MFA_temp.png").convert_alpha()
fuelres_on = pygame.image.load("images/indicators/fuelResOn.png").convert_alpha()
fuelres_off = pygame.image.load("images/indicators/fuelResOff.png").convert_alpha()