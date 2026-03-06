import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """  Class to Manage Game Assets and behavior """

    def __init__(self):
        """ Initialize the game ,and create game resources """
        pygame.init()

        self.clock = pygame.time.Clock()

        self.settings = Settings()

        # self.screen = pygame.display.set_mode((1200, 800))

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # Set background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """ Start the main loop for the game. """
        while True:
    # Watch the keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            # self.screen.fill(self.bg_color)

            self.screen.fill(self.settings.bg_color)

            self.ship.blitme()

            # Make fbd most recently drawn screen visible.
            pygame.display.flip()

            self.clock.tick(90)

if __name__ == '__main__':
# Make a Game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

#275




    # def __init__(self):
    #     """ Initialize the game ,and create game resources """
    #     pygame.init()  #1
    #
    #     self.clock = pygame.time.Clock()
    #     self.settings = Settings
    #
    #     self.screen = pygame.display.set_mode(
    #         (self.settings.screen_width, self.settings.screen_height))
    #     pygame.display.set_caption('Alien Invasion')
    #
    #     self.ship = Ship(self)
    #
    #     # Set the background color.
    #     self.bg_colour = (230, 230, 230)
    #
    # def run_game(self):
    #     """ Start the main loop for the game"""
    #     while True:
    #         self._check_events()
    #
    #         # Watch for keyboard and mouse events.
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 sys.exit()
    #
    #         # Redraw the screen during each pass through the loop.
    #         self.screen.fill(self.bg_colour)
    #         self.ship.blitme()
    #
    #         # Make the most recently draw screen visible.
    #         pygame.display.flip()
    #         self.clock.tick(90)


