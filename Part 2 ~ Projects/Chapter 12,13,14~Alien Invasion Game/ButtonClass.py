import pygame.font
class Button():
    def __init__(self,GameSetting,Screen,Msg):
        self.Screen=Screen
        self.ScreenRect=Screen.get_rect()
        self.Width,self.Height=200,50
        self.ButtonColour=(235, 95, 15)
        self.TextColour=(255,255,255)
        self.Font=pygame.font.Font(None,48)
        self.Rect=pygame.Rect(0,0,self.Width,self.Height)
        self.Rect.center=self.ScreenRect.center
        self.PrepMessage(Msg)

    def PrepMessage(self,Msg):
        self.MsgImage=self.Font.render(Msg,True,self.TextColour,self.ButtonColour)
        self.MsgImageRect=self.MsgImage.get_rect()
        self.MsgImageRect.center=self.Rect.center

    def DrawButton(self):
        # Using draw.rect lets us pass an optional border_radius parameter
        pygame.draw.rect(self.Screen, self.ButtonColour, self.Rect, border_radius=12)
        self.Screen.blit(self.MsgImage, self.MsgImageRect)
        