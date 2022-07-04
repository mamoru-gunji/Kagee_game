# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 14:01:46 2022

@author: takep
"""

import pygame
from anim_dic import anim_dic,anime_play

class Hp(pygame.sprite.Sprite):
    
    def __init__(self, Player1: bool, screen):
        pygame.sprite.Sprite.__init__(self)
        
        self.hp = 100.0
        self.prehp = 100.0
        self.yellowlength = 0
        self.prehp2 = 100.0
        self.screen = screen
        self.Player1 = Player1
        self.count = 0
        self.precount = 0
        self. yellow = False
        
    def update(self):
        if self.hp <= 0.0:
            self.hp = 0.0
            
        if self.prehp != self.hp:
            self.yellow = True
            self.precount = self.count
            
        self.yellowlength = (int)((self.prehp2 - self.hp) * 4)
        
        if self.yellowlength <= 0:
            self.yellow = False
            self.prehp2 = self.hp
            
        if self.yellow == True:
            if (self.count - self.precount) > 45:
                self.prehp2 -= 0.50
            
            if self.Player1 == True:
                a = 105 + (int)(self.hp * 3.3)
                b = 38
                c = self.yellowlength
                d = 50
                
            else:
                a = (int)(849 + 3.3 * (100 - self.prehp2))
                b = 38
                c = self.yellowlength
                d = 50
                
            pygame.draw.rect(self.screen, (255,255,100), pygame.Rect(a,b,c,d), width=0)
            
            
            
                
        
        if self.Player1 == True:
            a = 105
            b = 38
            c = (int)(self.hp * 3.3)
            d = 50
            
        else:
            a = (int)(849 + 3.3 * (100 - self.hp))
            b = 38
            c = (int)(self.hp * 3.3)
            d = 50
            
        pygame.draw.rect(self.screen, (255,0,0), pygame.Rect(a,b,c,d), width=0)
            
        self.prehp = self.hp
        self.count += 1
        
class Hissatsu(pygame.sprite.Sprite):
    
    def __init__(self, Player1: bool, screen):
        pygame.sprite.Sprite.__init__(self)
        
        self.value = 0.0    
        self.max_value = 100.0
        self.screen = screen
        self.Player1 = Player1
        self.count = 0
        
    def update(self):
        if self.value > self.max_value:
            self.value = self.max_value
        
        if self.Player1 == True:
            a = 98
            b = 140
            c = (int)(self.value * 2.51)
            d = 35
            
        else:
            a = (int)(939 + 2.51 * (100 - self.value))
            b = 140
            c = (int)(self.value * 2.51)
            d = 35
         
        if self.value == self.max_value:
            if (self.count % 20) >= 10:
                tup = (180,180,255)
            else:
                tup = (100,100,255)
        else:
            tup = (100,100,255)
        pygame.draw.rect(self.screen, tup, pygame.Rect(a,b,c,d), width=0)
        
        self.count += 1
        
class Background(pygame.sprite.Sprite):  
        def __init__(self):
         pygame.sprite.Sprite.__init__(self)
         
         self.count = 0
         self.animes, self.rect = anim_dic(True, 16)
         self.seq=[12,6,18,6,6,6,6,6,6]
         
        def update(self):
            self.image, end = anime_play(self.animes,self.seq,self.count,True)
            
            self.count += 1
            
class Countdown(pygame.sprite.Sprite):  
        def __init__(self):
         pygame.sprite.Sprite.__init__(self)
         
         self.count = 0
         self.finish = False
         self.active = False
         self.init = True
         self.animes, self.rect = anim_dic(False, 16)
         self.invisible = pygame.image.load("./assets/invisible.png")
         self.seq=[60,60,60,30]
         self.se = [pygame.mixer.Sound("./assets/se/three.wav"),pygame.mixer.Sound("./assets/se/two.wav"),pygame.mixer.Sound("./assets/se/one.wav"),
                    pygame.mixer.Sound("./assets/se/fight.wav")]
         
        def update(self):
            if self.active == True:
                if self.init == True:
                    self.count = 0
                    self.init = False
                    
                self.image, end = anime_play(self.animes,self.seq,self.count,False)
                if self.count == 1:
                    self.se[0].play()
                if self.count == 61:
                    self.se[1].play()
                if self.count == 121:
                    self.se[2].play()
                if self.count == 181:
                    self.se[3].play()
                    
                if self.count >= sum(self.seq):
                    self.finish = True
                    self.active = False
            else:
                self.image = self.invisible
                
            self.count += 1
            