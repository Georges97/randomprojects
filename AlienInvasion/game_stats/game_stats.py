class GameStats:
    """Track statistics for Alien Invasion."""
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.setting = ai_game.setting
        self.reset_stats()
    def reset_stats(self):
        """Initialize statistics that can change during"""
        self.ships_left = self.setting.ship_limit


