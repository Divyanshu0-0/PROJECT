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
    alien = AlienInvasion()
    alien.run_game()
