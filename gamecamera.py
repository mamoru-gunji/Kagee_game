# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 11:50:06 2022

@author: takep
"""
import multiprocessing
from yolo_take import detect


if __name__ == '__main__':
    detecting = multiprocessing.Process(
        target=detect.run,
        kwargs={
            'source': 0,
            'imgsz' :(480, 480),
            'weights': 'yolo_take/best.pt',
            
        }
    )
    detecting.start()
    
    detect.run(
            source=1,
            weights= 'yolo_take/best.pt',
            imgsz = (480,480),
            player = 1)
