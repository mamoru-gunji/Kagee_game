# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 18:13:21 2022

@author: takep
"""

import pygame
import warnings
warnings.filterwarnings('ignore')

#これはアニメーションデータをしまっている関数です。ここにアニメーションを登録します。idで管理されるのでどれがどのアニメか把握する必要あり

def anim_dic(Player1: bool, idnum):
    
    if idnum == 0:#プレイヤーの立ちアニメ
        if(Player1 == True):
            animes = [pygame.image.load("./assets/Player1/boy_0000.png"),
                      pygame.image.load("./assets/Player1/boy_0001.png"),
                      pygame.image.load("./assets/Player1/boy_0002.png"),
                      pygame.image.load("./assets/Player1/boy_0003.png"),
                      ]
            rect = pygame.Rect(0,0,300,500)
        else:
            animes = [pygame.image.load("./assets/Player2/girl_0000.png"),
                      pygame.image.load("./assets/Player2/girl_0001.png"),
                      pygame.image.load("./assets/Player2/girl_0002.png"),
                      pygame.image.load("./assets/Player2/girl_0003.png"),
                      pygame.image.load("./assets/Player2/girl_0004.png"),
                      pygame.image.load("./assets/Player2/girl_0005.png"),
                      pygame.image.load("./assets/Player2/girl_0006.png"),
                      pygame.image.load("./assets/Player2/girl_0007.png"),
                      pygame.image.load("./assets/Player2/girl_0008.png"),
                      pygame.image.load("./assets/Player2/girl_0009.png"),
                      pygame.image.load("./assets/Player2/girl_0010.png"),
                      pygame.image.load("./assets/Player2/girl_0011.png")]
            rect = pygame.Rect(0,0,300,500)
            
    elif idnum == 1:#犬などのパートナーキャラの通常アニメ
        if(Player1 == True):
            animes = [pygame.image.load("./assets/Player1/dog_0000.png"),
                      pygame.image.load("./assets/Player1/dog_0001.png"),
                      pygame.image.load("./assets/Player1/dog_0002.png"),
                      pygame.image.load("./assets/Player1/dog_0003.png"),
                      pygame.image.load("./assets/Player1/dog_0004.png"),
                      pygame.image.load("./assets/Player1/dog_0005.png"),
                      pygame.image.load("./assets/Player1/dog_0006.png"),
                      pygame.image.load("./assets/Player1/dog_0007.png"),
                      pygame.image.load("./assets/Player1/dog_0008.png"),
                      pygame.image.load("./assets/Player1/dog_0009.png"),
                      pygame.image.load("./assets/Player1/dog_0010.png"),
                      pygame.image.load("./assets/Player1/dog_0011.png"),]
            rect = pygame.Rect(0,0,100,100)
        else:
            animes = [pygame.image.load("./assets/Player2/eagle_0000.png"),
                      pygame.image.load("./assets/Player2/eagle_0001.png"),
                      pygame.image.load("./assets/Player2/eagle_0001.png"),
                      pygame.image.load("./assets/Player2/eagle_0002.png"),
                      pygame.image.load("./assets/Player2/eagle_0003.png"),
                      pygame.image.load("./assets/Player2/eagle_0004.png"),
                      pygame.image.load("./assets/Player2/eagle_0005.png"),
                      pygame.image.load("./assets/Player2/eagle_0006.png"),
                      pygame.image.load("./assets/Player2/eagle_0007.png"),
                      pygame.image.load("./assets/Player2/eagle_0008.png"),
                      pygame.image.load("./assets/Player2/eagle_0009.png"),
                      pygame.image.load("./assets/Player2/eagle_0010.png"),
                      pygame.image.load("./assets/Player2/eagle_0011.png"),]
            rect = pygame.Rect(0,0,100,100)
    elif idnum == 2:#カニの出現
        if(Player1 == True):
            animes = [pygame.image.load("./assets/Player1/club_0000.png"),
                      pygame.image.load("./assets/Player1/club_0001.png"),
                      pygame.image.load("./assets/Player1/club_0002.png"),
                      pygame.image.load("./assets/Player1/club_0003.png"),
                      pygame.image.load("./assets/Player1/club_0004.png"),
                      pygame.image.load("./assets/Player1/club_0005.png"),
                      pygame.image.load("./assets/Player1/club_0006.png"),
                      pygame.image.load("./assets/Player1/club_0007.png"),
                      pygame.image.load("./assets/Player1/club_0008.png"),
                      pygame.image.load("./assets/Player1/club_0009.png"),
                      pygame.image.load("./assets/Player1/club_0010.png"),
                      pygame.image.load("./assets/Player1/club_0011.png")]
            rect = pygame.Rect(0,0,100,100)
        else:
            animes = [pygame.image.load("./assets/Player2/club_0000.png"),
                      pygame.image.load("./assets/Player2/club_0001.png"),
                      pygame.image.load("./assets/Player2/club_0002.png"),
                      pygame.image.load("./assets/Player2/club_0003.png"),
                      pygame.image.load("./assets/Player2/club_0004.png"),
                      pygame.image.load("./assets/Player2/club_0005.png"),
                      pygame.image.load("./assets/Player2/club_0006.png"),
                      pygame.image.load("./assets/Player2/club_0007.png"),
                      pygame.image.load("./assets/Player2/club_0008.png"),
                      pygame.image.load("./assets/Player2/club_0009.png"),
                      pygame.image.load("./assets/Player2/club_0010.png"),
                      pygame.image.load("./assets/Player2/club_0011.png")]
            rect = pygame.Rect(0,0,100,100)
    elif idnum == 3:#プレイヤーの怯み
        if(Player1 == True):
            animes = [pygame.image.load("./assets/Player1/boy_damage_0000.png"),
                      pygame.image.load("./assets/Player1/boy_damage_0001.png"),
                      pygame.image.load("./assets/Player1/boy_damage_0002.png"),
                      pygame.image.load("./assets/Player1/boy_damage_0003.png"),
                      pygame.image.load("./assets/Player1/boy_damage_0004.png"),
                      pygame.image.load("./assets/Player1/boy_damage_0005.png"),
                      pygame.image.load("./assets/Player1/boy_damage_0006.png"),
                      pygame.image.load("./assets/Player1/boy_damage_0007.png"),
                      pygame.image.load("./assets/Player1/boy_damage_0008.png"),
                      pygame.image.load("./assets/Player1/boy_damage_0009.png"),
                      pygame.image.load("./assets/Player1/boy_damage_0010.png"),
                      pygame.image.load("./assets/Player1/boy_damage_0011.png"),
                      ]
            rect = pygame.Rect(100,400,100,100)
        else:
            animes = [pygame.image.load("./assets/Player2/girl_damage_0000.png"),
                      pygame.image.load("./assets/Player2/girl_damage_0001.png"),
                      pygame.image.load("./assets/Player2/girl_damage_0002.png"),
                      pygame.image.load("./assets/Player2/girl_damage_0003.png"),
                      pygame.image.load("./assets/Player2/girl_damage_0004.png"),
                      pygame.image.load("./assets/Player2/girl_damage_0005.png"),
                      pygame.image.load("./assets/Player2/girl_damage_0006.png"),
                      pygame.image.load("./assets/Player2/girl_damage_0007.png"),
                      pygame.image.load("./assets/Player2/girl_damage_0008.png"),
                      pygame.image.load("./assets/Player2/girl_damage_0009.png"),
                      pygame.image.load("./assets/Player2/girl_damage_0010.png"),
                      pygame.image.load("./assets/Player2/girl_damage_0011.png"),
                      ]
            rect = pygame.Rect(1050,400,100,100)
            
    elif idnum == 4:#プレイヤーの影絵出すアニメ
        if(Player1 == True):
            animes = [pygame.image.load("./assets/Player1/boy_hand_0000.png"),
                      pygame.image.load("./assets/Player1/boy_hand_0001.png"),
                      pygame.image.load("./assets/Player1/boy_hand_0002.png"),
                      pygame.image.load("./assets/Player1/boy_hand_0003.png"),
                      pygame.image.load("./assets/Player1/boy_hand_0004.png"),
                      pygame.image.load("./assets/Player1/boy_hand_0005.png"),
                      pygame.image.load("./assets/Player1/boy_hand_0006.png"),
                      pygame.image.load("./assets/Player1/boy_hand_0007.png"),
                      pygame.image.load("./assets/Player1/boy_hand_0008.png"),
                      pygame.image.load("./assets/Player1/boy_hand_0009.png"),
                      pygame.image.load("./assets/Player1/boy_hand_0010.png"),
                      pygame.image.load("./assets/Player1/boy_hand_0011.png"),
                      pygame.image.load("./assets/Player1/boy_hand_0012.png"),
                      pygame.image.load("./assets/Player1/boy_hand_0013.png"),
                      pygame.image.load("./assets/Player1/boy_hand_0014.png"),
                      pygame.image.load("./assets/Player1/boy_hand_0015.png"),
                      pygame.image.load("./assets/Player1/boy_hand_0016.png"),
                      pygame.image.load("./assets/Player1/boy_hand_0017.png")
                      ]
            rect = pygame.Rect(0,0,100,100)
        else:
            animes = [pygame.image.load("./assets/Player2/girl_hand_0000.png"),
                      pygame.image.load("./assets/Player2/girl_hand_0001.png"),
                      pygame.image.load("./assets/Player2/girl_hand_0002.png"),
                      pygame.image.load("./assets/Player2/girl_hand_0003.png"),
                      pygame.image.load("./assets/Player2/girl_hand_0004.png"),
                      pygame.image.load("./assets/Player2/girl_hand_0005.png"),
                      pygame.image.load("./assets/Player2/girl_hand_0006.png"),
                      pygame.image.load("./assets/Player2/girl_hand_0007.png"),
                      pygame.image.load("./assets/Player2/girl_hand_0008.png"),
                      pygame.image.load("./assets/Player2/girl_hand_0009.png"),
                      pygame.image.load("./assets/Player2/girl_hand_0010.png"),
                      pygame.image.load("./assets/Player2/girl_hand_0011.png"),
                      ]
            rect = pygame.Rect(0,-20,100,100)
            
    elif idnum == 5:#dogの強攻撃
        if(Player1 == True):#ハイド
                animes = [pygame.image.load("./assets/Player1/dog_hide_0000.png"),
                          pygame.image.load("./assets/Player1/dog_hide_0001.png"),
                          pygame.image.load("./assets/Player1/dog_hide_0002.png"),
                          pygame.image.load("./assets/Player1/dog_hide_0003.png"),
                          pygame.image.load("./assets/Player1/dog_hide_0004.png"),
                          pygame.image.load("./assets/Player1/dog_hide_0005.png"),
                          pygame.image.load("./assets/Player1/dog_hide_0006.png"),
                          pygame.image.load("./assets/Player1/dog_hide_0007.png"),
                          pygame.image.load("./assets/Player1/dog_hide_0008.png"),
                          pygame.image.load("./assets/Player1/dog_hide_0009.png"),
                          pygame.image.load("./assets/Player1/dog_hide_0010.png"),
                          pygame.image.load("./assets/Player1/dog_hide_0011.png")
                          ]
                rect = pygame.Rect(0,0,100,100)
        else:#アタック
                animes = [pygame.image.load("./assets/Player1/dog_strong_0000.png"),
                          pygame.image.load("./assets/Player1/dog_strong_0001.png"),
                          pygame.image.load("./assets/Player1/dog_strong_0002.png"),
                          pygame.image.load("./assets/Player1/dog_strong_0003.png"),
                          pygame.image.load("./assets/Player1/dog_strong_0004.png"),
                          pygame.image.load("./assets/Player1/dog_strong_0005.png"),
                          pygame.image.load("./assets/Player1/dog_strong_0006.png"),
                          pygame.image.load("./assets/Player1/dog_strong_0007.png"),
                          pygame.image.load("./assets/Player1/dog_strong_0008.png"),
                          pygame.image.load("./assets/Player1/dog_strong_0009.png"),
                          pygame.image.load("./assets/Player1/dog_strong_0010.png"),
                          pygame.image.load("./assets/Player1/dog_strong_0011.png"),
                          pygame.image.load("./assets/Player1/dog_strong_0012.png"),
                          pygame.image.load("./assets/Player1/dog_strong_0013.png"),
                          pygame.image.load("./assets/Player1/dog_strong_0014.png"),
                          pygame.image.load("./assets/Player1/dog_strong_0015.png"),
                          pygame.image.load("./assets/Player1/dog_strong_0016.png"),
                          pygame.image.load("./assets/Player1/dog_strong_0017.png"),
                          pygame.image.load("./assets/Player1/dog_strong_0018.png"),
                          pygame.image.load("./assets/Player1/dog_strong_0019.png"),
                          pygame.image.load("./assets/Player1/dog_strong_0020.png"),
                          pygame.image.load("./assets/Player1/dog_strong_0021.png"),
                          pygame.image.load("./assets/Player1/dog_strong_0022.png"),
                          pygame.image.load("./assets/Player1/dog_strong_0023.png")
                          ]
                rect = pygame.Rect(0,0,100,100)
                
    elif idnum == 6:#EF,斬撃と打撃単発
        if(Player1 == True):
            animes = [pygame.image.load("./assets/ef/claw/pipo-btleffect121_01.png"),
                      pygame.image.load("./assets/ef/claw/pipo-btleffect121_02.png"),
                      pygame.image.load("./assets/ef/claw/pipo-btleffect121_03.png"),
                      pygame.image.load("./assets/ef/claw/pipo-btleffect121_04.png"),
                      pygame.image.load("./assets/ef/claw/pipo-btleffect121_05.png"),
                      pygame.image.load("./assets/ef/claw/pipo-btleffect121_06.png"),
                      pygame.image.load("./assets/ef/claw/pipo-btleffect121_07.png"),
                      pygame.image.load("./assets/ef/claw/pipo-btleffect121_08.png"),
                      pygame.image.load("./assets/ef/claw/pipo-btleffect121_09.png"),
                      ]
            rect = pygame.Rect(0,0,100,100)
        else:
            animes = [pygame.image.load("./assets/ef/dageki/pipo-btleffect135_01.png"),
                      pygame.image.load("./assets/ef/dageki/pipo-btleffect135_02.png"),
                      pygame.image.load("./assets/ef/dageki/pipo-btleffect135_03.png"),
                      pygame.image.load("./assets/ef/dageki/pipo-btleffect135_04.png"),
                      pygame.image.load("./assets/ef/dageki/pipo-btleffect135_05.png"),
                      pygame.image.load("./assets/ef/dageki/pipo-btleffect135_06.png"),
                      ]
            rect = pygame.Rect(0,0,100,100)
    
    elif idnum == 7:#象
        if(Player1 == True):
            animes = [pygame.image.load("./assets/Player1/elephant_appear_0000.png"),
                      pygame.image.load("./assets/Player1/elephant_appear_0001.png"),
                      pygame.image.load("./assets/Player1/elephant_appear_0002.png"),
                      pygame.image.load("./assets/Player1/elephant_appear_0003.png"),
                      pygame.image.load("./assets/Player1/elephant_appear_0004.png"),
                      pygame.image.load("./assets/Player1/elephant_appear_0005.png"),
                      pygame.image.load("./assets/Player1/elephant_appear_0006.png"),
                      pygame.image.load("./assets/Player1/elephant_appear_0007.png"),
                      pygame.image.load("./assets/Player1/elephant_appear_0008.png"),
                      pygame.image.load("./assets/Player1/elephant_appear_0009.png"),
                      pygame.image.load("./assets/Player1/elephant_appear_0010.png"),
                      pygame.image.load("./assets/Player1/elephant_appear_0011.png")
                      ]
            rect = pygame.Rect(0,0,100,100)
        else:
            animes = [pygame.image.load("./assets/Player2/elephant_l_appear_0000.png"),
                      pygame.image.load("./assets/Player2/elephant_l_appear_0001.png"),
                      pygame.image.load("./assets/Player2/elephant_l_appear_0002.png"),
                      pygame.image.load("./assets/Player2/elephant_l_appear_0003.png"),
                      pygame.image.load("./assets/Player2/elephant_l_appear_0004.png"),
                      pygame.image.load("./assets/Player2/elephant_l_appear_0005.png"),
                      pygame.image.load("./assets/Player2/elephant_l_appear_0006.png"),
                      pygame.image.load("./assets/Player2/elephant_l_appear_0007.png"),
                      pygame.image.load("./assets/Player2/elephant_l_appear_0008.png"),
                      pygame.image.load("./assets/Player2/elephant_l_appear_0009.png"),
                      pygame.image.load("./assets/Player2/elephant_l_appear_0010.png"),
                      pygame.image.load("./assets/Player2/elephant_l_appear_0011.png")]
            rect = pygame.Rect(0,0,100,100)
            
    elif idnum == 8:#イーグルおよび犬の弱攻撃
        if(Player1 == True):#弱攻撃
            animes = [pygame.image.load("./assets/Player1/eagle_attack_0011.png"),
                      pygame.image.load("./assets/Player1/eagle_attack_0000.png"),
                      pygame.image.load("./assets/Player1/eagle_attack_0001.png"),
                      pygame.image.load("./assets/Player1/eagle_attack_0002.png"),
                      pygame.image.load("./assets/Player1/eagle_attack_0003.png"),
                      pygame.image.load("./assets/Player1/eagle_attack_0004.png"),
                      pygame.image.load("./assets/Player1/eagle_attack_0005.png"),
                      pygame.image.load("./assets/Player1/eagle_attack_0006.png"),
                      pygame.image.load("./assets/Player1/eagle_attack_0007.png"),
                      pygame.image.load("./assets/Player1/eagle_attack_0008.png"),
                      pygame.image.load("./assets/Player1/eagle_attack_0009.png"),
                      pygame.image.load("./assets/Player1/eagle_attack_0010.png"),
                      pygame.image.load("./assets/Player1/eagle_attack_0011.png")
                      ]
            rect = pygame.Rect(50,0,100,100)
        else:
            animes = [pygame.image.load("./assets/Player1/dog_attack_0000.png"),
                      pygame.image.load("./assets/Player1/dog_attack_0001.png"),
                      pygame.image.load("./assets/Player1/dog_attack_0002.png"),
                      pygame.image.load("./assets/Player1/dog_attack_0003.png"),
                      pygame.image.load("./assets/Player1/dog_attack_0004.png"),
                      pygame.image.load("./assets/Player1/dog_attack_0005.png"),
                      pygame.image.load("./assets/Player1/dog_attack_0006.png"),
                      pygame.image.load("./assets/Player1/dog_attack_0007.png"),
                      pygame.image.load("./assets/Player1/dog_attack_0008.png"),
                      pygame.image.load("./assets/Player1/dog_attack_0009.png"),
                      pygame.image.load("./assets/Player1/dog_attack_0010.png")]
            rect = pygame.Rect(0,0,100,100)
            
    elif idnum == 9:#エフェクト　防御と
        if(Player1 == True):#防御
            animes = [pygame.image.load("./assets/ef/deffence/effect_01.png"),
                      pygame.image.load("./assets/ef/deffence/effect_02.png"),
                      pygame.image.load("./assets/ef/deffence/effect_03.png"),
                      pygame.image.load("./assets/ef/deffence/effect_04.png"),
                      pygame.image.load("./assets/ef/deffence/effect_05.png"),
                      pygame.image.load("./assets/ef/deffence/effect_06.png"),
                      pygame.image.load("./assets/ef/deffence/effect_07.png"),
                      pygame.image.load("./assets/ef/deffence/effect_08.png"),
                      pygame.image.load("./assets/ef/deffence/effect_09.png"),
                      pygame.image.load("./assets/ef/deffence/effect_10.png"),
                      ]
            rect = pygame.Rect(50,0,100,100)
        else:
            animes = [pygame.image.load("./assets/Player2/elephant_0000.png"),
                      pygame.image.load("./assets/Player2/elephant_0001.png"),
                      pygame.image.load("./assets/Player2/elephant_0002.png"),
                      pygame.image.load("./assets/Player2/elephant_0003.png"),
                      pygame.image.load("./assets/Player2/elephant_0004.png"),
                      pygame.image.load("./assets/Player2/elephant_0005.png"),
                      pygame.image.load("./assets/Player2/elephant_0006.png"),
                      pygame.image.load("./assets/Player2/elephant_0007.png"),
                      pygame.image.load("./assets/Player2/elephant_0008.png"),
                      pygame.image.load("./assets/Player2/elephant_0009.png"),
                      pygame.image.load("./assets/Player2/elephant_0010.png"),
                      pygame.image.load("./assets/Player2/elephant_0011.png")]
            rect = pygame.Rect(0,0,100,100)
            
    elif idnum == 10:#必殺技の変身
        if(Player1 == True):#wolf
            animes = [pygame.image.load("./assets/Player1/wolf_0000.png"),
                      pygame.image.load("./assets/Player1/wolf_0001.png"),
                      pygame.image.load("./assets/Player1/wolf_0002.png"),
                      pygame.image.load("./assets/Player1/wolf_0003.png"),
                      pygame.image.load("./assets/Player1/wolf_0004.png"),
                      pygame.image.load("./assets/Player1/wolf_0005.png"),
                      pygame.image.load("./assets/Player1/wolf_0006.png"),
                      pygame.image.load("./assets/Player1/wolf_0007.png"),
                      pygame.image.load("./assets/Player1/wolf_0008.png"),
                      pygame.image.load("./assets/Player1/wolf_0009.png"),
                      pygame.image.load("./assets/Player1/wolf_0010.png"),
                      pygame.image.load("./assets/Player1/wolf_0011.png"),
                      pygame.image.load("./assets/Player1/wolf_0012.png"),
                      pygame.image.load("./assets/Player1/wolf_0013.png"),
                      pygame.image.load("./assets/Player1/wolf_0014.png"),
                      pygame.image.load("./assets/Player1/wolf_0015.png"),
                      pygame.image.load("./assets/Player1/wolf_0016.png"),
                      pygame.image.load("./assets/Player1/wolf_0017.png"),
                      pygame.image.load("./assets/Player1/wolf_0018.png"),
                      pygame.image.load("./assets/Player1/wolf_0019.png"),
                      pygame.image.load("./assets/Player1/wolf_0020.png"),
                      pygame.image.load("./assets/Player1/wolf_0021.png"),
                      pygame.image.load("./assets/Player1/wolf_0022.png"),
                      pygame.image.load("./assets/Player1/wolf_0023.png"),
                      ]
            rect = pygame.Rect(50,0,100,100)
        else:#archaeopteryx
            animes = [pygame.image.load("./assets/Player2/eagle_takeoff_0000.png"),
                      pygame.image.load("./assets/Player2/eagle_takeoff_0001.png"),
                      pygame.image.load("./assets/Player2/eagle_takeoff_0002.png"),
                      pygame.image.load("./assets/Player2/eagle_takeoff_0003.png"),
                      pygame.image.load("./assets/Player2/eagle_takeoff_0004.png"),
                      pygame.image.load("./assets/Player2/eagle_takeoff_0005.png"),
                      pygame.image.load("./assets/Player2/eagle_takeoff_0006.png"),
                      pygame.image.load("./assets/Player2/eagle_takeoff_0007.png"),
                      pygame.image.load("./assets/Player2/eagle_takeoff_0008.png"),
                      pygame.image.load("./assets/Player2/eagle_takeoff_0009.png"),
                      pygame.image.load("./assets/Player2/eagle_takeoff_0010.png"),
                      pygame.image.load("./assets/Player2/eagle_takeoff_0011.png"),
                      pygame.image.load("./assets/Player2/eagle_flip_0000.png"),
                      pygame.image.load("./assets/Player2/eagle_flip_0001.png"),
                      pygame.image.load("./assets/Player2/eagle_flip_0002.png"),
                      pygame.image.load("./assets/Player2/eagle_flip_0003.png"),
                      pygame.image.load("./assets/Player2/eagle_flip_0004.png"),
                      pygame.image.load("./assets/Player2/eagle_flip_0005.png"),
                      pygame.image.load("./assets/Player2/eagle_flip_0006.png"),
                      pygame.image.load("./assets/Player2/eagle_flip_0007.png"),
                      pygame.image.load("./assets/Player2/eagle_flip_0008.png"),
                      pygame.image.load("./assets/Player2/eagle_flip_0009.png"),
                      pygame.image.load("./assets/Player2/eagle_flip_0010.png"),
                      pygame.image.load("./assets/Player2/eagle_flip_0011.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_evo_0000.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_evo_0001.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_evo_0002.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_evo_0003.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_evo_0004.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_evo_0005.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_evo_0006.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_evo_0007.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_evo_0008.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_evo_0009.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_evo_0010.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_evo_0011.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_evo_0012.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_evo_0013.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_evo_0014.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_evo_0015.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_evo_0016.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_evo_0017.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_evo_0018.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_evo_0019.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_evo_0020.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_evo_0021.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_evo_0022.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_evo_0023.png"),
                      ]
            rect = pygame.Rect(0,0,100,100)
        
    
    elif idnum == 11:#イーグル　ハイドまでとアタック
        if(Player1 == True):#防御
            animes = [pygame.image.load("./assets/Player2/eagle_takeoff_0000.png"),
                      pygame.image.load("./assets/Player2/eagle_takeoff_0001.png"),
                      pygame.image.load("./assets/Player2/eagle_takeoff_0002.png"),
                      pygame.image.load("./assets/Player2/eagle_takeoff_0003.png"),
                      pygame.image.load("./assets/Player2/eagle_takeoff_0004.png"),
                      pygame.image.load("./assets/Player2/eagle_takeoff_0005.png"),
                      pygame.image.load("./assets/Player2/eagle_takeoff_0006.png"),
                      pygame.image.load("./assets/Player2/eagle_takeoff_0007.png"),
                      pygame.image.load("./assets/Player2/eagle_takeoff_0008.png"),
                      pygame.image.load("./assets/Player2/eagle_takeoff_0009.png"),
                      pygame.image.load("./assets/Player2/eagle_takeoff_0010.png"),
                      pygame.image.load("./assets/Player2/eagle_takeoff_0011.png"),
                      pygame.image.load("./assets/Player2/eagle_flip_0000.png"),
                      pygame.image.load("./assets/Player2/eagle_flip_0001.png"),
                      pygame.image.load("./assets/Player2/eagle_flip_0002.png"),
                      pygame.image.load("./assets/Player2/eagle_flip_0003.png"),
                      pygame.image.load("./assets/Player2/eagle_flip_0004.png"),
                      pygame.image.load("./assets/Player2/eagle_flip_0005.png"),
                      pygame.image.load("./assets/Player2/eagle_flip_0006.png"),
                      pygame.image.load("./assets/Player2/eagle_flip_0007.png"),
                      pygame.image.load("./assets/Player2/eagle_flip_0008.png"),
                      pygame.image.load("./assets/Player2/eagle_flip_0009.png"),
                      pygame.image.load("./assets/Player2/eagle_flip_0010.png"),
                      pygame.image.load("./assets/Player2/eagle_flip_0011.png"),
                      pygame.image.load("./assets/Player2/eagle_hide_0000.png"),
                      pygame.image.load("./assets/Player2/eagle_hide_0001.png"),
                      pygame.image.load("./assets/Player2/eagle_hide_0002.png"),
                      pygame.image.load("./assets/Player2/eagle_hide_0003.png"),
                      pygame.image.load("./assets/Player2/eagle_hide_0004.png"),
                      pygame.image.load("./assets/Player2/eagle_hide_0005.png"),
                      pygame.image.load("./assets/Player2/eagle_hide_0006.png"),
                      pygame.image.load("./assets/Player2/eagle_hide_0007.png"),
                      pygame.image.load("./assets/Player2/eagle_hide_0008.png"),
                      pygame.image.load("./assets/Player2/eagle_hide_0009.png"),
                      pygame.image.load("./assets/Player2/eagle_hide_0010.png"),
                      pygame.image.load("./assets/Player2/eagle_hide_0011.png")
                      ]
            rect = pygame.Rect(-30,0,100,100)
        else:
            animes = [pygame.image.load("./assets/Player2/eagle_strong_0000.png"),
                      pygame.image.load("./assets/Player2/eagle_strong_0001.png"),
                      pygame.image.load("./assets/Player2/eagle_strong_0002.png"),
                      pygame.image.load("./assets/Player2/eagle_strong_0003.png"),
                      pygame.image.load("./assets/Player2/eagle_strong_0004.png"),
                      pygame.image.load("./assets/Player2/eagle_strong_0005.png"),
                      pygame.image.load("./assets/Player2/eagle_strong_0006.png"),
                      pygame.image.load("./assets/Player2/eagle_strong_0007.png"),
                      pygame.image.load("./assets/Player2/eagle_strong_0008.png"),
                      pygame.image.load("./assets/Player2/eagle_strong_0009.png"),
                      pygame.image.load("./assets/Player2/eagle_strong_0010.png"),
                      pygame.image.load("./assets/Player2/eagle_strong_0011.png"),
                      pygame.image.load("./assets/Player2/eagle_strong_0012.png"),
                      pygame.image.load("./assets/Player2/eagle_strong_0013.png"),
                      pygame.image.load("./assets/Player2/eagle_strong_0014.png"),
                      pygame.image.load("./assets/Player2/eagle_strong_0015.png"),
                      pygame.image.load("./assets/Player2/eagle_strong_0016.png"),
                      pygame.image.load("./assets/Player2/eagle_strong_0017.png"),
                      pygame.image.load("./assets/Player2/eagle_strong_0018.png"),
                      pygame.image.load("./assets/Player2/eagle_strong_0019.png"),
                      pygame.image.load("./assets/Player2/eagle_strong_0020.png"),
                      pygame.image.load("./assets/Player2/eagle_strong_0021.png"),
                      pygame.image.load("./assets/Player2/eagle_strong_0022.png"),
                      pygame.image.load("./assets/Player2/eagle_strong_0023.png")
                      ]
            rect = pygame.Rect(-30,0,100,100)
    
    elif idnum == 12:#プレイヤー死亡
        if(Player1 == True):#防御
            animes = [pygame.image.load("./assets/Player1/boy_death_0000.png"),
                      pygame.image.load("./assets/Player1/boy_death_0001.png"),
                      pygame.image.load("./assets/Player1/boy_death_0002.png"),
                      pygame.image.load("./assets/Player1/boy_death_0003.png"),
                      pygame.image.load("./assets/Player1/boy_death_0004.png"),
                      pygame.image.load("./assets/Player1/boy_death_0005.png"),
                      pygame.image.load("./assets/Player1/boy_death_0006.png"),
                      pygame.image.load("./assets/Player1/boy_death_0007.png"),
                      pygame.image.load("./assets/Player1/boy_death_0008.png"),
                      pygame.image.load("./assets/Player1/boy_death_0009.png"),
                      pygame.image.load("./assets/Player1/boy_death_0010.png"),
                      pygame.image.load("./assets/Player1/boy_death_0011.png")
                      ]
            rect = pygame.Rect(0,0,100,100)
        else:
            animes = [pygame.image.load("./assets/Player2/girl_death_0000.png"),
                      pygame.image.load("./assets/Player2/girl_death_0001.png"),
                      pygame.image.load("./assets/Player2/girl_death_0002.png"),
                      pygame.image.load("./assets/Player2/girl_death_0003.png"),
                      pygame.image.load("./assets/Player2/girl_death_0004.png"),
                      pygame.image.load("./assets/Player2/girl_death_0005.png"),
                      pygame.image.load("./assets/Player2/girl_death_0006.png"),
                      pygame.image.load("./assets/Player2/girl_death_0007.png"),
                      pygame.image.load("./assets/Player2/girl_death_0008.png"),
                      pygame.image.load("./assets/Player2/girl_death_0009.png"),
                      pygame.image.load("./assets/Player2/girl_death_0010.png"),
                      pygame.image.load("./assets/Player2/girl_death_0011.png")
                      ]
            rect = pygame.Rect(0,0,100,100)
    elif idnum == 13:#パートナー死亡
        if(Player1 == True):#防御
            animes = [pygame.image.load("./assets/Player1/dog_death_kari_0000.png"),
                      pygame.image.load("./assets/Player1/dog_death_kari_0001.png"),
                      pygame.image.load("./assets/Player1/dog_death_kari_0002.png"),
                      pygame.image.load("./assets/Player1/dog_death_kari_0003.png"),
                      pygame.image.load("./assets/Player1/dog_death_kari_0004.png"),
                      pygame.image.load("./assets/Player1/dog_death_kari_0005.png"),
                      pygame.image.load("./assets/Player1/dog_death_kari_0006.png"),
                      pygame.image.load("./assets/Player1/dog_death_kari_0007.png"),
                      pygame.image.load("./assets/Player1/dog_death_kari_0008.png"),
                      pygame.image.load("./assets/Player1/dog_death_kari_0009.png"),
                      pygame.image.load("./assets/Player1/dog_death_kari_0010.png"),
                      pygame.image.load("./assets/Player1/dog_death_kari_0011.png")
                      ]
            rect = pygame.Rect(0,0,100,100)
        else:
            animes = [pygame.image.load("./assets/Player2/eagle_death_0000.png"),
                      pygame.image.load("./assets/Player2/eagle_death_0001.png"),
                      pygame.image.load("./assets/Player2/eagle_death_0002.png"),
                      pygame.image.load("./assets/Player2/eagle_death_0003.png"),
                      pygame.image.load("./assets/Player2/eagle_death_0004.png"),
                      pygame.image.load("./assets/Player2/eagle_death_0005.png"),
                      pygame.image.load("./assets/Player2/eagle_death_0006.png"),
                      pygame.image.load("./assets/Player2/eagle_death_0007.png"),
                      pygame.image.load("./assets/Player2/eagle_death_0008.png"),
                      pygame.image.load("./assets/Player2/eagle_death_0009.png"),
                      pygame.image.load("./assets/Player2/eagle_death_0010.png"),
                      pygame.image.load("./assets/Player2/eagle_death_0011.png")]
            rect = pygame.Rect(0,0,100,100)
            
    elif idnum == 14:#カニ死亡
        if(Player1 == True):#防御
            animes = [pygame.image.load("./assets/Player1/crub_death_0000.png"),
                      pygame.image.load("./assets/Player1/crub_death_0001.png"),
                      pygame.image.load("./assets/Player1/crub_death_0002.png"),
                      pygame.image.load("./assets/Player1/crub_death_0003.png"),
                      pygame.image.load("./assets/Player1/crub_death_0004.png"),
                      pygame.image.load("./assets/Player1/crub_death_0005.png"),
                      pygame.image.load("./assets/Player1/crub_death_0006.png"),
                      pygame.image.load("./assets/Player1/crub_death_0007.png"),
                      pygame.image.load("./assets/Player1/crub_death_0008.png"),
                      pygame.image.load("./assets/Player1/crub_death_0009.png"),
                      pygame.image.load("./assets/Player1/crub_death_0010.png"),
                      pygame.image.load("./assets/Player1/crub_death_0011.png")
                      ]
            rect = pygame.Rect(0,0,100,100)
        else:
            animes = [pygame.image.load("./assets/Player2/crub_death_l_0000.png"),
                      pygame.image.load("./assets/Player2/crub_death_l_0001.png"),
                      pygame.image.load("./assets/Player2/crub_death_l_0002.png"),
                      pygame.image.load("./assets/Player2/crub_death_l_0003.png"),
                      pygame.image.load("./assets/Player2/crub_death_l_0004.png"),
                      pygame.image.load("./assets/Player2/crub_death_l_0005.png"),
                      pygame.image.load("./assets/Player2/crub_death_l_0006.png"),
                      pygame.image.load("./assets/Player2/crub_death_l_0007.png"),
                      pygame.image.load("./assets/Player2/crub_death_l_0008.png"),
                      pygame.image.load("./assets/Player2/crub_death_l_0009.png"),
                      pygame.image.load("./assets/Player2/crub_death_l_0010.png"),
                      pygame.image.load("./assets/Player2/crub_death_l_0011.png")]
            rect = pygame.Rect(0,0,100,100)
            
            
    elif idnum == 15:#パートナー誕生
        if(Player1 == True):#防御
            animes = [pygame.image.load("./assets/Player1/dog_death_kari_0011.png"),
                      pygame.image.load("./assets/Player1/dog_death_kari_0010.png"),
                      pygame.image.load("./assets/Player1/dog_death_kari_0009.png"),
                      pygame.image.load("./assets/Player1/dog_death_kari_0008.png"),
                      pygame.image.load("./assets/Player1/dog_death_kari_0007.png"),
                      pygame.image.load("./assets/Player1/dog_death_kari_0006.png"),
                      pygame.image.load("./assets/Player1/dog_death_kari_0005.png"),
                      pygame.image.load("./assets/Player1/dog_death_kari_0004.png"),
                      pygame.image.load("./assets/Player1/dog_death_kari_0003.png"),
                      pygame.image.load("./assets/Player1/dog_death_kari_0002.png"),
                      pygame.image.load("./assets/Player1/dog_death_kari_0001.png"),
                      pygame.image.load("./assets/Player1/dog_death_kari_0000.png")
                      ]
            rect = pygame.Rect(0,0,100,100)
        else:
            animes = [pygame.image.load("./assets/Player2/eagle_death_0011.png"),
                      pygame.image.load("./assets/Player2/eagle_death_0010.png"),
                      pygame.image.load("./assets/Player2/eagle_death_0009.png"),
                      pygame.image.load("./assets/Player2/eagle_death_0008.png"),
                      pygame.image.load("./assets/Player2/eagle_death_0007.png"),
                      pygame.image.load("./assets/Player2/eagle_death_0006.png"),
                      pygame.image.load("./assets/Player2/eagle_death_0005.png"),
                      pygame.image.load("./assets/Player2/eagle_death_0004.png"),
                      pygame.image.load("./assets/Player2/eagle_death_0003.png"),
                      pygame.image.load("./assets/Player2/eagle_death_0002.png"),
                      pygame.image.load("./assets/Player2/eagle_death_0001.png"),
                      pygame.image.load("./assets/Player2/eagle_death_0000.png")]
            rect = pygame.Rect(0,0,100,100)
    elif idnum == 16:#バックグラウンドとカウントダウン
        if(Player1 == True):#背景
            animes = [pygame.image.load("./assets/BG_0000.png"),
                      pygame.image.load("./assets/BG_0001.png"),
                      pygame.image.load("./assets/BG_0002.png"),
                      pygame.image.load("./assets/BG_0003.png"),
                      pygame.image.load("./assets/BG_0004.png"),
                      pygame.image.load("./assets/BG_0005.png"),
                      pygame.image.load("./assets/BG_0006.png"),
                      pygame.image.load("./assets/BG_0007.png"),
                      pygame.image.load("./assets/BG_0008.png"),
                      ]
            rect = pygame.Rect(0,0,100,100)
        else:
            animes = [pygame.image.load("./assets/three.png"),
                      pygame.image.load("./assets/two.png"),
                      pygame.image.load("./assets/one.png"),
                      pygame.image.load("./assets/fight.png"),
                      ]
            rect = pygame.Rect(0,0,100,100)
    elif idnum == 17:#必殺技第二段階
        if(Player1 == True):#背景
            animes = [pygame.image.load("./assets/Player1/wolf_hide_0000.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0001.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0002.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0003.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0004.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0005.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0006.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0007.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0008.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0009.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0010.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0011.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0012.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0013.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0014.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0015.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0016.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0017.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0018.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0019.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0020.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0021.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0022.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0023.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0024.png"),
                      pygame.image.load("./assets/Player1/wolf_hide_0025.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0000.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0001.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0002.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0003.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0004.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0005.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0006.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0007.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0008.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0009.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0010.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0011.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0012.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0013.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0014.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0015.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0016.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0017.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0018.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0019.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0020.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0021.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0022.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0023.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0024.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0025.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0026.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0027.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0028.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0029.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0030.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0031.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0032.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0033.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0034.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0035.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0036.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0037.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0038.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0039.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0040.png"),
                      pygame.image.load("./assets/Player1/wolf_strong_0041.png"),
                      ]
            rect = pygame.Rect(0,0,100,100)
        else:
            animes = [pygame.image.load("./assets/Player2/archaeopteryx_hide_0000.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_hide_0001.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_hide_0002.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_hide_0003.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_hide_0004.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_hide_0005.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_hide_0006.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_hide_0007.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_hide_0008.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_hide_0009.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_hide_0010.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_hide_0011.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_hide_0012.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_hide_0013.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_hide_0014.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_hide_0015.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_hide_0016.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_hide_0017.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_hide_0018.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_hide_0019.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_hide_0020.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_hide_0021.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_hide_0022.png"),
                      pygame.image.load("./assets/Player2/archaeopteryx_hide_0023.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0000.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0001.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0002.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0003.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0004.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0005.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0006.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0007.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0008.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0009.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0010.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0011.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0012.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0013.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0014.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0015.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0016.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0017.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0018.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0019.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0020.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0021.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0022.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0023.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0024.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0025.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0026.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0027.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0028.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0029.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0030.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0031.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0032.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0033.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0034.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0035.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0036.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0037.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0038.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0039.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0040.png"),
                      pygame.image.load("./assets/Player2/aptrx_strong_0041.png")
                      ]
            rect = pygame.Rect(0,0,100,100)
            
    elif idnum == 18:#うさぎ
        if(Player1 == True):#背景
            animes = [pygame.image.load("./assets/Player1/rabbit_0000.png"),
                      pygame.image.load("./assets/Player1/rabbit_0001.png"),
                      pygame.image.load("./assets/Player1/rabbit_0002.png"),
                      pygame.image.load("./assets/Player1/rabbit_0003.png"),
                      pygame.image.load("./assets/Player1/rabbit_0004.png"),
                      pygame.image.load("./assets/Player1/rabbit_0005.png"),
                      pygame.image.load("./assets/Player1/rabbit_0006.png"),
                      pygame.image.load("./assets/Player1/rabbit_0007.png"),
                      pygame.image.load("./assets/Player1/rabbit_0008.png"),
                      pygame.image.load("./assets/Player1/rabbit_0009.png"),
                      pygame.image.load("./assets/Player1/rabbit_0010.png"),
                      pygame.image.load("./assets/Player1/rabbit_0011.png"),
                      pygame.image.load("./assets/Player1/rabbit_0012.png"),
                      pygame.image.load("./assets/Player1/rabbit_0013.png"),
                      pygame.image.load("./assets/Player1/rabbit_0014.png"),
                      pygame.image.load("./assets/Player1/rabbit_0015.png"),
                      pygame.image.load("./assets/Player1/rabbit_0016.png"),
                      pygame.image.load("./assets/Player1/rabbit_0017.png"),
                      pygame.image.load("./assets/Player1/rabbit_0018.png"),
                      pygame.image.load("./assets/Player1/rabbit_0019.png"),
                      pygame.image.load("./assets/Player1/rabbit_0020.png"),
                      pygame.image.load("./assets/Player1/rabbit_0021.png"),
                      pygame.image.load("./assets/Player1/rabbit_0022.png"),
                      pygame.image.load("./assets/Player1/rabbit_0023.png"),
                      pygame.image.load("./assets/Player1/rabbit_0024.png"),
                      pygame.image.load("./assets/Player1/rabbit_0025.png"),
                      pygame.image.load("./assets/Player1/rabbit_0026.png"),
                      pygame.image.load("./assets/Player1/rabbit_0027.png"),
                      pygame.image.load("./assets/Player1/rabbit_0028.png"),
                      pygame.image.load("./assets/Player1/rabbit_0029.png"),
                      pygame.image.load("./assets/Player1/rabbit_0030.png"),
                      pygame.image.load("./assets/Player1/rabbit_0031.png"),
                      pygame.image.load("./assets/Player1/rabbit_a_0000.png")        
                      ]
            rect = pygame.Rect(0,0,100,100)
        else:
            animes = [pygame.image.load("./assets/Player2/rabbit_l_0000.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0001.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0002.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0003.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0004.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0005.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0006.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0007.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0008.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0009.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0010.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0011.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0012.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0013.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0014.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0015.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0016.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0017.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0018.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0019.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0020.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0021.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0022.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0023.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0024.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0025.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0026.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0027.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0028.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0029.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0030.png"),
                      pygame.image.load("./assets/Player2/rabbit_l_0031.png"),
                      pygame.image.load("./assets/Player2/rabbit_a_l_0000.png") 
                      ]
            rect = pygame.Rect(0,0,100,100)
    elif idnum == 19:#owla
        if(Player1 == True):
            animes = [pygame.image.load("./assets/Player1/owl_a_0000.png"),
                      pygame.image.load("./assets/Player1/owl_a_0001.png"),
                      pygame.image.load("./assets/Player1/owl_a_0002.png"),
                      pygame.image.load("./assets/Player1/owl_a_0003.png"),
                      pygame.image.load("./assets/Player1/owl_a_0004.png"),
                      pygame.image.load("./assets/Player1/owl_a_0005.png"),
                      pygame.image.load("./assets/Player1/owl_a_0006.png"),
                      pygame.image.load("./assets/Player1/owl_a_0007.png"),
                      pygame.image.load("./assets/Player1/owl_a_0008.png"),
                      pygame.image.load("./assets/Player1/owl_a_0009.png"),
                      pygame.image.load("./assets/Player1/owl_a_0010.png"),
                      pygame.image.load("./assets/Player1/owl_a_0011.png")
                      ]
            rect = pygame.Rect(0,0,100,100)
        else:
            animes = [pygame.image.load("./assets/Player2/owl_a_l_0000.png"),
                      pygame.image.load("./assets/Player2/owl_a_l_0001.png"),
                      pygame.image.load("./assets/Player2/owl_a_l_0002.png"),
                      pygame.image.load("./assets/Player2/owl_a_l_0003.png"),
                      pygame.image.load("./assets/Player2/owl_a_l_0004.png"),
                      pygame.image.load("./assets/Player2/owl_a_l_0005.png"),
                      pygame.image.load("./assets/Player2/owl_a_l_0006.png"),
                      pygame.image.load("./assets/Player2/owl_a_l_0007.png"),
                      pygame.image.load("./assets/Player2/owl_a_l_0008.png"),
                      pygame.image.load("./assets/Player2/owl_a_l_0009.png"),
                      pygame.image.load("./assets/Player2/owl_a_l_0010.png"),
                      pygame.image.load("./assets/Player2/owl_a_l_0011.png")]
            rect = pygame.Rect(0,0,100,100)
    elif idnum == 20:#owlb
        if(Player1 == True):
            animes = [pygame.image.load("./assets/Player1/owl_b_0000.png"),
                      pygame.image.load("./assets/Player1/owl_b_0001.png"),
                      pygame.image.load("./assets/Player1/owl_b_0002.png"),
                      pygame.image.load("./assets/Player1/owl_b_0003.png"),
                      pygame.image.load("./assets/Player1/owl_b_0004.png"),
                      pygame.image.load("./assets/Player1/owl_b_0005.png"),
                      ]
            rect = pygame.Rect(0,0,100,100)
        else:
            animes = [pygame.image.load("./assets/Player2/owl_b_l_0000.png"),
                      pygame.image.load("./assets/Player2/owl_b_l_0001.png"),
                      pygame.image.load("./assets/Player2/owl_b_l_0002.png"),
                      pygame.image.load("./assets/Player2/owl_b_l_0003.png"),
                      pygame.image.load("./assets/Player2/owl_b_l_0004.png"),
                      pygame.image.load("./assets/Player2/owl_b_l_0005.png")
                      ]
            rect = pygame.Rect(0,0,100,100)
    elif idnum == 21:#owlhit
        if(Player1 == True):
            animes = [pygame.image.load("./assets/Player1/owl_hit_0000.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0001.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0002.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0003.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0004.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0005.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0006.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0007.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0008.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0009.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0010.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0011.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0012.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0013.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0014.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0015.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0016.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0017.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0018.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0019.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0020.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0021.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0022.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0023.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0024.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0025.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0026.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0027.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0028.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0029.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0030.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0031.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0032.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0033.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0034.png"),
                      pygame.image.load("./assets/Player1/owl_hit_0035.png")
                      ]
            rect = pygame.Rect(0,0,100,100)
        else:
            animes = [pygame.image.load("./assets/Player2/owl_hit_l_0000.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0001.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0002.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0003.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0004.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0005.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0006.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0007.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0008.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0009.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0010.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0011.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0012.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0013.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0014.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0015.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0016.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0017.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0018.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0019.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0020.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0021.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0022.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0023.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0024.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0025.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0026.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0027.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0028.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0029.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0030.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0031.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0032.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0033.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0034.png"),
                      pygame.image.load("./assets/Player2/owl_hit_l_0035.png")
                      ]
            rect = pygame.Rect(0,0,100,100)
    elif idnum == 22:#owlmiss
        if(Player1 == True):
            animes = [pygame.image.load("./assets/Player1/owl_miss_0000.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0001.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0002.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0003.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0004.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0005.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0006.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0007.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0008.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0009.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0010.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0011.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0012.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0013.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0014.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0015.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0016.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0017.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0018.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0019.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0020.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0021.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0022.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0023.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0024.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0025.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0026.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0027.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0028.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0029.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0030.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0031.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0032.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0033.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0034.png"),
                      pygame.image.load("./assets/Player1/owl_miss_0035.png")
                      ]
            rect = pygame.Rect(0,0,100,100)
        else:
            animes = [pygame.image.load("./assets/Player2/owl_miss_l_0000.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0001.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0002.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0003.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0004.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0005.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0006.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0007.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0008.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0009.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0010.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0011.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0012.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0013.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0014.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0015.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0016.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0017.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0018.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0019.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0020.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0021.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0022.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0023.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0024.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0025.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0026.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0027.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0028.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0029.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0030.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0031.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0032.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0033.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0034.png"),
                      pygame.image.load("./assets/Player2/owl_miss_l_0035.png")
                      ]
            rect = pygame.Rect(0,0,100,100)
    elif idnum == 23:#とびら
        if(Player1 == True):
            animes = [pygame.image.load("./assets/cut_general_0000.png"),
                      pygame.image.load("./assets/cut_general_0001.png"),
                      pygame.image.load("./assets/cut_general_0002.png"),
                      pygame.image.load("./assets/cut_general_0003.png"),
                      pygame.image.load("./assets/cut_general_0004.png"),
                      pygame.image.load("./assets/cut_general_0005.png"),
                      pygame.image.load("./assets/cut_general_0006.png"),
                      pygame.image.load("./assets/cut_general_0007.png"),
                      pygame.image.load("./assets/cut_general_0008.png"),
                      pygame.image.load("./assets/cut_general_0009.png"),
                      pygame.image.load("./assets/cut_general_0010.png"),
                      pygame.image.load("./assets/cut_general_0011.png")
                      ]
            rect = pygame.Rect(0,0,100,100)
        else:
            animes = [pygame.image.load("./assets/cut_general_0011.png"),
                      pygame.image.load("./assets/cut_general_0010.png"),
                      pygame.image.load("./assets/cut_general_0009.png"),
                      pygame.image.load("./assets/cut_general_0008.png"),
                      pygame.image.load("./assets/cut_general_0007.png"),
                      pygame.image.load("./assets/cut_general_0006.png"),
                      pygame.image.load("./assets/cut_general_0005.png"),
                      pygame.image.load("./assets/cut_general_0004.png"),
                      pygame.image.load("./assets/cut_general_0003.png"),
                      pygame.image.load("./assets/cut_general_0002.png"),
                      pygame.image.load("./assets/cut_general_0001.png"),
                      pygame.image.load("./assets/cut_general_0000.png")
                      ]
            rect = pygame.Rect(0,0,100,100)
    elif idnum == 24:#win
        if(Player1 == True):
            animes = [pygame.image.load("./assets/Player1/boy_win_0000.png"),
                      pygame.image.load("./assets/Player1/boy_win_0001.png"),
                      pygame.image.load("./assets/Player1/boy_win_0002.png"),
                      pygame.image.load("./assets/Player1/boy_win_0003.png"),
                      pygame.image.load("./assets/Player1/boy_win_0004.png"),
                      pygame.image.load("./assets/Player1/boy_win_0005.png"),
                      pygame.image.load("./assets/Player1/boy_win_0006.png"),
                      pygame.image.load("./assets/Player1/boy_win_0007.png"),
                      pygame.image.load("./assets/Player1/boy_win_0008.png"),
                      pygame.image.load("./assets/Player1/boy_win_0009.png"),
                      pygame.image.load("./assets/Player1/boy_win_0010.png"),
                      pygame.image.load("./assets/Player1/boy_win_0011.png"),
                      pygame.image.load("./assets/Player1/boy_win_0012.png"),
                      pygame.image.load("./assets/Player1/boy_win_0013.png"),
                      pygame.image.load("./assets/Player1/boy_win_0014.png"),
                      pygame.image.load("./assets/Player1/boy_win_0015.png"),
                      pygame.image.load("./assets/Player1/boy_win_0016.png"),
                      pygame.image.load("./assets/Player1/boy_win_0017.png"),
                      pygame.image.load("./assets/Player1/boy_win_0018.png"),
                      pygame.image.load("./assets/Player1/boy_win_0019.png"),
                      pygame.image.load("./assets/Player1/boy_win_0020.png"),
                      pygame.image.load("./assets/Player1/boy_win_0021.png"),
                      pygame.image.load("./assets/Player1/boy_win_0022.png"),
                      pygame.image.load("./assets/Player1/boy_win_0023.png")
                      ]
            rect = pygame.Rect(0,0,100,100)
        else:
            animes = [pygame.image.load("./assets/Player2/girl_win_0000.png"),
                      pygame.image.load("./assets/Player2/girl_win_0001.png"),
                      pygame.image.load("./assets/Player2/girl_win_0002.png"),
                      pygame.image.load("./assets/Player2/girl_win_0003.png"),
                      pygame.image.load("./assets/Player2/girl_win_0004.png"),
                      pygame.image.load("./assets/Player2/girl_win_0005.png"),
                      pygame.image.load("./assets/Player2/girl_win_0006.png"),
                      pygame.image.load("./assets/Player2/girl_win_0007.png"),
                      pygame.image.load("./assets/Player2/girl_win_0008.png"),
                      pygame.image.load("./assets/Player2/girl_win_0009.png"),
                      pygame.image.load("./assets/Player2/girl_win_0010.png"),
                      pygame.image.load("./assets/Player2/girl_win_0011.png"),
                      pygame.image.load("./assets/Player2/girl_win_0012.png"),
                      pygame.image.load("./assets/Player2/girl_win_0013.png"),
                      pygame.image.load("./assets/Player2/girl_win_0014.png"),
                      pygame.image.load("./assets/Player2/girl_win_0015.png"),
                      pygame.image.load("./assets/Player2/girl_win_0016.png"),
                      pygame.image.load("./assets/Player2/girl_win_0017.png"),
                      pygame.image.load("./assets/Player2/girl_win_0018.png"),
                      pygame.image.load("./assets/Player2/girl_win_0019.png"),
                      pygame.image.load("./assets/Player2/girl_win_0020.png"),
                      pygame.image.load("./assets/Player2/girl_win_0021.png"),
                      pygame.image.load("./assets/Player2/girl_win_0022.png"),
                      pygame.image.load("./assets/Player2/girl_win_0023.png"),
                      pygame.image.load("./assets/Player2/girl_win_0024.png"),
                      pygame.image.load("./assets/Player2/girl_win_0025.png"),
                      pygame.image.load("./assets/Player2/girl_win_0026.png"),
                      pygame.image.load("./assets/Player2/girl_win_0027.png"),
                      pygame.image.load("./assets/Player2/girl_win_0028.png"),
                      pygame.image.load("./assets/Player2/girl_win_0029.png"),
                      pygame.image.load("./assets/Player2/girl_win_0030.png"),
                      pygame.image.load("./assets/Player2/girl_win_0031.png"),
                      pygame.image.load("./assets/Player2/girl_win_0032.png"),
                      pygame.image.load("./assets/Player2/girl_win_0033.png"),
                      pygame.image.load("./assets/Player2/girl_win_0034.png"),
                      pygame.image.load("./assets/Player2/girl_win_0035.png"),
                      pygame.image.load("./assets/Player2/girl_win_0036.png"),
                      pygame.image.load("./assets/Player2/girl_win_0037.png"),
                      pygame.image.load("./assets/Player2/girl_win_0038.png"),
                      pygame.image.load("./assets/Player2/girl_win_0039.png"),
                      pygame.image.load("./assets/Player2/girl_win_0040.png"),
                      pygame.image.load("./assets/Player2/girl_win_0041.png"),
                      pygame.image.load("./assets/Player2/girl_win_0042.png"),
                      pygame.image.load("./assets/Player2/girl_win_0043.png"),
                      pygame.image.load("./assets/Player2/girl_win_0044.png"),
                      pygame.image.load("./assets/Player2/girl_win_0045.png"),
                      pygame.image.load("./assets/Player2/girl_win_0046.png"),
                      pygame.image.load("./assets/Player2/girl_win_0047.png")
                      ]
            rect = pygame.Rect(0,0,100,100)
            
    for i in range(len(animes)):
        animes[i] = animes[i].convert_alpha()
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
    
        