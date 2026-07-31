import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,Screen,Settings):
        """Initialise the ship and its starting position"""
        super(Ship,self).__init__()
        self.Screen=Screen
        self.Settings=Settings

        #Load the ship's image and get its rect()
        self.ImageFile="Space Shuttle.png"
        self.OriginalImage=pygame.image.load(self.ImageFile).convert_alpha()
        self.Image=pygame.transform.scale(self.OriginalImage, (175,175))
        self.Rect=self.Image.get_rect() #In Pygame, self.rect is a standard object attribute used within custom classes (such as Pygame Sprites) to store and track the exact position, size, and boundary coordinates of a game object
        self.image = self.Image  
        self.rect = self.Rect   
        self.ScreenRect=Screen.get_rect()
        self.MovingRight=False
        self.MovingLeft=False
        self.MovingUp=False
        self.MovingDown=False

        #Start each new ship at the bottom center of the screen
        self.Rect.centerx=self.ScreenRect.centerx
        self.Rect.bottom=self.ScreenRect.bottom
        self.CentreX=float(self.Rect.centerx)
        self.CentreY=float(self.Rect.centery)
        

    def Update(self):
        if self.MovingRight and self.Rect.right<self.ScreenRect.right:
            self.CentreX+=self.Settings.ShipSpeedFactor
        if self.MovingLeft and self.Rect.left>0:
            self.CentreX-=self.Settings.ShipSpeedFactor
        if self.MovingUp and self.Rect.top>0:
            self.CentreY-=self.Settings.ShipSpeedFactor
        if self.MovingDown and self.Rect.bottom<self.ScreenRect.bottom:
            self.CentreY+=self.Settings.ShipSpeedFactor
        self.Rect.centerx=int(self.CentreX)
        self.Rect.bottom=int(self.CentreY)



    def blitme(self):
        """Draw the ship at its current location."""
        self.Screen.blit(self.Image,self.Rect)

    def CenterShip(self):
        """Reset the ship position cleanly to the bottom center of the screen."""
        self.Rect.centerx = self.ScreenRect.centerx
        self.Rect.bottom = self.ScreenRect.bottom
        
        # CRITICAL FIX: Update the tracking decimals so the ship stays centered!
        self.CentreX = float(self.Rect.centerx)
        self.CentreY = float(self.Rect.centery)
    