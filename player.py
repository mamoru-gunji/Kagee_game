# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 22:23:59 2022

@author: takep
"""

import pygame
from anim_dic import anim_dic
from anim_dic import anime_play

class Player(pygame.sprite.Sprite):
    
    def __init__(self, Player1: bool):
        pygame.sprite.Sprite.__init__(self)
        #両プレイヤーで共通の値を登録
        
        self.gauge = 0.0 #必殺ゲージ
        self.update_count = 0
        self.index = 0
        self.animerate = 60 #この数字を変えるとアニメの一ループの時間が変わる。60で一秒。120で二秒。
        
        self.hirumi = False #これがTrueのとき怯み状態であり、無敵
        self.hirumi_init = True #怯み処理の初期化
        self.excute = False#これがTrueのとき影絵出すアニメ再生
        self.excute_init = True #影絵出す処理の初期化
        self.hirumi_seq = [10,10,40]#怯みアニメのフレーム配分。これらの合計が怯み時間となる。
        self.norm_seq = [5,5,5,5,5,5,5,5,5,5,5,5]
        
        #アニメ画像の登録
        self.norm_animes, self.rect = anim_dic(Player1, 0)
        self.hirumi_animes, self.rect1 = anim_dic(Player1, 3)
        self.excute_animes, rec = anim_dic(Player1,4)
        
        #両プレイヤーで値が違う場合
        if Player1 == True:
            self.excute_seq = [0,1,1,1,1,1,1,1,1,1,1,1,1,15]
        else:
            self.excute_seq = [0,0,0,1,1,1,1,1,1,1,1,15]
        
            
        #アニメ画像の変形
        #for num in range(len(self.norm_animes)):
            #self.norm_animes[num] = pygame.transform.scale(self.norm_animes[num], (250, 250))
        
        for num in range(len(self.hirumi_animes)):
            self.hirumi_animes[num] = pygame.transform.scale(self.hirumi_animes[num], (150, 250))
            
        hoge = len(self.norm_animes)
        for num in range(hoge - 2):
            self.norm_animes.append(self.norm_animes[-2 - num])
            
        
        
        
        
        
        
    def update(self):
        
        if self.hirumi == True:
            if self.hirumi_init == True:
                self.hirumi_init = False
                self.update_count = 0
                
             #アニメーションの再生　再生は一回限り
            self.image, end = anime_play(self.hirumi_animes,self.hirumi_seq,self.update_count)
            
            if self.update_count >= sum(self.hirumi_seq):
                #怯みの正常終了
                 self.hirumi = False
                 self.hirumi_init = True
                 self.hirumi_seq[-1] = 40#怯み時間を正常化
                 
            
        elif self.excute == True:
            if self.excute_init == True:
                self.excute_init = False
                self.update_count = 0
                
             #アニメーションの再生　再生は一回限り
            self.image, end = anime_play(self.excute_animes,self.excute_seq,self.update_count)
            
            if self.update_count >= sum(self.excute_seq):
                #影絵出しの正常終了
                 self.excute = False
                 self.excute_init = True
                 
            
        
        else:
            #アニメ管理 (立ち姿)
            self.image, end = anime_play(self.norm_animes,self.norm_seq,self.update_count, True)
            
                
        self.update_count += 1
        