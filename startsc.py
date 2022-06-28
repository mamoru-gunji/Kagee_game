# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 20:17:41 2022

@author: takep
"""

import pygame


def show_start_screen(screen: pygame.Surface,background :pygame.image):
    font = pygame.font.Font(None, 70)
    pygame.display.set_caption('影絵ゲーム')


    clock = pygame.time.Clock()

    screen.blit(background, (0, 0))

    text = font.render("Press S to start", True, (200, 150, 0))
    screen.blit(text, (500, 300))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type != pygame.KEYDOWN:
                continue
            elif event.key == ord('s'):
                print('S')
                return
        clock.tick(60)
        
def show_finish_screen(screen,finish):
    font = pygame.font.Font(None, 70)



    clock = pygame.time.Clock()

    if finish == True:
        text = font.render("2Pwin!", True, (250, 50, 50))
    else:
        text = font.render("1Pwin!", True, (250, 50, 50))
        
    screen.blit(text, (600, 300))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type != pygame.KEYDOWN:
                continue
            elif event.key == ord('s'):
                return
        clock.tick(60)