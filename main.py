import pygame
# Assuming Background, SevenSegmentClock, RPMGauge, etc., are defined in the modules package

from modules.segment_display import SevenSegmentClock, BatteryVoltageDisplay
# from modules.rpm_gauge import RPMGauge
from modules.gauges import Gauge, RPMGauge
from modules.stuff import ImageSprite, PlaceObject, LightsManager
# Other imports as necessary

pygame.init()
screen = pygame.display.set_mode((800, 480))  # Adjust to your desired resolution

# Initialize the layers
#Layer 1 Background
BACKGROUND = PlaceObject('images/background.png')

#Layer 2 Background Objects
RPM_BACKGROUND = PlaceObject('images/rpm/rpm_background.png')  # Assuming you use the Background class for simplicity
MFA_BACKGROUND = PlaceObject('images/mfa/mfa_background.png')
LIGHTS_BACKGROUND = PlaceObject('images/lights/lights_background.png')
CLOCK_BACKGROUND = PlaceObject('images/clock/clock_background.png')
BARS_BACKGROUND = PlaceObject('images/bars/bars_background.png')

# Layer 3 Foreground Objects
# Gauges
oil_pressure_gauge = Gauge('images/bars/oil_pressure/oil_pressure_', 
                           position=(0,0), min_value=0, max_value=5, 
                           single_image_mode=True
                           )
fuel_gauge = Gauge('images/bars/fuel_level/fuel_level_', 
                           position=(0,0), min_value=0, max_value=100, 
                           single_image_mode=True
                           )
coolant_temp_gauge = Gauge('images/bars/coolant_temp/coolant_temp_', 
                           position=(0,0), min_value=40, max_value=120, 
                           single_image_mode=True
                           )
turbo_pressure_gauge = Gauge('images/bars/turbo/turbo_pressure_', 
                           position=(0,0), min_value=0, max_value=100, 
                           single_image_mode=True
                           )
rpm_gauge = RPMGauge('images/rpm/', 
                           position=(0,0), min_value=0, max_value=7000, 
                           max_bars=70
                           )

# Clock
seven_segment_clock = SevenSegmentClock()

lights_manager = LightsManager()  # Adjust the position as needed
battery_voltage_display = BatteryVoltageDisplay()



#seven_segment_clock = SevenSegmentClock(position=(x, y))  # Add necessary arguments
#rpm_gauge = RPMGauge(base_image_path='path/to/rpm/', positions=[(x1, y1), (x2, y2), ...])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Layer 1: Draw background
    BACKGROUND.draw(screen)

    # Layer 2: Draw components in "off" state
    RPM_BACKGROUND.draw(screen)
    MFA_BACKGROUND.draw(screen)
    LIGHTS_BACKGROUND.draw(screen)
    CLOCK_BACKGROUND.draw(screen)
    BARS_BACKGROUND.draw(screen)

    # Layer 3: Draw dynamic components
    oil_pressure_gauge.set_value(3) #TODO: is hardcoded value
    fuel_gauge.set_value(50) #TODO: is hardcoded value
    coolant_temp_gauge.set_value(50) #TODO: is hardcoded value
    turbo_pressure_gauge.set_value(50) #TODO: is hardcoded value
    rpm_gauge.set_value(6200) #TODO: is hardcoded value


    oil_pressure_gauge.draw(screen)
    fuel_gauge.draw(screen)
    coolant_temp_gauge.draw(screen)
    turbo_pressure_gauge.draw(screen)
    rpm_gauge.draw(screen)

    seven_segment_clock.set_time_now()
    seven_segment_clock.draw(screen)

    lights_manager.set_value('coolant_warning', True)
    lights_manager.set_value('high_beam', True)
    lights_manager.set_value('low_beam', True)
    lights_manager.set_value('oil_warning', True)
    lights_manager.set_value('parking_lights', True)
    lights_manager.set_value('turn_signal', True)


    lights_manager.set_value('battery_warning', True)
    lights_manager.draw(screen)

    battery_voltage_display.set_value(12.0)
    battery_voltage_display.draw(screen)

    # Update the RPM gauge similarly
    #rpm_gauge.set_rpm(7200)  # Set this based on your application's state
    #rpm_gauge.draw(screen)

    # Update the screen
    pygame.display.flip()

    # Cap the framerate
    pygame.time.Clock().tick(60)

pygame.quit()