# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 22:23:59 2022

@author: takep
"""

import pygame

class Player(pygame.sprite.Sprite):
    
    def __init__(self, Player1: bool):
        pygame.sprite.Sprite.__init__(self)
        #両プレイヤーで共通の値を登録
        self.hp = 100.0
        self.gauge = 0.0 #必殺ゲージ
        self.update_count = 0
        self.index = 0
        self.animerate = 60 #この数字を変えるとアニメの一ループの時間が変わる。60で一秒。120で二秒。
        
        #アニメ画像の登録
        if(Player1 == True):
            self.norm_animes = [pygame.image.load("./assets/Player1/norm1.png"),
                                pygame.image.load("./assets/Player1/norm2.png"),
                                pygame.image.load("./assets/Player1/norm3.png")]
            self.rect = pygame.Rect(100,400,300,500)
        else:
            self.norm_animes = [pygame.image.load("./assets/Player2/norm1.png"),
                                pygame.image.load("./assets/Player2/norm2.png"),
                                pygame.image.load("./assets/Player2/norm3.png")]
            self.rect = pygame.Rect(1000,400,300,500)
            
        #アニメ画像の変形
        for num in range(len(self.norm_animes)):
            self.norm_animes[num] = pygame.transform.scale(self.norm_animes[num], (150, 250))
            
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
        