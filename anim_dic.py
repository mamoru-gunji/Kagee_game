# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 18:13:21 2022

@author: takep
"""

import pygame

#これはアニメーションデータをしまっている関数です。ここにアニメーションを登録します。idで管理されるのでどれがどのアニメか把握する必要あり

def anim_dic(Player1: bool, idnum):
    
    if idnum == 0:#プレイヤーの立ちアニメ
        if(Player1 == True):
            animes = [pygame.image.load("./assets/Player1/boy_kari_0000.png"),
                      pygame.image.load("./assets/Player1/boy_kari_0001.png"),
                      pygame.image.load("./assets/Player1/boy_kari_0002.png"),
                      pygame.image.load("./assets/Player1/boy_kari_0003.png"),
                      pygame.image.load("./assets/Player1/boy_kari_0004.png"),
                      pygame.image.load("./assets/Player1/boy_kari_0005.png"),
                      pygame.image.load("./assets/Player1/boy_kari_0006.png"),
                      pygame.image.load("./assets/Player1/boy_kari_0007.png"),
                      pygame.image.load("./assets/Player1/boy_kari_0008.png"),
                      pygame.image.load("./assets/Player1/boy_kari_0009.png"),
                      pygame.image.load("./assets/Player1/boy_kari_0010.png"),
                      pygame.image.load("./assets/Player1/boy_kari_0011.png")]
            rect = pygame.Rect(0,0,300,500)
        else:
            animes = [pygame.image.load("./assets/Player2/girl_kari_0000.png"),
                      pygame.image.load("./assets/Player2/girl_kari_0001.png"),
                      pygame.image.load("./assets/Player2/girl_kari_0002.png"),
                      pygame.image.load("./assets/Player2/girl_kari_0003.png"),
                      pygame.image.load("./assets/Player2/girl_kari_0004.png"),
                      pygame.image.load("./assets/Player2/girl_kari_0005.png"),
                      pygame.image.load("./assets/Player2/girl_kari_0006.png"),
                      pygame.image.load("./assets/Player2/girl_kari_0007.png"),
                      pygame.image.load("./assets/Player2/girl_kari_0008.png"),
                      pygame.image.load("./assets/Player2/girl_kari_0009.png"),
                      pygame.image.load("./assets/Player2/girl_kari_0010.png"),
                      pygame.image.load("./assets/Player2/girl_kari_0011.png")]
            rect = pygame.Rect(0,-20,300,500)
            
    elif idnum == 1:#犬などのパートナーキャラの通常アニメ
        if(Player1 == True):
            animes = [pygame.image.load("./assets/Player1/part0.png"),
                      pygame.image.load("./assets/Player1/part1.png"),
                      pygame.image.load("./assets/Player1/part1.png"),
                      pygame.image.load("./assets/Player1/part2.png"),
                      pygame.image.load("./assets/Player1/part3.png"),
                      pygame.image.load("./assets/Player1/part4.png"),
                      pygame.image.load("./assets/Player1/part5.png"),
                      pygame.image.load("./assets/Player1/part6.png"),
                      pygame.image.load("./assets/Player1/part7.png"),
                      pygame.image.load("./assets/Player1/part8.png"),
                      pygame.image.load("./assets/Player1/part9.png"),
                      pygame.image.load("./assets/Player1/part10.png"),
                      pygame.image.load("./assets/Player1/part11.png"),]
            rect = pygame.Rect(0,0,100,100)
        else:
            animes = [pygame.image.load("./assets/Player2/part0.png"),
                      pygame.image.load("./assets/Player2/part1.png"),
                      pygame.image.load("./assets/Player2/part1.png"),
                      pygame.image.load("./assets/Player2/part2.png"),
                      pygame.image.load("./assets/Player2/part3.png"),
                      pygame.image.load("./assets/Player2/part4.png"),
                      pygame.image.load("./assets/Player2/part5.png"),
                      pygame.image.load("./assets/Player2/part6.png"),
                      pygame.image.load("./assets/Player2/part7.png"),
                      pygame.image.load("./assets/Player2/part8.png"),
                      pygame.image.load("./assets/Player2/part9.png"),
                      pygame.image.load("./assets/Player2/part10.png"),
                      pygame.image.load("./assets/Player2/part11.png"),]
            rect = pygame.Rect(0,0,100,100)
    elif idnum == 2:#カニの出現
        if(Player1 == True):
            animes = [pygame.image.load("./assets/Player1/club0.png"),
                      pygame.image.load("./assets/Player1/club1.png"),
                      pygame.image.load("./assets/Player1/club2.png"),
                      pygame.image.load("./assets/Player1/club3.png"),
                      pygame.image.load("./assets/Player1/club4.png"),
                      pygame.image.load("./assets/Player1/club5.png"),
                      pygame.image.load("./assets/Player1/club6.png"),
                      pygame.image.load("./assets/Player1/club7.png"),
                      pygame.image.load("./assets/Player1/club8.png"),
                      pygame.image.load("./assets/Player1/club9.png"),
                      pygame.image.load("./assets/Player1/club10.png"),
                      pygame.image.load("./assets/Player1/club11.png")]
            rect = pygame.Rect(-10,50,100,100)
        else:
            animes = [pygame.image.load("./assets/Player2/club0.png"),
                      pygame.image.load("./assets/Player2/club1.png"),
                      pygame.image.load("./assets/Player2/club2.png"),
                      pygame.image.load("./assets/Player2/club3.png"),
                      pygame.image.load("./assets/Player2/club4.png"),
                      pygame.image.load("./assets/Player2/club5.png"),
                      pygame.image.load("./assets/Player2/club6.png"),
                      pygame.image.load("./assets/Player2/club7.png"),
                      pygame.image.load("./assets/Player2/club8.png"),
                      pygame.image.load("./assets/Player2/club9.png"),
                      pygame.image.load("./assets/Player2/club10.png"),
                      pygame.image.load("./assets/Player2/club11.png")]
            rect = pygame.Rect(0,0,100,100)
    elif idnum == 3:#プレイヤーの怯み
        if(Player1 == True):
            animes = [pygame.image.load("./assets/Player1/hirumi1.png"),
                      pygame.image.load("./assets/Player1/hirumi2.png"),
                      pygame.image.load("./assets/Player1/hirumi3.png")]
            rect = pygame.Rect(100,400,100,100)
        else:
            animes = [pygame.image.load("./assets/Player2/hirumi1.png"),
                      pygame.image.load("./assets/Player2/hirumi2.png"),
                      pygame.image.load("./assets/Player2/hirumi3.png")]
            rect = pygame.Rect(1050,400,100,100)
    
    return animes, rect


#アニメ再生用の関数！roopにもたいおうだぜ
def anime_play(animes, seq, count, roop = False):
    count2 = count
    end = False
    if roop == False:
        if count <= seq[0]:
            image = animes[0]
        elif count >= sum(seq):
            image = animes[-1]
            end = True
        else:
            hoge = 0
            for num in range(len(seq)):
                hoge += seq[num]
                if hoge >= count:
                    image = animes[num]
                    break
    else:
        while count2 >= sum(seq):
            count2 = count2 - sum(seq)
        if count2 < seq[0]:
            image = animes[0]
        else:
            hoge = 0
            for num in range(len(seq)):
                hoge += seq[num]
                if hoge > count2:
                    image = animes[num]
                    break
    return image, end
    
        