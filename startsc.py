# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 20:17:41 2022

@author: takep
"""

import pygame
from anim_dic import anim_dic
from anim_dic import anime_play


class Door(pygame.sprite.Sprite):
    
    def __init__(self, Player1):
        pygame.sprite.Sprite.__init__(self)
        
        self.active = False 
        self.init = True
        self.count = 0
        #self.effect = Effect(True,6,825 + a,230 + b,400,400,False,False,[3,3,3,3,3,3,5,5])
            
  
        self.invisible = pygame.image.load("./assets/invisible.png")
        
        #アニメ画像の登録
        self.animes, self.rect = anim_dic(Player1,23)
        self.p1 = Player1
        
        if Player1 == True:
            self.anime_seq = [3,3,3,3,3,3,3,3,3,3,3,40]
            self.se = pygame.mixer.Sound("./assets/se/close.wav")
        else:
            self.anime_seq = [40,3,3,3,3,3,3,3,3,3,3,3]
            self.se = pygame.mixer.Sound("./assets/se/open.wav")

            
    def update(self):
        if self.active == True:
            #開始時初期化処理
            if self.init == True:
                self.count = 0
                self.init = False
                
            #アニメーションの再生　再生は一回限り
            self.image, end = anime_play(self.animes,self.anime_seq,self.count) 
            
            if self.count == 40 and self.p1 == False:
               self.se.play()
            if self.count == 30 and self.p1 == True:
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


def show_start_screen(screen: pygame.Surface,background :pygame.image):
    font = pygame.font.Font(None, 70)
    pygame.display.set_caption('影絵ゲーム')

    op = Door(True)
    door_group = pygame.sprite.Group()
    door_group.add(op)
    
    clock = pygame.time.Clock()

    screen.blit(background, (0, 0))

    text = font.render("Press S to start", True, (200, 150, 0))
    screen.blit(text, (500, 500))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type != pygame.KEYDOWN:
                continue
            elif event.key == ord('s'):
                print('S')
                op.active = True
                break
        if op.active == True:
            break
        clock.tick(60)
        
    for i in range(sum(op.anime_seq)):
        screen.blit(background, (0, 0))
        door_group.update()
        door_group.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    return
    
class Win(pygame.sprite.Sprite):
    
    def __init__(self, Player1):
        pygame.sprite.Sprite.__init__(self)
        
        self.active = True
        self.init = True
        self.count = 0
        #self.effect = Effect(True,6,825 + a,230 + b,400,400,False,False,[3,3,3,3,3,3,5,5])
            
  
        self.invisible = pygame.image.load("./assets/invisible.png")
        
        #アニメ画像の登録
        self.animes, self.rect = anim_dic(Player1,24)
        self.p1 = Player1
        self.se = pygame.mixer.Sound("./assets/se/iyopon.wav")
        self.se.set_volume(0.25)
        
        self.anime_seq = []
        for i in range(24):
            self.anime_seq.append(7)
            
        self.image = self.animes[0]

            
    def update(self):
        if self.active == True:
            #開始時初期化処理
            if self.init == True:
                self.count = 0
                self.init = False
                self.image = self.animes[0]
                
            #アニメーションの再生　再生は一回限り
            if self.count > 75:
                self.image, end = anime_play(self.animes,self.anime_seq,self.count - 75) 
            
                
            
            if self.count == 75:
               self.se.play()
            
                
            if self.count >= sum(self.anime_seq):
                #正常終了
                self.active = False
                self.init = True
                
                return
            
        
        
            
            
        else:
            self.image = self.animes[-1]   
        #開始時より時間軸管理のためのカウント増加
        self.count += 1
clock = pygame.time.Clock()
def show_finish_screen(screen,finish, op, doorgroup, win1, win2):
    
    
    wingroup = pygame.sprite.Group()
    if finish == True:
        
        wingroup.add(win2)
    else:
        
        wingroup.add(win1)
        
    

    op.active = True
    c = 0
    for i in range(60):
        clock.tick(60)
    while True:
       
        screen.fill((50,50,50))
        wingroup.update()
        wingroup.draw(screen)
        doorgroup.update()
        doorgroup.draw(screen)
        pygame.display.flip()
        if c == 192:
            break
        clock.tick(40)
        c += 1
        
    


    pygame.display.flip()
    

    while True:
        for event in pygame.event.get():
            # ESCキーが押されたら終了
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_s):
                return 0
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_a):
                win1.active = True
                win1.init = True
                win2.active = True
                win2.init = True
                show_finish_screen(screen, finish, op, doorgroup, win1, win2)
                return 1
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_r):
                return 1
                
        clock.tick(30)