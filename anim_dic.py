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
            animes = [pygame.image.load("./assets/Player1/norm1.png"),
                          pygame.image.load("./assets/Player1/norm2.png"),
                                pygame.image.load("./assets/Player1/norm3.png")]
            rect = pygame.Rect(100,400,300,500)
        else:
            animes = [pygame.image.load("./assets/Player2/norm1.png"),
                                pygame.image.load("./assets/Player2/norm2.png"),
                                pygame.image.load("./assets/Player2/norm3.png")]
            rect = pygame.Rect(1050,400,300,500)
            
    elif idnum == 1:#犬などのパートナーキャラの通常アニメ
        if(Player1 == True):
            animes = [pygame.image.load("./assets/Player1/part1.png"),
                                pygame.image.load("./assets/Player1/part1.png"),
                                pygame.image.load("./assets/Player1/part2.png"),
                                pygame.image.load("./assets/Player1/part3.png")]
            rect = pygame.Rect(250,520,100,100)
        else:
            animes = [pygame.image.load("./assets/Player2/part1.png"),
                                pygame.image.load("./assets/Player2/part1.png"),
                                pygame.image.load("./assets/Player2/part2.png"),
                                pygame.image.load("./assets/Player2/part3.png")]
            rect = pygame.Rect(830,520,100,100)
    elif idnum == 2:#カニの出現
        if(Player1 == True):
            animes = [pygame.image.load("./assets/Player1/crab1.png"),
                      pygame.image.load("./assets/Player1/crab2.png"),
                      pygame.image.load("./assets/Player1/crab3.png")]
            rect = pygame.Rect(0,0,100,100)
        else:
            animes = [pygame.image.load("./assets/Player2/crab1.png"),
                      pygame.image.load("./assets/Player2/crab2.png"),
                      pygame.image.load("./assets/Player2/crab3.png")]
            rect = pygame.Rect(0,0,100,100)
    
    return animes, rect
        