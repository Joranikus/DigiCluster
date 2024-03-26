import pygame
from modules.segment_display import SevenSegmentClock, BatteryVoltageDisplay
from modules.gauges import Gauge, RPMGauge, RpmGaugeAnimation
from modules.visual_elements import PlaceObject, LightsManager

class Dashboard():
    ANIMATION_DURATION=6

    def __init__(self, debug_mode):
        pygame.init()
        if debug_mode:
            screen_width, screen_height = 800, 480
            self.screen = pygame.display.set_mode((screen_width, screen_height), pygame.HWSURFACE | pygame.DOUBLEBUF)
        else:
            screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
            self.screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)  # Fullscreen mode

        self.init_objects()
        self.dynamic_data = {
            'oil_pressure': 3,
            'fuel_level': 50,
            'coolant_temp': 50,
            'turbo_pressure': 50,
            'rpm_value': 100,
            'battery_voltage': 12.0,
            'lights': {
                'coolant_warning': True,
                'high_beam': True,
                'low_beam': True,
                'oil_warning': True,
                'parking_lights': True,
                'turn_signal': True,
                'battery_warning': True
            }
        }

        # Start the RPM gauge animation
        # self.rpm_animation.start_animation()

    
    def init_objects(self):
        # Initialize background layers
        # Layer 1 Background
        self.BACKGROUND = PlaceObject('images/background.png')

        # Layer 2 Background Objects
        self.RPM_BACKGROUND = PlaceObject('images/rpm/rpm_background.png')
        self.MFA_BACKGROUND = PlaceObject('images/mfa/mfa_background.png')
        self.LIGHTS_BACKGROUND = PlaceObject('images/lights/lights_background.png')
        self.CLOCK_BACKGROUND = PlaceObject('images/clock/clock_background.png')
        self.BARS_BACKGROUND = PlaceObject('images/bars/bars_background.png')

        # Layer 3 Foreground Objects
        # Gauges
        self.oil_pressure_gauge = Gauge('images/bars/oil_pressure/oil_pressure_',
                                position=(0, 0), min_value=0, max_value=5,
                                single_image_mode=True
                                )
        self.fuel_gauge = Gauge('images/bars/fuel_level/fuel_level_',
                        position=(0, 0), min_value=0, max_value=100,
                        single_image_mode=True
                        )
        self.coolant_temp_gauge = Gauge('images/bars/coolant_temp/coolant_temp_',
                                position=(0, 0), min_value=40, max_value=120,
                                single_image_mode=True
                                )
        self.turbo_pressure_gauge = Gauge('images/bars/turbo/turbo_pressure_',
                                    position=(0, 0), min_value=0, max_value=100,
                                    single_image_mode=True
                                    )
        self.rpm_gauge = RPMGauge('images/rpm/',
                            position=(0, 0), min_value=0, max_value=7000,
                            max_bars=70
                            )
        # Initialize the RPM gauge animation
        self.rpm_animation = RpmGaugeAnimation(self.rpm_gauge, animation_duration=self.ANIMATION_DURATION)
        self.rpm_animation.start_animation()  # Start the animation

        # Clock
        self.seven_segment_clock = SevenSegmentClock()

        self.lights_manager = LightsManager()  # Adjust the position as needed
        self.battery_voltage_display = BatteryVoltageDisplay()

    def draw_objects(self):
        # Layer 1: Draw background
        self.BACKGROUND.draw(self.screen)

        # Layer 2: Draw components in "off" state
        self.RPM_BACKGROUND.draw(self.screen)
        self.MFA_BACKGROUND.draw(self.screen)
        self.LIGHTS_BACKGROUND.draw(self.screen)
        self.CLOCK_BACKGROUND.draw(self.screen)
        self.BARS_BACKGROUND.draw(self.screen)

        # Layer 3: Draw dynamic components

        self.oil_pressure_gauge.draw(self.screen)
        self.fuel_gauge.draw(self.screen)
        self.coolant_temp_gauge.draw(self.screen)
        self.turbo_pressure_gauge.draw(self.screen)
        self.rpm_animation.draw(self.screen)
        self.rpm_gauge.draw(self.screen)
        self.seven_segment_clock.draw(self.screen)
        self.lights_manager.draw(self.screen)
        self.battery_voltage_display.draw(self.screen)
    
    def update_objects(self):
        # Update gauges with values from dynamic_data
        self.oil_pressure_gauge.set_value(self.dynamic_data['oil_pressure'])
        self.fuel_gauge.set_value(self.dynamic_data['fuel_level'])
        self.coolant_temp_gauge.set_value(self.dynamic_data['coolant_temp'])
        self.turbo_pressure_gauge.set_value(self.dynamic_data['turbo_pressure'])
        self.rpm_gauge.set_value(self.dynamic_data['rpm_value'])
        self.battery_voltage_display.set_value(self.dynamic_data['battery_voltage'])

        # Update lights with values from dynamic_data
        for light, state in self.dynamic_data['lights'].items():
            self.lights_manager.set_value(light, state)

        # Update the RPM gauge animation
        self.rpm_animation.update()

        # Update the clock
        self.seven_segment_clock.set_time_now()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.update_objects()
            self.draw_objects()
            
            pygame.display.flip()

        pygame.quit()