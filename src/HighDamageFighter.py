import pygame
from src import Hero
class HighDamageFighter(Hero.Hero):
    def __init__(self, name, x, y, direction, img_file):
        Hero.Hero.__init__(self, name, x, y, direction, img_file)
        self.health = 200
        self.damage = 50
        self.restTime = 3
    
 
