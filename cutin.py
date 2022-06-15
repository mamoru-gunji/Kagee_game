# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 01:04:22 2022

@author: takep
"""

import pygame

class Cutin(pygame.sprite.Sprite):
    
    def __init__(self, Player1: bool, cutin_id):
        pygame.sprite.Sprite.__init__(self)
        
        self.active = False #これがTrueだとコマンドが開始する合図になる
        self.init = True
        self.count = 0
        self.keisu = [120,100,0.15,15]#縦、横、大きくなるペース、アニメの枚数
        self.animes = []
        self.rects = []
            

        
        self.invisible = pygame.image.load("./assets/invisible.png")
        
        if Player1 == True:
            self.images = [pygame.image.load("./assets/Player1/crab.png")]
            self.voices = [pygame.mixer.Sound("./assets/se/crab1.wav")]
            a=200
            b=380
            self.rect = pygame.Rect(a,b,300,500)
            
        else:
            self.images = [pygame.image.load("./assets/Player2/crab.png")]
            self.voices = [pygame.mixer.Sound("./assets/se/crab2.wav")]
            a=950
            b=380
            self.rect = pygame.Rect(a,b,300,500)
            
        self.origin = pygame.transform.scale(self.images[cutin_id],(self.keisu[0],self.keisu[1]))
        self.voice = self.voices[cutin_id]

        for i in range(self.keisu[3]):
            self.animes.append(pygame.transform.scale(self.images[cutin_id], ((int)(self.keisu[0] * (1 + self.keisu[2] * i)), (int)(self.keisu[1] * (1 + self.keisu[2] * i)))))
            self.rects.append(pygame.Rect((int)(a - self.keisu[0] * ((self.keisu[2] * i) / 2)),(int)(b - self.keisu[1] * ((self.keisu[2] * i) / 2)),0,0))
        
        
    def update(self):
        if self.active == True:
            #開始時初期化処理、音声の再生含む
            if self.init == True:
                self.count = 0
                self.init = False
                self.voice.play()

            
            #アニメーションの再生　再生は一回限り
            self.image = self.animes[self.count]
            self.rect = self.rects[self.count]
            
            #終了処理
            if self.count == (self.keisu[3] - 1):
                self.active = False
                self.init = True
            
        else:
            self.image = self.invisible
            
        self.count += 1