# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 00:05:56 2022

@author: takep
"""

import pygame
from anim_dic import anim_dic
from anim_dic import anime_play

class Defence(pygame.sprite.Sprite):
    
    def __init__(self, Player1: bool, animeid, hantei_term, anime_seq):
        pygame.sprite.Sprite.__init__(self)
        
        self.active = False #これがTrueだとコマンドが開始する合図になる
        self.init = True
        self.count = 0

            
        self.f_hantei = hantei_term#引数で指定する判定の発生時間
        self.fin = False #正常終了を外部に伝えるためのbool
        self.hantei = False #判定発生を外部に伝えるためのbool
        self.anime_seq = anime_seq #それぞれのアニメフレームの継続フレーム数を記述したリスト　アニメの枚数と同じでなければならない

        #カニの死亡
        self.death = False
        self.death_init = True
        self.death_seq = [3,3,3,3,3,3,3,3,3,3,3,3]
        
        self.invisible = pygame.image.load("./assets/invisible.png")
        
        #アニメ画像の登録
        self.animes, self.rect = anim_dic(Player1,animeid)
        self.death_animes,rec = anim_dic(Player1,14)
            
    def update(self):
        
        if self.death == True:
            if self.death_init == True:
                self.count = 0
                self.hantei = False 
                self.init = True
                self.active =False
                self.death_init = False
                
            #アニメーションの再生　再生は一回限り
            
            self.image, end = anime_play(self.death_animes,self.death_seq,self.count) 
            
            if self.count >= sum(self.death_seq):
                self.death = False
                self.death_init = True
        
        
        
        elif self.active == True:
            #開始時初期化処理
            if self.init == True:
                self.count = 0 
                self.hantei = False 
                self.init = False
                
            #判定発生
            if self.count == self.f_hantei:
                self.hantei = True
                
            #アニメーションの再生　再生は一回限り
            
            self.image, end = anime_play(self.animes,self.anime_seq,self.count) 
                    
                
             
        else:
            self.image = self.invisible
            
        self.count += 1