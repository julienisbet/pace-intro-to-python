import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion():
    """Class to manage game state"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.bg_color = self.settings.bg_color
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.ship.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()