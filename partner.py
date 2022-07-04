# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 14:19:11 2022

@author: takep
"""

import pygame
from anim_dic import anim_dic
from anim_dic import anime_play
from attack import Dog_atk,Eagle_atk,Hissatsu2

class Partner(pygame.sprite.Sprite):
    
    def __init__(self, Player1: bool):
        pygame.sprite.Sprite.__init__(self)
        #両プレイヤーで共通の値を登録
        self.update_count = 0
        self.index = 0
        self.stand_seq =[6,6,6,6,6,6,6,6,6,6,6,6]
        #パートナーのアタックに関するメンバ
        
        self.attack = False
        self.hantei = False
        self.attack_init = True
        self.crab = False
        self.dog_se = pygame.mixer.Sound("./assets/se/dog.wav")
        self.wolf_2_1 = pygame.mixer.Sound("./assets/se/wolf2_1.wav")
        self.arche2_1 = pygame.mixer.Sound("./assets/se/arche.wav")
        self.Player1 = Player1
        self.invisible = pygame.image.load("./assets/invisible.png")
        
        #必殺関係
        self.hissatsu = False
        self.hissatsu_init = True
        self.black = False
        self.hissatsu_seq = [6,6,6,6,6,6,6,6,6,6,6,6]
        
        self.hissatsu2 = Hissatsu2(Player1)
            
        #death関連
        self.death = False
        self.death_init = True
        self.death_seq = [6,6,6,6,6,6,6,6,6,6,6,6]
        
        #アニメ画像の登録
        self.norm_animes, self.rect = anim_dic(Player1, 1)
        self.trans_animes,self.rect_t = anim_dic(Player1, 10)
        self.death_animes,rec = anim_dic(Player1,13)
        if Player1 == True:
            
            self.attack_animes, self.rect1 = anim_dic(Player1, 5)
            
            self.attack_seq = [50,0,4,4,4,3,4,4,3,3,3,3] #attackするときのアニメのフレーム数割り当て
            self.dog_atk = Dog_atk(0,50)
            self.dog_atk1 = Dog_atk(-270,50)
            
            self.trans_seq = [60,3,3,3,4,4,4,4,7,7,1,1,1,1,4,4,5,5,4,3,3,3,3,12]
            
        
        else:
            self.attack_animes, self.rect1 = anim_dic(True, 11)
            self.attack_seq = [4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,3,3,3,3,3,3] #attackするときのアニメのフレーム数割り当て
            
            self.eagle_atk = Eagle_atk(0,0)
            self.eagle_atk1 = Eagle_atk(220,0)
            
            
            self.trans_seq = [17,4,4,4,
                              4,4,4,4,
                              4,4,4,4,
                              4,4,4,4,
                              4,4,4,4,
                              4,4,4,4,
                              4,4,4,4,
                              4,4,4,4,
                              4,4,4,4,
                              4,4,4,4,
                              4,4,4,4,
                              4,4,4,20]
        
        
        #アニメ画像の変形
        #for num in range(len(self.norm_animes)):
            #self.norm_animes[num] = pygame.transform.scale(self.norm_animes[num], (200, 140))
            
        
        
        
    def update(self):
        #通常アタック関係
        if self.attack == True:
            if self.attack_init == True:
                self.update_count = 0
                self.attack_init = False
        
            self.image, end = anime_play(self.attack_animes,self.attack_seq,self.update_count) 
            
            if self.Player1 == True:
                
                if self.update_count == 42:
                    self.dog_se.play()
                    
                if self.update_count == 69:
                    if self.crab == False:
                        
                        self.dog_atk.active = True
                        
                    else:
                        self.dog_atk1.active = True
                
                if self.update_count >= (sum(self.attack_seq) + sum(self.dog_atk.anime_seq)):
                    #正常終了
                    self.attack = False
                    self.attack_init = True
                    
            else:
                if self.update_count == 59:
                    if self.crab == False:
                        
                        self.eagle_atk.active = True
                        
                    else:
                        self.eagle_atk1.active = True
                if self.update_count >= (sum(self.attack_seq)+ sum(self.eagle_atk.anime_seq)):
                    #正常終了
                    self.attack = False
                    self.attack_init = True
                 
         #必殺技関係
        elif self.hissatsu == True:
            if self.hissatsu_init == True:
                self.update_count = 0
                self.hissatsu_init = False
                
            self.image, end = anime_play(self.trans_animes,self.trans_seq,self.update_count) 
            
            if self.Player1 == True:
                if self.update_count == 61:
                    self.black = True
                    self.wolf_2_1.play()
            else:
                if self.update_count == 61:
                    self.black = True
                    self.arche2_1.play()
                
            if self.update_count >= sum(self.trans_seq):
                #正常終了
                self.hissatsu = False
                self.hissatsu_init = True
                self.hissatsu2.active = True
                self.black = False
           #必殺技　段階2　無敵
        elif self.hissatsu2.active == True:
           self.image = self.invisible
                
             #死亡   
        elif self.death == True:
            if self.death_init == True:
                self.death_init = False
                self.update_count = 0
                
             #アニメーションの再生　再生は一回限り
            self.image, end = anime_play(self.death_animes,self.death_seq,self.update_count)
            
            if self.update_count >= sum(self.death_seq):
                self.finish = True
                
        else:
            
            #アニメ管理 
            self.image, end = anime_play(self.norm_animes,self.stand_seq,self.update_count, True)
            
        self.update_count += 1
        
        
        
class Partnerf(pygame.sprite.Sprite):
    
    def __init__(self, Player1: bool):
        pygame.sprite.Sprite.__init__(self)
        #両プレイヤーで共通の値を登録
        self.active = False
        self.active1 = False 
        self.update_count = 0
        self.init = True
        self.stand_seq =[6,6,6,6,6,6,6,6,6,6,6,6]
        self.born_seq = [5,5,5,5,5,5,5,5,5,5,5,5]
        #パートナーのアタックに関するメンバ
        

        self.crab = False
        self.dog_se = pygame.mixer.Sound("./assets/se/dog.wav")
        self.eagle_se = pygame.mixer.Sound("./assets/se/eagle.wav")
        self.eagle_se.set_volume(0.15)
        
        self.Player1 = Player1
        if Player1 == True:
            
            self.default_pic = pygame.image.load("./assets/dogf.png")
        else:
            self.default_pic = pygame.image.load("./assets/eaglef.png")

        
        #アニメ画像の登録
        self.norm_animes, self.rect = anim_dic(Player1, 1)

        self.born_animes,rec = anim_dic(Player1,15)

   
        
        
    def update(self):
        if self.active == True:
            if self.init == True:
                self.init = False
                self.update_count = 0
                
            self.image, end = anime_play(self.born_animes,self.born_seq,self.update_count, False)
            
            if self.update_count == 30:
                if self.Player1 == True:
                    self.dog_se.play()
                else:
                    self.eagle_se.play()
                    
            if self.update_count >= sum(self.born_seq):
                self.active = False
                self.active1 = True
        elif self.active1 == True:
            self.image, end = anime_play(self.norm_animes,self.stand_seq,self.update_count, True)
            
        else:
            self.image = self.default_pic
            
        self.update_count += 1