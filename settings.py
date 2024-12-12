class Settings:
    """ A class to store all settings for the Game """

    def __init__(self):
        """Initialize game's settings """

        # Screen Settings
        self.screen_width = 600
        self.screen_height = 800
        self.bg_color = (103, 181, 246)

        # Ship Settings
        self.ship_speed = 5.5

        # Bullet Settings
        self.bullet_speed = 7.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3



        