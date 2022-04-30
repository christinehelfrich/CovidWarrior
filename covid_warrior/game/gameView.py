import os
import random
import arcade
from game import constants
from game.player import Player
from game.enemy import Enemy


class GameView(arcade.View):
    """
    This class is a child of the view class. It contains the main game loop and
    lets the player play the game. It handles all of the sprites and the sounds 
    of the game and anything else that is needed to defeat the coronavirus.
    """

    def __init__(self):
        super().__init__()

        arcade.set_background_color(arcade.color.AMAZON)

        # Variables that will hold sprite lists
        self.player = Player()
        self.karen_sprite_list = None
        self.mask_sprite_list = None
        self.sanitizer_sprite_list = None
        self.virus_sprite_list = None
        self.holding_left = False
        self.holding_right = False
        self.gameOver = False

        # Load sounds
        self.shoot_mask = arcade.load_sound(":resources:sounds/laser3.wav")
        self.shoot_sanitizer = arcade.load_sound(":resources:sounds/laser5.wav")
        self.good_hit_mask = arcade.load_sound(":resources:sounds/rockHit2.wav")
        self.good_hit_sanitizer = arcade.load_sound(":resources:sounds/laser4.wav")
        self.bad_hit = arcade.load_sound(":resources:sounds/hit1.wav")

        # player's score
        self.score = 0

        self.setup()

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here

        # Sprite lists
        
        self.karen_sprite_list = arcade.SpriteList()
        self.mask_sprite_list = arcade.SpriteList()
        self.sanitizer_sprite_list = arcade.SpriteList()
        self.virus_sprite_list = arcade.SpriteList()

        # player's score
        self.score = 0

        # self.spawn_all_enemies()

        # All sprite list
        self.all_sprites = arcade.SpriteList()
        

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below
        self.karen_sprite_list.draw()
        self.virus_sprite_list.draw()
        self.player.draw()
        self.mask_sprite_list.draw()
        self.sanitizer_sprite_list.draw()

        # Draw our score on the screen
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 5, 570,
                         arcade.csscolor.WHITE, 18)

        # Draw the level on the screen
        # level_text = f"Level: {constants.LEVEL}"
        # arcade.draw_text(level_text, 700, 570,
        #                  arcade.csscolor.WHITE, 18)
        
        # Game background color
        arcade.set_background_color(arcade.color.AMAZON)


    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        if self.holding_left == True:
            self.player.move_left()
        if self.holding_right == True:
            self.player.move_right()
        self.player.draw()
        self.karen_sprite_list.update()
        self.virus_sprite_list.update()
        self.mask_sprite_list.update()
        self.sanitizer_sprite_list.update()
        
        # Loop through each colliding sprite, remove it, and add to the score.
        self.check_projectile_collisions()
        self.spawn_enemies(delta_time)
        self.checkEnemyPosition()
        self.check_player_collision()
        if self.gameOver:
            # pass self, the current view, to preserve this view's state
            from game.highScore import HighScore
            highScore = HighScore()
            # set new high score
            if self.score > int(highScore.highScoreRead):
                highScore.newHighScore(self.score)
            from game.gameOverView import GameOverView
            gameOver = GameOverView(self)
            self.window.show_view(gameOver)

    def spawn_enemies(self, delta_time):

        for i in range(constants.ENEMY_COUNT):
            # Have a random 1 in 200 change of shooting each 1/60th of a second
            odds = 600

            # Adjust odds based on delta-time
            adj_odds = int(odds * (1 / 60) / delta_time)


            if random.randrange(adj_odds) == 0:
                randoNum = random.randint(1, 100)

                if randoNum % 3 == 0:
                    # Set up virus
                    virus = Enemy(os.path.join(constants.PATH, "./sprites/virus.png"), constants.SPRITE_SCALING_ENEMY)

                    # Set its position to a random position at the top of the screen
                    virus.left = random.randint(60, constants.SCREEN_WIDTH - 75)
                    virus.top = constants.SCREEN_HEIGHT
                    virus.radius = 30
                    self.virus_sprite_list.append(virus)
                    
                else: 
                    # Set up karen
                    karen = Enemy(os.path.join(constants.PATH, "./sprites/karen.png"), constants.SPRITE_SCALING_ENEMY)
                    # Set its position to a random position at the top of the screen
                    karen.left = random.randint(60, constants.SCREEN_WIDTH - 75)
                    karen.top = constants.SCREEN_HEIGHT
                    karen.radius = 60
                    self.karen_sprite_list.append(karen)


    def check_projectile_collisions(self):
        # Loop through each colliding sprite, remove it, and add to the score.
        for enemy in self.karen_sprite_list: 
            for projectile in self.mask_sprite_list:
                if arcade.check_for_collision(enemy, projectile):
                    self.karen_sprite_list.remove(enemy)
                    self.mask_sprite_list.remove(projectile)
                    self.score += 50
                    arcade.play_sound(self.good_hit_mask)
            for projectile in self.sanitizer_sprite_list:
                if arcade.check_for_collision(enemy, projectile):
                    self.sanitizer_sprite_list.remove(projectile)
                    arcade.play_sound(self.bad_hit)
                
        for enemy in self.virus_sprite_list: 
            for projectile in self.sanitizer_sprite_list:
                if arcade.check_for_collision(enemy, projectile):
                    self.virus_sprite_list.remove(enemy)
                    self.sanitizer_sprite_list.remove(projectile)
                    self.score += 100
                    arcade.play_sound(self.good_hit_sanitizer)
            for projectile in self.mask_sprite_list:
                if arcade.check_for_collision(enemy, projectile):
                    self.mask_sprite_list.remove(projectile)
                    arcade.play_sound(self.bad_hit)
    
    def check_player_collision(self):
        for enemy in self.karen_sprite_list:
            too_close = enemy.radius + self.player.radius
            if (abs(enemy.center_x - self.player.player_sprite.center_x) < too_close and
                abs(enemy.center_y - self.player.player_sprite.center_y) < too_close):
                self.gameOver = True
        for enemy in self.virus_sprite_list:
            too_close = enemy.radius + self.player.radius
            if (abs(enemy.center_x - self.player.player_sprite.center_x) < too_close and
                abs(enemy.center_y - self.player.player_sprite.center_y) < too_close):
                self.gameOver = True
    
    def checkEnemyPosition(self):
        for enemy in self.virus_sprite_list:
            if enemy.center_y < 0:
                self.gameOver = True
        for enemy in self.karen_sprite_list:
            if enemy.center_y < 0:
                self.gameOver = True
        

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        # self.projectile_sprite.center_y = self.projectile_sprite.center_y + 5
        if key == arcade.key.A:
            # Create a bullet
            self.projectile_sprite = arcade.Sprite(os.path.join(constants.PATH, "./sprites/facemask.png"), constants.SPRITE_SCALING_PROJECTILE)
            # Give the bullet a speed
            self.projectile_sprite.change_y = constants.BULLET_SPEED
            # Position the bullet
            self.projectile_sprite.center_x = self.player.player_sprite.center_x
            self.projectile_sprite.bottom = self.player.player_sprite.top
            # Add the bullet to the appropriate lists
            self.mask_sprite_list.append(self.projectile_sprite)
            #play bullet sound
            arcade.play_sound(self.shoot_mask)
            
        if key == arcade.key.D:
            # Create a bullet
            self.projectile2_sprite = arcade.Sprite(os.path.join(constants.PATH, "./sprites/sanitizer-drop.png"), constants.SPRITE_SCALING_PROJECTILE)
            # Give the bullet a speed
            self.projectile2_sprite.change_y = constants.BULLET_SPEED
            # Position the bullet
            self.projectile2_sprite.center_x = self.player.player_sprite.center_x
            self.projectile2_sprite.bottom = self.player.player_sprite.top
            # Add the bullet to the appropriate lists
            self.sanitizer_sprite_list.append(self.projectile2_sprite)
            #play bullet sound
            arcade.play_sound(self.shoot_sanitizer)
        
        if key == arcade.key.LEFT:
            self.holding_left = True

        if key == arcade.key.RIGHT:
            self.holding_right = True
        
        if key == arcade.key.ESCAPE:
            # pass self, the current view, to preserve this view's state
            from game.pauseView import PauseView
            pause = PauseView(self)
            self.window.show_view(pause)

        
    def on_key_release(self, key, key_modifiers):
        """
        Called when a key is released. Sets the state of
        the arrow key as being not held anymore.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT:
            self.holding_left = False

        if key == arcade.key.RIGHT:
            self.holding_right = False