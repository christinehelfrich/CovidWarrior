import os
import arcade
from game import constants
import random

class Enemy(arcade.Sprite):
    """
    This class represents the enemies on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the enemy to a random spot above the screen
        self.center_y = random.randrange(constants.SCREEN_HEIGHT + 20,
                                         constants.SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(constants.SCREEN_WIDTH)

    def update(self):

        # Move the enemy
        self.center_y -= constants.ENEMY_VELOCITY

        # See if the enemy has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            # self.reset_pos()
            self.remove_from_sprite_lists()
            