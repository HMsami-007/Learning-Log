import pygame.font
from pygame.sprite import Group
from ShipClass import Ship
class Scoreboard():
    def __init__(self,GameSetting,Screen,GameStats):
        self.Screen=Screen
        self.ScreenRect=Screen.get_rect()
        self.GameSettings=GameSetting
        self.Stats=GameStats
        self.TextColour=(255, 255, 255)
        self.Font=pygame.font.Font(None,48)
        self.PrepScore()
        self.PrepHighScore()
        self.PrepLevel()
        self.PrepShips()

    def PrepScore(self):
        RoundedScore=int(round(self.Stats.Score,-1))
        ScoreStr="{:,}".format(RoundedScore)
        self.ScoreImage=self.Font.render(ScoreStr,True,self.TextColour)
        self.ScoreRect=self.ScoreImage.get_rect()
        self.ScoreRect.right=self.ScreenRect.right-20
        self.ScoreRect.top=20

    def ShowScore(self):
        self.Screen.blit(self.ScoreImage,self.ScoreRect)
        self.Screen.blit(self.HighScoreImage,self.HighScoreRect)
        self.Screen.blit(self.LevelImage,self.LevelRect)
        self.ships.draw(self.Screen)

    def PrepHighScore(self):
        HighScore=int(round(self.Stats.HighScore,-1))
        HighScoreStr="{:,}".format(HighScore)
        self.HighScoreImage=self.Font.render(HighScoreStr,True,self.TextColour)
        self.HighScoreRect=self.HighScoreImage.get_rect()
        self.HighScoreRect.centerx=self.ScreenRect.centerx
        self.HighScoreRect.top=self.ScoreRect.top

    def PrepLevel(self):
        self.LevelImage=self.Font.render(str(self.Stats.Level),True,self.TextColour)
        self.LevelRect=self.LevelImage.get_rect()
        self.LevelRect.right=self.ScoreRect.right
        self.LevelRect.top=self.ScoreRect.bottom+10

    def PrepShips(self):
        self.ships=Group()
        for ShipNo in range(self.Stats.ShipsLeft):
            ship=Ship(self.Screen,self.GameSettings)
            ship.image = pygame.transform.smoothscale(ship.Image, (45, 45))
            ship.rect = ship.image.get_rect()
            ship.rect.x = 10 + ShipNo * 55
            ship.rect.y = 10
            ship.Rect = ship.rect
            self.ships.add(ship)

            
                    
                             
        