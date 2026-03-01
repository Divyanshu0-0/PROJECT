import sys
import pygame

class AlienInvasion:
    """  Class to Manage Game Assets """
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 680))
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        """ Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently draw screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a Game instance and run the game.
    ai = alien = AlienInvasion()
    ai.run_game()

def __init__(self):
    """ Initialize the game ,and create game resources"""
    pygame.init()
    self.clock = pygame.time.Clock()

def run_game(self):
    """Start the main loop for the game."""
    while True:

        pygame.display.flip()
        pygame.clock.tick(90)
def __init__(self):

    pygame.display.set_caption("Alien Invasion")

    # Set the background color.
    self.bg_colour = (230, 230, 230)

def run_game(self):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.bg_color)

        # Make the most recently draw screen visible.
        pygame.display.flip()
        self.clock.tick(90)

# -------------------------------------------------------------

import pygame
from settings import Settings

class AlienInvasion:
    """ Overall class to manage game assets and behavior."""

def __init__(self):
    """ Initialize class to manage game resources. """
    pygame.init()
    self.clock = pygame.time.Clock()
    self.settings = Settings()

    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    def run_game(self):
            # Redraw the screen