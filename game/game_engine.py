import pygame
import sys
from game.player import Player
from game.rope import Rope

class GameEngine:
    def __init__(self):
        pygame.init()
        self.width, self.height = 900, 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Tug of War - Vibe Coded Edition")
        
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.game_duration = 30  # Timer duration in seconds
        
        # Color Palette
        self.WHITE = (255, 255, 255)
        self.BLACK = (20, 20, 20)
        self.RED = (220, 53, 69)
        self.BLUE = (13, 110, 253)
        self.GREEN = (40, 167, 69)
        self.GRAY = (200, 200, 200)

        # Game Entities
        self.p1 = Player("Player 1", pygame.K_a, self.RED, "left")
        self.p2 = Player("Player 2", pygame.K_l, self.BLUE, "right")
        self.rope = Rope(self.width)
        
        self.start_ticks = pygame.time.get_ticks()
        self.winner = None

        # Fonts
        self.font = pygame.font.SysFont("Arial", 26, bold=True)
        self.large_font = pygame.font.SysFont("Arial", 42, bold=True)

    def reset(self):
        """Reset match variables for game replay."""
        self.rope.reset()
        self.start_ticks = pygame.time.get_ticks()
        self.winner = None

    def run(self):
        """Main event loop."""
        running = True
        while running:
            self.clock.tick(self.fps)

            # Countdown Timer Evaluation
            if self.winner is None:
                seconds_passed = (pygame.time.get_ticks() - self.start_ticks) // 1000
                time_left = max(0, self.game_duration - seconds_passed)

                # Time ran out: evaluate who is closest to their side
                if time_left == 0:
                    if self.rope.position < self.width // 2:
                        self.winner = "Player 1 (Left)"
                    elif self.rope.position > self.width // 2:
                        self.winner = "Player 2 (Right)"
                    else:
                        self.winner = "Tie Game!"
            else:
                time_left = 0

            # Input Event Handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if self.winner is None:
                        if self.p1.is_pulling(event):
                            self.rope.pull_left()
                        elif self.p2.is_pulling(event):
                            self.rope.pull_right()

                        self.winner = self.rope.check_winner()

                    # Press 'R' to restart game
                    if event.key == pygame.K_r:
                        self.reset()

            self.rope.clamp()
            self.draw(time_left)

        pygame.quit()
        sys.exit()

    def draw(self, time_left: int):
        """Render all frame elements."""
        self.screen.fill(self.WHITE)

        # Center Line & Winning Threshold Boundaries
        pygame.draw.line(self.screen, self.GRAY, (self.width // 2, 80), (self.width // 2, 380), 3)
        pygame.draw.line(self.screen, self.RED, (self.width // 2 - self.rope.win_threshold, 160), 
                         (self.width // 2 - self.rope.win_threshold, 340), 4)
        pygame.draw.line(self.screen, self.BLUE, (self.width // 2 + self.rope.win_threshold, 160), 
                         (self.width // 2 + self.rope.win_threshold, 340), 4)

        # Rope Line & Center Knot Circle
        pygame.draw.line(self.screen, self.BLACK, (80, 250), (self.width - 80, 250), 8)
        pygame.draw.circle(self.screen, self.GREEN, (self.rope.position, 250), 16)

        # HUD Display Elements
        p1_txt = self.font.render("Player 1: Press 'A'", True, self.RED)
        p2_txt = self.font.render("Player 2: Press 'L'", True, self.BLUE)
        timer_txt = self.font.render(f"Time Remaining: {time_left}s", True, self.BLACK)

        self.screen.blit(p1_txt, (40, 30))
        self.screen.blit(p2_txt, (self.width - 240, 30))
        self.screen.blit(timer_txt, (self.width // 2 - 110, 30))

        # Game Over / Winner Banner
        if self.winner:
            res_txt = self.large_font.render(f"{self.winner} Wins!", True, self.GREEN if "Tie" not in self.winner else self.BLACK)
            rst_txt = self.font.render("Press 'R' to Restart", True, self.BLACK)
            self.screen.blit(res_txt, (self.width // 2 - res_txt.get_width() // 2, 370))
            self.screen.blit(rst_txt, (self.width // 2 - rst_txt.get_width() // 2, 430))

        pygame.display.flip()