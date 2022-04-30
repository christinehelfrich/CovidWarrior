import arcade
from game import constants
import os

class PauseView(arcade.View):
    """
    This class is a child of the view class. It is displayed when the player
    pushes Esc. while in the game view. It pauses the game and lets the user
    quit the game if they want to.
    """

    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        self.background = arcade.load_texture(os.path.join(constants.PATH, "./sprites/pause-background.jpeg"))

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT,self.background)

        arcade.draw_text("GAME PAUSED", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2+50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

        # Show tip to return or reset
        arcade.draw_text("Press Esc. to resume",
                        constants.SCREEN_WIDTH/2,
                        constants.SCREEN_HEIGHT/2,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Press Enter to return to Main Menu",
                        constants.SCREEN_WIDTH/2,
                        constants.SCREEN_HEIGHT/2-30,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:   # resume game
            self.window.show_view(self.game_view)
        elif key == arcade.key.ENTER:  # reset game
            from game.menuView import MenuView
            game = MenuView()
            self.window.show_view(game)