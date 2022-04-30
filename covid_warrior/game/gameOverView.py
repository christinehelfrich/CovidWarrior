import arcade
from game import constants
import os
from game.gameView import GameView
from game.menuView import MenuView
from game.highScore import HighScore


class GameOverView(arcade.View):
    """
    This class is a child of the view class. It appears when the player
    loses the game and let the player return to the main menu or play
    again.
    """

    def __init__(self,game_view):
        super().__init__()
        self.game_view = game_view
        self.background = arcade.load_texture(os.path.join(constants.PATH, "./sprites/gameOver-background.jpeg"))
        self.highScore = HighScore()


    def on_show(self):
        arcade.set_background_color(arcade.color.RED)
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT,self.background)


        # draw text 
        arcade.draw_text("GAME OVER", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2+90,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        
        # draw text
        arcade.draw_text("Score: " + str(self.game_view.score), constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2+60,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        
        # draw text
        arcade.draw_text("High Score: " + self.highScore.highScoreRead, constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2+20,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        
        # Show tip to return or reset
        arcade.draw_text("Press Enter to play again",
                        constants.SCREEN_WIDTH/2,
                        constants.SCREEN_HEIGHT/2,
                        arcade.color.BLACK,
                        font_size=20,
                        anchor_x="center")
                        
        arcade.draw_text("Press Esc. to return to Main Menu",
                        constants.SCREEN_WIDTH/2,
                        constants.SCREEN_HEIGHT/2-30,
                        arcade.color.BLACK,
                        font_size=20,
                        anchor_x="center")
    
    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:   # resume game
            game = MenuView()
            self.window.show_view(game)
        elif key == arcade.key.ENTER:  # reset game
            game = GameView()
            self.window.show_view(game)