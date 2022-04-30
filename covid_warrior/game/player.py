import arcade
import os
from game import constants

class Player():
    """
    This class is what the player controls in the game. It can move sideways
    on the screen and shoot projectiles.
    """

    def __init__(self):
        self.player_sprite_list = None
        # Set up the player info
        self.player_sprite = None
        self.player_sprite_list = arcade.SpriteList()
        # Set up the player
        self.player_sprite = arcade.Sprite(os.path.join(constants.PATH, "./sprites/shooter.png"), constants.SPRITE_SCALING_PLAYER)
        self.radius = 30

        # self.player_sprite = arcade.Sprite("./sprites/mustache-logo.png")
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 50
        self.player_sprite_list.append(self.player_sprite)


    
    def move_left(self):
        if self.player_sprite.center_x > 0:
            self.player_sprite.center_x -= constants.PLAYER_VELOCITY
        
        
    def move_right(self):
        if self.player_sprite.center_x < constants.SCREEN_WIDTH:
            self.player_sprite.center_x += constants.PLAYER_VELOCITY
        
    def draw(self):
        self.player_sprite_list.draw()