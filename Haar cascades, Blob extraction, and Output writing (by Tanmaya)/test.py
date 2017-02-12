#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 22:49:29 2016

@author: tanmaya
"""

import cv2
import numpy as np
f=open("list.txt", "r")
video=np.array([cv2.imread("Grayscale/"+y[:len(y)-2],0) for y in f])
background=np.median(video, axis=[0])
bg=np.array(background, dtype="uint8")
cv2.imwrite("background2.jpg", bg)