# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 01:04:22 2022

@author: takep
"""

import pygame
from anim_dic import anim_dic
from anim_dic import anime_play

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
            self.images = [pygame.image.load("./assets/Player1/crab.png"),
                           pygame.image.load("./assets/Player1/dog.png"),
                           pygame.image.load("./assets/Player1/elephant.png"),
                           pygame.image.load("./assets/Player1/eagle.png"),
                           pygame.image.load("./assets/Player1/dog.png")
                           ]
            
            self.voices = [pygame.mixer.Sound("./assets/se/crab1.wav"),
                           pygame.mixer.Sound("./assets/se/dog1.wav"),
                           pygame.mixer.Sound("./assets/se/elephant1.wav"),
                           pygame.mixer.Sound("./assets/se/eagle1.wav"),
                           pygame.mixer.Sound("./assets/se/wolf1.wav")]
            a=200
            b=380
            self.rect = pygame.Rect(a,b,300,500)
            
        else:
            self.images = [pygame.image.load("./assets/Player2/crab.png"),
                           pygame.image.load("./assets/Player2/dog.png"),
                           pygame.image.load("./assets/Player2/elephant.png"),
                           pygame.image.load("./assets/Player2/eagle.png"),
                           pygame.image.load("./assets/Player2/eagle.png")]
            
            self.voices = [pygame.mixer.Sound("./assets/se/crab2.wav"),
                           pygame.mixer.Sound("./assets/se/dog2.wav"),
                           pygame.mixer.Sound("./assets/se/elephant2.wav"),
                           pygame.mixer.Sound("./assets/se/eagle2.wav"),
                           pygame.mixer.Sound("./assets/se/archaeopteryx.wav")]
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
        
        
        
class Effect(pygame.sprite.Sprite):
    
    def __init__(self, p1,idnum,a, b, c, d,vhan,hhan,anime_seq):
        pygame.sprite.Sprite.__init__(self)
        
        self.active = False #これがTrueだとエフェクトが開始する合図になる
        self.init = True
        self.count = 0
            
        self.anime_seq = anime_seq 
        
        self.invisible = pygame.image.load("./assets/invisible.png")
        
        #アニメ画像の登録
        self.animes, self.rect = anim_dic(p1,idnum)
        self.rect = pygame.Rect(a,b,100,100)
        
        for i in range(len(self.animes)):
            self.animes[i] = pygame.transform.scale(self.animes[i],(c,d))
            
        if vhan == True:
            for i in range(len(self.animes)):
                self.animes[i] = pygame.transform.rotate(self.animes[i],180)
              
        if hhan == True:
            for i in range(len(self.animes)):
                self.animes[i] = pygame.transform.rotate(self.animes[i],90)
            
    def update(self):
        if self.active == True:
            #開始時初期化処理
            if self.init == True:
                self.count = 0
                self.hantei = False 
                self.init = False
                
            #判定発生
            #if self.count == self.f_hantei:
               # self.hantei = True
                
            #アニメーションの再生　再生は一回限り
            self.image, end = anime_play(self.animes,self.anime_seq,self.count) 
                    
                
            if self.count >= sum(self.anime_seq):
                #正常終了
                self.active = False
                self.init = True
                
                return
            
        
        
            #開始時より時間軸管理のためのカウント増加
            self.count += 1
            
        else:
            self.image = self.invisible     