import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,GameSetting,Screen):
        super(Alien,self).__init__()
        self.Screen=Screen
        self.GameSetting=GameSetting
        self.RawImage=pygame.image.load("UFO.png")
        self.Image=pygame.transform.scale(self.RawImage,(85,50))
        self.rect=self.Image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height  
        self.x=float(self.rect.x)

    def blitme(self):
        self.Screen.blit(self.Image,self.rect)      

    def update(self): # Note: lowercase "update" allows Pygame Group automation!
        """Move the alien left or right based on fleet direction settings."""
        self.x += (self.GameSetting.AlienSpeedFactor * self.GameSetting.FleetDirection)
        self.rect.x = self.x