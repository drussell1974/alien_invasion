class GameStats():
    """ Track statistics for Alien Invasion """
    def __init__(self, ai_settings):
        """ Initialize statistics """
        self.ai_settings = ai_settings
        self.reset_stats()
        # start alien invasion in active status
        self.game_active = True
        # High score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """ Initialise statistics that can change during the game """
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
