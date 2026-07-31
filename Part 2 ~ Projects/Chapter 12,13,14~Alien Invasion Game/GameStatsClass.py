class GameStats():
    def __init__(self,GameSettings):
        self.GameSettings=GameSettings
        self.ResetStats()
        self.GameActive=False
        self.HighScore=0
 
    def ResetStats(self):
        self.ShipsLeft=self.GameSettings.ShipLimit
        self.Score=0
        self.Level=1