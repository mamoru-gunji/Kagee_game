# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 15:27:02 2022

@author: takep
"""

import pygame
from anim_dic import anim_dic
from anim_dic import anime_play
from cutin import Effect
import warnings
warnings.filterwarnings('ignore')

class Attack(pygame.sprite.Sprite):
    
    def __init__(self, Player1: bool, animeid, se_voice, hantei_term, anime_seq):
        pygame.sprite.Sprite.__init__(self)
        
        self.active = False #これがTrueだと攻撃が開始する合図になる
        self.init = True
        self.count = 0
        self.f_frame = sum(anime_seq)#引数で指定する攻撃の終了時間
        
            
        self.f_hantei = hantei_term#引数で指定する判定の発生時間
        self.fin = False #正常終了を外部に伝えるためのbool
        self.hantei = False #判定発生を外部に伝えるためのbool
        self.anime_seq = anime_seq #それぞれのアニメフレームの継続フレーム数を記述したリスト　アニメの枚数と同じでなければならない
        
        self.invisible = pygame.image.load("./assets/invisible.png")
        self.se = pygame.mixer.Sound(se_voice[0])
        self.voice = pygame.mixer.Sound(se_voice[1])
        
        self.voicef = se_voice[2]
        
        #アニメ画像の登録
        self.animes, self.rect = anim_dic(Player1,animeid)
        self.rectx = self.rect.x
            
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
            self.image, end = anime_play(self.animes,self.anime_seq,self.count) 
                    
            #音声再生
            
            if self.count == self.voicef:
                self.voice.play()
                
            if self.count >= self.f_frame:
                #正常終了
                self.fin = True
                self.active = False
                self.init = True
                self.rect.x = self.rectx
                
                return
            
        
        
            #開始時より時間軸管理のためのカウント増加
            self.count += 1
            
        else:
            self.image = self.invisible
            
            
class Dog_atk(pygame.sprite.Sprite):
    
    def __init__(self, a, b):
        pygame.sprite.Sprite.__init__(self)
        
        self.active = False #これがTrueだと攻撃が開始する合図になる
        self.init = True
        self.count = 0
        self.effect = Effect(True,6,825 + a,230 + b,400,400,False,False,[3,3,3,3,3,3,5,5])
            
        #self.f_hantei = hantei_term#引数で指定する判定の発生時間
        self.fin = False #正常終了を外部に伝えるためのbool
        self.hantei = False #判定発生を外部に伝えるためのbool
        self.anime_seq = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2] #犬がでてくるアニメの設定
        self.se = pygame.mixer.Sound("./assets/se/nail.wav")
        
        self.invisible = pygame.image.load("./assets/invisible.png")
        
        #アニメ画像の登録
        self.animes, self.rect = anim_dic(False,5)
        self.rect = pygame.Rect(a,b,100,100)
            
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
            
            if self.count == 12:
               self.effect.active = True
               self.hantei = True
               self.se.play()
                
            if self.count >= sum(self.anime_seq):
                #正常終了
                self.active = False
                self.init = True
                
                return
            
        
        
            #開始時より時間軸管理のためのカウント増加
            self.count += 1
            
        else:
            self.image = self.invisible         

class Elephant(pygame.sprite.Sprite):
    
    def __init__(self, p1):
        pygame.sprite.Sprite.__init__(self)
        
        self.active = False #これがTrueだとエフェクトが開始する合図になる
        self.active1 = False
        self.init = True
        self.init1 = True
        self.count = 0
            
        self.anime_seq = [3,3,3,3,3,3,3,3,3,3,3,480]
        self.se = pygame.mixer.Sound("./assets/se/elephant.wav")
        
        self.invisible = pygame.image.load("./assets/invisible.png")
        
        #アニメ画像の登録
        self.animes, self.rect = anim_dic(p1,7)
        self.rectx = self.rect.x
        self.p1 = p1
            
    def update(self):
        if ((self.active == True) and (self.active1 == False)):
            #開始時初期化処理
            if self.init == True:
                self.count = 0
                self.init = False
                
                
            if self.count >= 30:
                #正常終了
                self.active = False
                self.active1 = True
                self.init = True
                
                return
            
            #開始時より時間軸管理のためのカウント増加
            self.count += 1
        

        if self.active1 == True:
            if self.init1 == True:
                self.count = 0
                self.init1 = False
                self.rect.x = self.rectx
            #アニメーションの再生　再生は一回限り
            self.image, end = anime_play(self.animes,self.anime_seq,self.count) 
            
            if self.count == 12:
                self.se.play()
            if self.count > 460:
                
                if self.p1 == True:
                    self.rect.x -= 20
                else:
                    self.rect.x += 30
                
            if self.count >= sum(self.anime_seq):
                #正常終了
                self.active1 = False
                
                self.init1 = True
                
            #開始時より時間軸管理のためのカウント増加
            self.count += 1
        
            
        else:
            self.image = self.invisible     
    
class Eagle_atk(pygame.sprite.Sprite):
    
    def __init__(self, a, b):
        pygame.sprite.Sprite.__init__(self)
        
        self.active = False #これがTrueだと攻撃が開始する合図になる
        self.init = True
        self.count = 0
        #self.effect = Effect(True,6,825 + a,230 + b,400,400,False,False,[3,3,3,3,3,3,5,5])
            
        #self.f_hantei = hantei_term#引数で指定する判定の発生時間
        self.fin = False #正常終了を外部に伝えるためのbool
        self.hantei = False #判定発生を外部に伝えるためのbool
        self.anime_seq = [4,4,4,4,4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0] #鷲がでてくるアニメの設定
        self.se = pygame.mixer.Sound("./assets/se/nail.wav")
        
        self.invisible = pygame.image.load("./assets/invisible.png")
        
        #アニメ画像の登録
        self.animes, self.rect = anim_dic(False,11)
        self.rect = pygame.Rect(a,b,100,100)
            
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
            
            if self.count == 22:
               #self.effect.active = True
               self.hantei = True
               self.se.play()
                
            if self.count >= sum(self.anime_seq):
                #正常終了
                self.active = False
                self.init = True
                
                return
            
        
        
            #開始時より時間軸管理のためのカウント増加
            self.count += 1
            
        else:
            self.image = self.invisible         
            
            
class Hissatsu2(pygame.sprite.Sprite):
    
    def __init__(self, Player1):
        pygame.sprite.Sprite.__init__(self)
        self.active = False #これがTrueだと攻撃が開始する合図になる
        self.init = True
        self.count = 0
        self.hantei = [False,False,False,False]
        self.animes, self.rect = anim_dic(Player1,17)
        
        self.invisible = pygame.image.load("./assets/invisible.png")
        self.p1 = Player1
        self.keisu = 4
        self.se = [pygame.mixer.Sound("./assets/se/wolf2_2.wav"), pygame.mixer.Sound("./assets/se/wolf2_3.wav"),pygame.mixer.Sound("./assets/se/wolf2_4.wav"),
                   pygame.mixer.Sound("./assets/se/nail.wav"),pygame.mixer.Sound("./assets/se/nail2.wav")]
        self.seq = []
        if Player1 ==  True:
            
            for i in range(68):
                self.seq.append(self.keisu)
        else:
            for i in range(66):
                self.seq.append(self.keisu)
            
            
    def update(self):
        if self.active == True:
            #開始時初期化処理
            if self.init == True:
                self.count = 0
                self.hantei = [False,False,False,False]
                self.init = False
                
            self.image, end = anime_play(self.animes,self.seq,self.count)
            if self.p1 == True:
                if self.count == self.keisu * (18):
                    self.se[2].play()
                if self.count == self.keisu * (26 + 7):
                    self.hantei[0] = True
                    self.se[3].play()
                    self.se[0].play()
                if self.count == self.keisu * (26 + 15):
                    self.hantei[1] = True
                    self.se[3].play()
                if self.count == self.keisu * (26 + 28):
                    self.hantei[2] = True
                    self.se[4].play()
                    self.se[1].play()
            else:
                if self.count == self.keisu * 56:
                    self.hantei[0] = True
                    
            if self.count >= sum(self.seq):
                self.active = False
                self.init = True
                
        else:
            self.image = self.invisible
        
        self.count += 1
        
        
class Rabbit(pygame.sprite.Sprite):
    
    def __init__(self, Player1):
        pygame.sprite.Sprite.__init__(self)
        
        self.active = False #これがTrueだと攻撃が開始する合図になる
        self.init = True
        self.count = 0
        self.active2 = False
        self.hantei = False
        

        self.anime_seq = [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,240] #usagiがでてくるアニメの設定

        
        self.invisible = pygame.image.load("./assets/invisible.png")
        
        #アニメ画像の登録
        self.animes, self.rect = anim_dic(Player1,18)
        
            
    def update(self):
        if self.active == True or self.active2 == True:
            #開始時初期化処理
            if self.init == True:
                self.count = 0
                self.active2 = False 
                self.hantei = False
                self.init = False
                
            #判定発生
            #if self.count == self.f_hantei:
               # self.hantei = True
                
            #アニメーションの再生　再生は一回限り
            self.image, end = anime_play(self.animes,self.anime_seq,self.count) 
            
            if self.count == 90:
               #self.effect.active = True
               self.active2 = True
               self.hantei = True
               #self.se.play()
                
            if self.count >= sum(self.anime_seq):
                #正常終了
                self.active = False
                self.active2 = False
                self.init = True
                
                return
        else:
            self.image = self.invisible
            
        self.count += 1
        
class Owl(pygame.sprite.Sprite):
    
    def __init__(self, Player1):
        pygame.sprite.Sprite.__init__(self)
        
        self.active = False #これがTrueだと攻撃が開始する合図になる
        self.init = True
        self.count = 0
        self.active2 = False
        self.active3 = False
        self.hantei = False
        self.crab = False

        self.anime_seq = [3,3,3,3,3,3,3,3,3,3,3,3] #usagiがでてくるアニメの設定
        self.anime_seql = [10,10,10,10,10,10]
        self.anime_seqf = [3,2,3,2,
                           3,2,3,2,
                           3,2,3,2,
                           3,2,3,2,
                           3,2,3,2,
                           3,2,3,2,
                           3,2,3,2,
                           3,2,3,2,
                           3,2,3,2]

        self.voice = pygame.mixer.Sound("./assets/se/owl.wav")
        self.invisible = pygame.image.load("./assets/invisible.png")
        
        #アニメ画像の登録
        self.animes, self.rect = anim_dic(Player1,19)
        self.animesl, rec = anim_dic(Player1,20)
        self.animesf, rec = anim_dic(Player1,21)
        self.animesfc, rec = anim_dic(Player1,22)
        
            
    def update(self):
        if self.active == True:
            #開始時初期化処理
            if self.init == True:
                self.count = 0
                self.active2 = False 
                self.active3 = False
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
                self.active2 = True
                self.count = 0
                self.init = True
                self.voice.play()
                
                return
        elif self.active2 == True:
            
            #アニメーションの再生　再生は一回限り
            self.image, end = anime_play(self.animesl,self.anime_seql,self.count, True)
            
            if self.count == 240:
                #正常終了
                self.active3 = True
                self.active2 = False
                self.count = 0
        elif self.active3 == True:
            
            if self.crab == True:
                self.image, end = anime_play(self.animesfc,self.anime_seqf,self.count)
            else:
                self.image, end = anime_play(self.animesf,self.anime_seqf,self.count)
            
            if self.count == 17 or self.count == 25 or self.count == 32 or self.count == 40 or self.count == 47  or self.count == 57 or self.count == 65 or self.count == 75 or self.count == 80:
                self.hantei = True
                
            if self.count >= sum(self.anime_seqf):
                #正常終了

                self.active3 = False
                self.init = True
        else:
            self.image = self.invisible
            
        self.count += 1