import pygame      ##.venv\Scripts\pip install pygame   <----Use this in terminal to resolve unreferenced problem
from Settings import GameSettings
from ShipClass import Ship
from AlienClass import Alien
from GameStatsClass import GameStats
from pygame.sprite import Group
from ButtonClass import Button
from ScoreboardClass import Scoreboard
import GameFunctions 
def RunGame():
    #Initialise game and create a screen object
    pygame.init()
    GameSetting=GameSettings()
    ScreenSize=(GameSetting.ScreenWidth,GameSetting.ScreenHeight)
    Screen=pygame.display.set_mode(ScreenSize)
    pygame.display.set_caption("Alien Invasion")
    PlayButton=Button(GameSetting,Screen,"Play")
    Stats=GameStats(GameSetting)
    ship=Ship(Screen,GameSetting)
    Bullets=Group()
    Aliens=Group()
    SB=Scoreboard(GameSetting,Screen,Stats)
    # Look for your original image loading setup:
    BackgroundRaw = pygame.image.load("Stars.jpg")
    BackgroundImage = pygame.transform.scale(BackgroundRaw, ScreenSize).convert_alpha()
    
    # ------------------ REPLACE STEP 1 WITH THIS CODE ------------------
    # This clones the star pattern from the bottom and fades it into the top
    BridgeHeight = 90  # Height of the star-merging zone
    
    # 1. Capture a clean slice of the bright blue nebula from the bottom edge
    BottomSlice = pygame.Surface((GameSetting.ScreenWidth, BridgeHeight), pygame.SRCALPHA)
    BottomSlice.blit(BackgroundImage, (0, 0), (0, GameSetting.ScreenHeight - BridgeHeight, GameSetting.ScreenWidth, BridgeHeight))
    
    # 2. Smoothly melt that bright star slice directly onto the dark top edge
    for RowY in range(BridgeHeight):
        # Calculate a soft exponential falloff factor
        Progress = RowY / BridgeHeight
        AlphaValue = int(255 * ((1.0 - Progress) ** 1.3))
        
        # Overwrite the transparency of just this specific horizontal line row
        LineMask = pygame.Surface((GameSetting.ScreenWidth, 1), pygame.SRCALPHA)
        LineMask.blit(BottomSlice, (0, 0), (0, RowY, GameSetting.ScreenWidth, 1))
        
        # Fill a temporary pixel blender to match the blending alpha curve
        BlendAlpha = pygame.Surface((GameSetting.ScreenWidth, 1), pygame.SRCALPHA)
        BlendAlpha.fill((255, 255, 255, AlphaValue))
        LineMask.blit(BlendAlpha, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        
        # Stamp it onto the top edge of the master background container
        BackgroundImage.blit(LineMask, (0, RowY))
        
    BackgroundY = 0  # Your standard scroll tracker
    # --------------------------------------------------------------------
    AlienObject=Alien(GameSetting,Screen)
    GameFunctions.CreateFleet(GameSetting,Screen,Aliens)
    #Start the main loop for the game
    while True:
        GameFunctions.CheckEvents(GameSetting, Screen, Stats, PlayButton, ship, Bullets, Aliens,SB)
        if Stats.GameActive:
            ship.Update()
            Bullets.update()
            for Bullet in Bullets.copy():
                if Bullet.rect.bottom<=0:
                    Bullets.remove(Bullet)
            Collisions=pygame.sprite.groupcollide(Bullets,Aliens,True,True)
            if Collisions:
                for aliens in Collisions.values():
                    Stats.Score+=GameSetting.AlienPoints*len(aliens)
                    SB.PrepScore()
                GameFunctions.CheckHighScore(Stats,SB)
            if len(Aliens)==0:
                GameSetting.IncreaseSpeed()
                Stats.Level+=1
                SB.PrepLevel()
                GameFunctions.CreateFleet(GameSetting,Screen,Aliens)
        # Advance the position down the screen
        BackgroundY += 0.5  
        if BackgroundY >= GameSetting.ScreenHeight:
            BackgroundY = 0
        
        # Render both segments right-side up smoothly
        Screen.blit(BackgroundImage, (0, BackgroundY))
        Screen.blit(BackgroundImage, (0, BackgroundY - GameSetting.ScreenHeight))
        SB.ShowScore()
        if Stats.GameActive:
            for Bullet in Bullets.sprites():
                Bullet.DrawBullet()
            for UFO in Aliens.sprites():
                UFO.blitme()
            ship.blitme()
        else:
            PlayButton.DrawButton()
        GameFunctions.UpdateAliens(GameSetting, Stats, Screen, ship, Aliens, Bullets, PlayButton,SB)  
        #Make the most recently drawn screen visible.
        pygame.display.flip()      ##it refreshes the picture on the screen. It is exactly like how a video works: it shows a fast sequence of static pictures (frames) to create the illusion of smooth movement.

RunGame()




