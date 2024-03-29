import pygame
import random
class DamagePowerUp(pygame.sprite.Sprite):
    def __init__(self, x , y , img_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.dval = 50
        self.rect.centerx  = x
        self.rect.centery  = y

    def applyUpgrade(self , hero):
        """
            takes one parameter, the hero which is receiving the upgrade
            applies the damage upgrade to the hero
            returns nothing
        """
        hero.damage = hero.damage + self.dval


    def setPos(self,x , y):
        """
            takes x and y coordinates as parameters
            sets the position of the power-up
            returns nothing
        """
        self.rect.centerx = x
        self.rect.centery = y
    def getPos(self):
        """
            returns the postion of the power-up in a tuple (centerx,centery)
        """
        return (self.rect.centerx,self.rect.centery)
