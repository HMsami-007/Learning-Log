import sys
from time import sleep
import pygame
from BulletClass import Bullet
from AlienClass import Alien
from ScoreboardClass import Scoreboard
def CheckEvents(GameSetting, Screen, Stats, PlayButton, Ship, Bullets, Aliens,Scoreboard):
    """Respond to keypresses and mouse events."""
    for Event in pygame.event.get():
        if Event.type==pygame.QUIT:
            sys.exit()

        elif Event.type == pygame.MOUSEBUTTONDOWN:
            MouseX, MouseY = pygame.mouse.get_pos()
            # Check if the click coordinates overlap the button box
            if PlayButton.Rect.collidepoint(MouseX, MouseY) and not Stats.GameActive:
                GameSetting.InitializeDynamicSettings()
                Stats.ResetStats()
                Stats.GameActive = True
                Scoreboard.PrepScore()
                Scoreboard.PrepHighScore()
                Scoreboard.PrepLevel()
                Scoreboard.PrepShips()
                Aliens.empty()
                Bullets.empty()
                CreateFleet(GameSetting, Screen, Aliens)
                Ship.CenterShip()

        elif Event.type==pygame.KEYDOWN:
            if Event.key==pygame.K_RIGHT:
                Ship.MovingRight=True
            elif Event.key==pygame.K_LEFT:
                Ship.MovingLeft=True
            elif Event.key==pygame.K_UP:
                Ship.MovingUp=True
            elif Event.key==pygame.K_DOWN:
                Ship.MovingDown=True
            elif Event.key==pygame.K_SPACE:
                if len(Bullets)<GameSetting.BulletsAllowed:
                    NewBullet=Bullet(GameSetting,Screen,Ship)
                    Bullets.add(NewBullet)
            elif Event.key==pygame.K_q:
                sys.exit()

        elif Event.type==pygame.KEYUP:
            if Event.key==pygame.K_RIGHT:
                Ship.MovingRight=False
            elif Event.key==pygame.K_LEFT:
                Ship.MovingLeft=False
            elif Event.key==pygame.K_UP:
                Ship.MovingUp=False
            elif Event.key==pygame.K_DOWN:
                Ship.MovingDown=False

def CreateFleet(GameSetting,Screen,Aliens):
    AlienObject=Alien(GameSetting,Screen)
    AlienWidth=AlienObject.rect.width
    AlienHeight=AlienObject.rect.height
    AvailableSpaceX=GameSetting.ScreenWidth-2*AlienWidth
    NumberAliensX=int(AvailableSpaceX/(2*AlienWidth))
    NumberOfRows=4
    for RowNo in range(NumberOfRows):
        for AlienNo in range(NumberAliensX):
            AlienObject=Alien(GameSetting,Screen)
            AlienObject.x=AlienWidth+2*AlienWidth*AlienNo
            AlienObject.rect.x=AlienObject.x
            AlienObject.rect.y=AlienHeight+2*AlienHeight*RowNo
            Aliens.add(AlienObject)

def CheckFleetEdges(GameSetting, Aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for UFO in Aliens.sprites():
        # Check if the alien hit the left or right edge
        screen_rect = UFO.Screen.get_rect()
        if UFO.rect.right >= screen_rect.right or UFO.rect.left <= 0:
            ChangeFleetDirection(GameSetting, Aliens)
            break

def ChangeFleetDirection(GameSetting, Aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for UFO in Aliens.sprites():
        UFO.rect.y += GameSetting.FleetDropSpeed
    GameSetting.FleetDirection *= -1

def ShipHit(GameSetting,Stats,Screen,Ship,Aliens,Bullets,PlayButton,SB):
    if Stats.ShipsLeft > 0:
        Stats.ShipsLeft-=1
        SB.PrepShips()
        Aliens.empty()
        Bullets.empty()
        CreateFleet(GameSetting,Screen,Aliens)
        Ship.CenterShip()
        sleep(0.1)
    else:
        Stats.GameActive = False
        pygame.mouse.set_visible(True)
        PlayButton.PrepMessage("Play Again") 
        

def UpdateAliens(GameSetting,Stats,Screen,Ship,Aliens,Bullets,PlayButton,SB):   
    """Check if the fleet is at an edge, then update all positions."""
    CheckFleetEdges(GameSetting, Aliens)
    Aliens.update() # This automatically runs the update method inside AlienClass
    Ship.rect = Ship.Rect 
    if pygame.sprite.spritecollideany(Ship, Aliens):
        ShipHit(GameSetting,Stats,Screen,Ship,Aliens,Bullets,PlayButton,SB)
    HitAliens = pygame.sprite.spritecollide(Ship, Aliens, True)
    for UFO in HitAliens:
        print("Ship Hit!!!")

def CheckHighScore(Stats,Scoreboard):
    if Stats.Score>Stats.HighScore:
        Stats.HighScore=Stats.Score
        Scoreboard.PrepHighScore()



