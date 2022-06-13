# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 14:19:11 2022

@author: takep
"""

import pygame
from anim_dic import anim_dic
from anim_dic import anime_play

class Partner(pygame.sprite.Sprite):
    
    def __init__(self, Player1: bool):
        pygame.sprite.Sprite.__init__(self)
        #両プレイヤーで共通の値を登録
        self.update_count = 0
        self.index = 0
        self.stand_seq =[6,6,6,6,6,6,6,6,6,6,6,6]
        
        #パートナーのアタックに関するメンバ
        self.attack_seq = [10,10,10,10] #attackするときのアニメのフレーム数割り当て
        self.attack = False
        self.hantei = False
        self.attack_init = True
        
        
        #アニメ画像の登録
        self.norm_animes, self.rect = anim_dic(Player1, 1)
        #self.attack_animes, self.rect1 = anim_dic(Player1, 4)
        
        
        #アニメ画像の変形
        #for num in range(len(self.norm_animes)):
            #self.norm_animes[num] = pygame.transform.scale(self.norm_animes[num], (200, 140))
            
        hoge = len(self.norm_animes)
        for num in range(hoge - 2):
            self.norm_animes.append(self.norm_animes[-2 - num])
            
        
        
        
        
        
        
    def update(self):
        
        #アニメ管理 
        self.image, end = anime_play(self.norm_animes,self.stand_seq,self.update_count, True)
        
        self.update_count += 1