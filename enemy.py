import pygame

class Enemy:
    """ Class to create the Enemy """

    def __init__(self, ai_game):
        """Initialize the enemy ship and set it's starting position """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()



    
    def blitme(self):
        """ Draw the enemy ship at its current location """
        self.screen.blit(self.image, self.rect)