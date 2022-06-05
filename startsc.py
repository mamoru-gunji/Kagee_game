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
            if event.key == ord('q'):
                return
            elif event.key == ord('s'):
                print('S')
                return
        clock.tick(60)