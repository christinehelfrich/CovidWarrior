import arcade
from game import constants
import os
from game.gameView import GameView


class MenuView(arcade.View):
    """
    This class is a child of the view class. It displays when the game is started
    and shows how to play the game.
    """

    def __init__(self):
        super().__init__()
        # self.background = None
        self.background = arcade.load_texture(os.path.join(constants.PATH, "./sprites/main-background.jpeg"))

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT,self.background)
        arcade.draw_text("COVID Warrior", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2 + 50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance.", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

        arcade.draw_text("How to Play",constants.SCREEN_WIDTH/2,constants.SCREEN_HEIGHT/2-60,
                         arcade.color.BLACK, font_size=20, anchor_x="center")

        howToPlayText1 = "Move your warrior left and right with the arrow keys."
        howToPlayText2 = "Use A and D to shoot projectiles. A for Masks and D for hand sanitizer."
        howToPlayText3 = "Shoot the Karens with masks and kill the virus with sanitizer before"
        howToPlayText4 = "they reach the bottom of the bottom of the screen."
        howToPlayText5 = "Press Esc. to pause."

        arcade.draw_text(howToPlayText1,constants.SCREEN_WIDTH/2,constants.SCREEN_HEIGHT/2-90,
                         arcade.color.BLACK, font_size=16, anchor_x="center")
        arcade.draw_text(howToPlayText2,constants.SCREEN_WIDTH/2,constants.SCREEN_HEIGHT/2-120,
                         arcade.color.BLACK, font_size=16, anchor_x="center")
        arcade.draw_text(howToPlayText3,constants.SCREEN_WIDTH/2,constants.SCREEN_HEIGHT/2-150,
                         arcade.color.BLACK, font_size=16, anchor_x="center")
        arcade.draw_text(howToPlayText4,constants.SCREEN_WIDTH/2,constants.SCREEN_HEIGHT/2-180,
                         arcade.color.BLACK, font_size=16, anchor_x="center")
        arcade.draw_text(howToPlayText5,constants.SCREEN_WIDTH/2,constants.SCREEN_HEIGHT/2-210,
                         arcade.color.BLACK, font_size=16, anchor_x="center")


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game = GameView()
        game.setup()
        self.window.show_view(game)