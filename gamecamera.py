# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 11:50:06 2022

@author: takep & mg
"""
import multiprocessing
from yolo_take import detect
import cv2


def list_available_cameras():
    available_cameras = []
    for i in range(10):
        cap = cv2.VideoCapture(i)
        if not cap.isOpened():
            break
        camera_id = i
        available_cameras.append(camera_id)
        cap.release()

        if len(available_cameras) >= 2:
            return available_cameras

    print("No camera error")


if __name__ == "__main__":
    camera = list_available_cameras()
    detecting = multiprocessing.Process(
        target=detect.run,
        kwargs={
            "source": camera[0],
            "imgsz": (480, 480),
            "weights": "yolo_take/best.pt",
        },
    )
    detecting.start()

    detect.run(
        source=camera[1], weights="yolo_take/best.pt", imgsz=(480, 480), player=1
    )
