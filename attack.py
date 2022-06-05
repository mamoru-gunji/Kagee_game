# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 15:27:02 2022

@author: takep
"""

import pygame
from anim_dic import anim_dic

class Attack(pygame.sprite.Sprite):
    
    def __init__(self, Player1: bool, animeid, frame_term, hantei_term, anime_seq):
        pygame.sprite.Sprite.__init__(self)
        
        self.active = False #これがTrueだと攻撃が開始する合図になる
        self.init = True
        self.count = 0
        if frame_term == -1:
            self.f_frame = 240000
        else:
            self.f_frame = frame_term#引数で指定する攻撃の終了時間
            
        self.f_hantei = hantei_term#引数で指定する判定の発生時間
        self.fin = False #正常終了を外部に伝えるためのbool
        self.hantei = False #判定発生を外部に伝えるためのbool
        self.anime_seq = anime_seq #それぞれのアニメフレームの継続フレーム数を記述したリスト　アニメの枚数と同じでなければならない
        
        self.invisible = pygame.image.load("./assets/invisible.png")
        
        #アニメ画像の登録
        self.animes, self.rect = anim_dic(Player1,animeid)
            
    def update(self):
        if self.active == True:
            #開始時初期化処理
            if self.init == True:
                self.count = 0
                self.fin = False 
                self.hantei = False 
                self.init = False
                
            #判定発生
            if self.count == self.f_hantei:
                self.hantei = True
                
            #アニメーションの再生　再生は一回限り
            if self.count <= self.anime_seq[0]:
                self.image = self.animes[0]
            elif self.count >= sum(self.anime_seq):
                self.image = self.animes[-1]
            else:
                hoge = 0
                for num in range(len(self.anime_seq)):
                    hoge += self.anime_seq[num]
                    if hoge > self.count:
                        self.image = self.animes[num]
                        break
                    
                
            if self.count >= self.f_frame:
                #正常終了
                self.fin = True
                self.active = False
                self.init = True
                
                return
            
        
        
            #開始時より時間軸管理のためのカウント増加
            self.count += 1
            
        else:
            self.image = self.invisible