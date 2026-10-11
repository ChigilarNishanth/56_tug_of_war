import pygame

class Rope:
    def __init__(self, screen_width: int, win_threshold: int = 220):
        self.screen_width = screen_width
        self.center_x = screen_width // 2
        self.position = self.center_x
        self.win_threshold = win_threshold
        self.pull_step = 15

    def pull_left(self):
        """Move rope marker left for Player 1."""
        self.position -= self.pull_step

    def pull_right(self):
        """Move rope marker right for Player 2."""
        self.position += self.pull_step

    def reset(self):
        """Reset rope position back to the exact center."""
        self.position = self.center_x

    def clamp(self):
        """Keep the rope position within visible screen bounds."""
        self.position = max(100, min(self.screen_width - 100, self.position))

    def check_winner(self):
        """Evaluate if rope crossed winning boundaries."""
        if self.position <= (self.center_x - self.win_threshold):
            return "Player 1 (Left)"
        elif self.position >= (self.center_x + self.win_threshold):
            return "Player 2 (Right)"
        return None