import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    def __init__(self,Settings,Screen,Ship):
        """Create a bullet object at the ship's current position"""
        super(Bullet,self).__init__()
        self.Screen=Screen

        #Create a bullet rect at (0,0) and then set correct position.
        self.rect=pygame.Rect(0,0,Settings.BulletWidth,Settings.BulletHeight)
        # Change these two lines inside __init__:
        self.rect.centerx=Ship.Rect.centerx
        self.rect.top=Ship.Rect.top

        #Store the bullet's position as a decimal value
        self.y=float(self.rect.y)
        self.Colour=Settings.BulletColour
        self.SpeedFactor=Settings.BulletSpeedFactor

    def update(self):
        """Move the bullet up the screen"""
        #Update the decimal position of the bullet
        self.y-=self.SpeedFactor
        #Update the rect position
        self.rect.y=self.y

    def DrawBullet(self):
        """Draw the bullet to the screen"""
        GlowRect = self.rect.inflate(6, 6)
        pygame.draw.rect(self.Screen, (255, 180, 0), GlowRect)
        pygame.draw.rect(self.Screen, (255, 255, 255), self.rect)
        