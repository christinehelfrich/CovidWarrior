from game import constants
import os


class HighScore():
    """
    This class initializes the high score. Gets the value from text file.
    """
    def __init__(self): 
        self.scoreFile = open(os.path.join(constants.PATH, "./highScore/highScore.txt"), "r")
        self.highScoreRead = self.scoreFile.read()
        self.scoreFile.close()
        
    def newHighScore(self, score):
        """
        Changes the high score if reached
        """
        self.highScore = str(score)
        self.scoreFile = open(os.path.join(constants.PATH, "./highScore/highScore.txt"), "w")
        #self.scoreFile = open("highScore/highScore.txt", "w")
        self.scoreFile.write(self.highScore)
        self.scoreFile.close()