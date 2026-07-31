class GameSettings():
    """A class to store all settings for alien invasion game"""
    def __init__(self):
        """Initialise the game's settings"""
        #Screen settings
        self.ScreenWidth=1200
        self.ScreenHeight=800
        self.ScreenSize=(self.ScreenWidth,self.ScreenHeight)
        self.ShipSpeedFactor=2
        #BulletSettings
        self.BulletSpeedFactor=5
        self.BulletWidth=3
        self.BulletHeight=15
        self.BulletColour=0,191,255
        self.BulletsAllowed=5
        self.AlienSpeedFactor = 0.1
        self.FleetDropSpeed = 5   
        self.FleetDirection = 1     
        self.ShipLimit=3 
        self.SpeedUpScale=1.1
        self.ScoreScale=1.5
        self.InitializeDynamicSettings()

    def InitializeDynamicSettings(self):
        self.ShipSpeedFactor=1.5
        self.BulletSpeedFactor=3
        self.AlienSpeedFactor=1
        self.FleetDirection=1
        self.AlienPoints=50

    def IncreaseSpeed(self):
        self.ShipSpeedFactor*=self.SpeedUpScale
        self.BulletSpeedFactor*=self.SpeedUpScale
        self.AlienSpeedFactor*=self.SpeedUpScale
        self.AlienPoints=int(self.AlienPoints*self.ScoreScale)