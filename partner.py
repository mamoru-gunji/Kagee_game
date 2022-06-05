# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 14:19:11 2022

@author: takep
"""

import pygame

class Partner(pygame.sprite.Sprite):
    
    def __init__(self, Player1: bool):
        pygame.sprite.Sprite.__init__(self)
        #両プレイヤーで共通の値を登録
        self.update_count = 0
        self.index = 0
        self.animerate = 60 #この数字を変えるとアニメの一ループの時間が変わる。60で一秒。120で二秒。
        
        #アニメ画像の登録
        if(Player1 == True):
            self.norm_animes = [pygame.image.load("./assets/Player1/part1.png"),
                                pygame.image.load("./assets/Player1/part1.png"),
                                pygame.image.load("./assets/Player1/part2.png"),
                                pygame.image.load("./assets/Player1/part3.png")]
            self.rect = pygame.Rect(250,500,100,100)
        else:
            self.norm_animes = [pygame.image.load("./assets/Player2/part1.png"),
                                pygame.image.load("./assets/Player2/part1.png"),
                                pygame.image.load("./assets/Player2/part2.png"),
                                pygame.image.load("./assets/Player2/part3.png")]
            self.rect = pygame.Rect(750,500,100,100)
            
        #アニメ画像の変形
        for num in range(len(self.norm_animes)):
            self.norm_animes[num] = pygame.transform.scale(self.norm_animes[num], (200, 140))
            
        hoge = len(self.norm_animes)
        for num in range(hoge - 2):
            self.norm_animes.append(self.norm_animes[-2 - num])
            
        
        
        
        
        
        
    def update(self):
        
        #アニメ管理 
        self.framerate = self.animerate / len(self.norm_animes)
        
        if((self.update_count % int(self.framerate)) == 0):
            self.index += 1
            
        if self.index >= len(self.norm_animes):
            self.index = 0
            
        self.image = self.norm_animes[self.index]
        self.update_count += 1
        if(self.update_count == 60):
            self.update_count = 0
        