# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 14:01:46 2022

@author: takep
"""

import pygame
from anim_dic import anim_dic

class Hp(pygame.sprite.Sprite):
    
    def __init__(self, Player1: bool):
        pygame.sprite.Sprite.__init__(self)
        
        self.hp = 100.0
        
        
class Hissatsu(pygame.sprite.Sprite):
    
    def __init__(self, Player1: bool):
        pygame.sprite.Sprite.__init__(self)
        
        self.value = 0.0    
        self.max_value = 100.0
        
    def update(self):
        if self.value > self.max_value:
            self.value = self.max_value